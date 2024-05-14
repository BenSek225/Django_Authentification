from django.shortcuts import render, redirect

from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseForbidden
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import codecs


# Create your views here.


def connexion (request):
   if request.method == "POST":
      email = request.POST.get('email', None)
      password = request.POST.get('password', None)

      user = User.objects.filter(email=email).first()
      if user:
         auth_user = authenticate(username = user.username,   password = password)
         if auth_user:
            login(request, auth_user)
            return redirect('acceuil')
         else:
            print("Mot de passe incorrecte")
      else:
         print("L'utilisateur n'existe pas!")
      print("=="*5, " NEW POST: ", email, password, "=="*5)
   return render(request, 'connexion.html', {})


def inscription (request):
   error = False
   message =" "
   if request.method == "POST":
      name = request.POST.get('name', None)
      email = request.POST.get('email', None)
      password = request.POST.get('password', None)
      repassword = request.POST.get('repassword', None)

      # Email
      try:
         validate_email(email)
      except:
         error = True
         message = "Enter un email valide svp!"
      
      # Password
      if error == False:
         if password != repassword:
            error = True
            message = "Les deux mot de passe ne correspondent pas !"
      
      # Exist
      user = User.objects.filter(Q(email = email) | Q(username = name)).first()
      if user:
         error = True
         message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"

      # Enregistrement
      if error == False:
         user = User(
            username = name,
            email = email,
         )
         user.save()

         user.password = password
         user.set_password(user.password)
         user.save()
         print("=="*5, " NEW POST: ", name, email, password, repassword, "=="*5)

         return redirect('connexion')
      
   context = {
      'error':error,
      'message':message
   }
   return render(request, 'inscription.html', context)


@login_required(login_url='connexion')
def acceuil (request):
   name = request.user.username
   return render(request, 'acceuil.html', {'name': name})


def deconnexion (request):
   logout(request)
   return redirect ('connexion')


def forgot (request):
   error = False
   success = False
   message = ""

   if request.method == 'POST':
      email= request.POST.get('email')

      user = User.objects.filter(email = email).first()

      if user:
         print("En cour d'execution mot de passe oublier")

         token = default_token_generator.make_token(user)
         uid = urlsafe_base64_encode(force_bytes(user.id))
         current_site = request.META["HTTP_HOST"]
         context = {
            "token": token,
            "uid": uid,
            "domaine": f"http://{current_site}"
         }
         
         html = render_to_string("email.html", context)

         msg = EmailMessage(
            "Test Envoie d'email django, use template",
            html,
            "NWAARR-Entreprise <sekongobienvenu22@gmail.com>",
            [user.email]
         )

         msg.content_subtype = "html"
         msg.send()

         message = "En cour d'execution mot de passe oublier"
         success = True
      else:
         print("L'utilisateur n'existe pas !")

         error = True
         message = "L'utilisateur n'existe pas !"

   contextt = {
      'success': success,
      'error':error,
      'message':message
   }
   return render(request, 'forgot.html', contextt)


def update (request, token, uid):
   print("token:", token, "uid:", uid)

   try:
      user_id = urlsafe_base64_decode(uid)
      print("user_id:", user_id)
      decode_uid = codecs.decode(user_id, "utf-8")
      print("decode_uid:", decode_uid)
      user = User.objects.get(id=decode_uid)
      print("user:", user)
   except:
      return HttpResponseForbidden(
         "Vous n'aviez pas la permission de modifier ce mot de pass. Utilisateur introuvable"
      )

   check_token = default_token_generator.check_token(user, token)
   if not check_token:
      return HttpResponseForbidden(
         "Vous n'aviez pas la permission de modifier ce mot de pass. Votre Token est invalid ou a espiré"
      )

   error = False
   success = False
   message = ""
   if request.method == "POST":
      password = request.POST.get("password")
      repassword = request.POST.get("repassword")
      print("password:", password, "repassword:", repassword)
      if repassword == password:
         try:
            validate_password(password, user)
            user.set_password(password)
            user.save()

            success = True
            message = "votre mot de pass a été modifié avec succès!"
         except ValidationError as e:
            error = True
            message = str(e)
      else:
         error = True
         message = "Les deux mot de pass ne correspondent pas"

   context = {
      "error": error,
      "success": success,
      "message": message
   }

   return render(request, 'update.html', context)