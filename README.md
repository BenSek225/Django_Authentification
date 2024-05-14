# Projet d'Authentification Django

## Description

Ce projet est une application Django complète qui gère l'authentification et l'autorisation des utilisateurs. Il offre des fonctionnalités essentielles pour la gestion des comptes utilisateurs, notamment l'inscription des utilisateurs, la connexion, la réinitialisation de mot de passe et la gestion administrative des utilisateurs. Le projet est conçu avec Bootstrap pour une interface utilisateur responsive et attrayante.

## Fonctionnalités

- **Inscription des Utilisateurs** : Permet aux utilisateurs de créer un compte avec un nom d'utilisateur, un e-mail et un mot de passe.
- **Connexion des Utilisateurs** : Authentification sécurisée des utilisateurs avec e-mail et mot de passe.
- **Réinitialisation de Mot de Passe** : Les utilisateurs peuvent réinitialiser leur mot de passe via une vérification par e-mail.
- **Tableau de Bord** : Un tableau de bord personnalisé qui accueille l'utilisateur connecté.
- **Interface Admin** : Accès complet à l'interface d'administration de Django pour la gestion des utilisateurs et d'autres données.
- **Déconnexion** : Déconnexion sécurisée des utilisateurs en un clic.
- **Design Responsive** : Utilisation de Bootstrap pour garantir que l'application soit responsive et adaptée aux mobiles.

## Technologies Utilisées

- **Django** : Un framework web Python de haut niveau qui encourage le développement rapide et un design propre et pragmatique.
- **Bootstrap** : Un framework frontend puissant pour un développement web plus rapide et plus facile.
- **SQLite** : Base de données par défaut pour le développement Django.
- **HTML/CSS/JavaScript** : Technologies web standards pour la construction de l'interface utilisateur.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/yourusername/django-authentication-project.git
   cd django-authentication-project

2. Créez et activez un environnement virtuel :
    ```bash
    source monde/bin/activate  # Sur Windows, utilisez `monde\Scripts\activate`

3. Installez outils web que j'ai installer pour l'envoie d'email :
   ```bash
   pip install "django-anymail[sendinblue]"

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt

5. Appliquez les migrations :
   ```bash
   python manage.py migrate

6. Créez un superutilisateur pour accéder à l'interface d'administration :
   ```bash
   python manage.py createsuperuser

7. Démarrez le serveur de développement :
    ```bash
    python manage.py runserver

8. Ouvrez votre navigateur et accédez à http://127.0.0.1:8000 pour voir l'application.

## Utilisation

- **Inscription** : Créez un nouveau compte utilisateur.
- **Connexion** : Accédez à votre compte en utilisant votre e-mail et votre mot de passe.
- **Tableau de Bord** : Consultez votre tableau de bord personnalisé après vous être connecté.
- **Réinitialisation de Mot de Passe** : Utilisez la fonctionnalité de réinitialisation de mot de passe si vous oubliez votre mot de passe.
- **Admin** : Gérez les utilisateurs et d'autres données via l'interface d'administration Django à http://127.0.0.1:8000/admin.
