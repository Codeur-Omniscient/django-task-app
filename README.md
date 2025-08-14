# 📝 Django REST Framework - Todo API

Une API RESTful développée avec **Django REST Framework (DRF)** dans le but de mettre en pratique les concepts appris sur le framework.  
Cette application gère des tâches (todo) avec un système complet d'authentification, de permissions et de filtrage.

---

## 🚀 Fonctionnalités

- **Authentification par Token** (`rest_framework.authtoken`)
- **Permissions personnalisées** (accès restreint par utilisateur)
- **CRUD complet** (Créer, Lire, Mettre à jour, Supprimer des tâches)
- **Filtrage avancé** des données
- **Recherche** et **Tri** sur les champs
- **Tests automatisés** pour assurer la fiabilité

---

## 🛠️ Technologies utilisées

- **Python 3.11+**
- **Django 5+**
- **Django REST Framework**
- **SQLite** (par défaut, mais compatible avec PostgreSQL/MySQL)
- **django-filter** (pour filtrage, recherche, ordering)

---

## 📦 Installation et exécution

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/Codeur-Omniscient/django-task-app.git
cd django-task-app
```

### 2️⃣ Créer un environnement virtuel et l’activer

```bash
python -m venv venv
source venv/bin/activate     # Mac / Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 6️⃣ Lancer le serveur

```bash
python manage.py runserver
```

---

## 🔑 Authentification par Token

1. Crée un compte via `/admin` ou via une requête API.
2. Récupère un **token** en envoyant une requête POST à :

```
POST /auth/register/
{
  "username": "ton_username",
  "email": "ton_email@example.com",
  "password": "ton_password"
}
```

3. Utilise ce token dans les requêtes suivantes :

```
Authorization: Token <votre_token>
```

---

## 🔍 Points d’API principaux

| Méthode | Endpoint         | Description                   | Auth Requise |
| ------- | ---------------- | ----------------------------- | ------------ |
| GET     | `/tasks/list/`   | Liste toutes les tâches       | ✅           |
| POST    | `/tasks/create/` | Crée une nouvelle tâche       | ✅           |
| GET     | `/tasks/{id}/`   | Récupère une tâche spécifique | ✅           |
| PUT     | `/tasks/{id}/`   | Met à jour une tâche          | ✅           |
| DELETE  | `/tasks/{id}/`   | Supprime une tâche            | ✅           |

---

## 🔎 Filtrage, Recherche et Ordering

- **Filtrage** : `/tasks/list/?status=done`
- **Recherche** : `/tasks/list/?search=ma_tache`
- **Tri** : `/tasks/list/?ordering=title` ou `/tasks/list/?ordering=-created_at`

---

## 🧪 Lancer les tests

```bash
python manage.py test
```

---

## 📜 Licence

Ce projet est open-source et disponible sous la licence MIT.
