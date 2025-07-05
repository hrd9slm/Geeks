# WeatherAlert – Application Météo Intelligente

## Description du projet

**WeatherAlert** est une application web développée en Python avec Flask. Elle permet :

-  De consulter la météo d'une ville en temps réel via l'API OpenWeather
-  De stocker les données météo (température, humidité, description) dans une base PostgreSQL
-  De générer une alerte automatique si pluie ou tempête sont détectées
-  De visualiser un graphique de température historique
-  D’accéder aux données via une API REST
-  D’utiliser une interface web simple en HTML

---

##  Fonctionnalités

- Interface utilisateur via Flask + Jinja2
- Appels à l’API OpenWeather
- Stockage dans PostgreSQL avec SQLAlchemy
- Alerte météo automatique (pluie/orage)
- API REST :
  - `POST /api/weather`
  - `GET /api/weather/<city>`
  - `GET /api/weather/<city>/chart`
- Génération de graphique matplotlib

---

## 🖥️ Technologies utilisées

- Python 3.10+
- Flask
- SQLAlchemy
- PostgreSQL
- Requests
- python-dotenv
- matplotlib
- OpenWeather API

---

## ⚙️ Installation et exécution (local)

### 📁 1. Cloner le projet

```bash
git clone 
cd weather-alert
```

###  2. Créer un environnement virtuel

```bash
python -m venv venv
#  Windows
venv\Scripts\activate
#  macOS / Linux
source venv/bin/activate
```

###  3. Installer les dépendances

```bash
pip install -r requirements.txt
```

###  4. Configurer les variables d’environnement

Créer un fichier `.env` dans le dossier principal :

```
API_KEY=ta_clé_openweather
DB_USER=postgres
DB_PASSWORD=ton_mot_de_passe
DB_NAME=weather_alert_db
DB_HOST=localhost
DB_PORT=5432
```

Tu peux obtenir une clé gratuite ici : https://openweathermap.org/api

###  5. Créer la base PostgreSQL

Lancer `psql`, pgAdmin ou un outil similaire, et exécuter :

```sql
CREATE DATABASE weather_alert_db;
```

###  6. Créer la table `weather`

Lancer ce script une fois :

```bash
python models.py
```

> Cela utilise SQLAlchemy pour créer automatiquement la table `weather`.

###  7. Lancer l'application

```bash
python app.py
```

L'application sera accessible à l’adresse :

```
http://127.0.0.1:5000/
```

---

##  Exemples d’API

###  POST : Ajouter météo pour une ville

```bash
curl -X POST http://127.0.0.1:5000/api/weather \
     -H "Content-Type: application/json" \
     -d "{\"city\": \"Paris\"}"
```

###  GET : Récupérer historique météo d'une ville

```bash
curl http://127.0.0.1:5000/api/weather/Paris
```

###  GET : Récupérer le graphique de température

Ouvrir dans navigateur :

```
http://127.0.0.1:5000/api/weather/Paris/chart
```

---

## 💻 Interface utilisateur

1. Lance `app.py`
2. Va sur : `http://localhost:5000/`
3. Entre le nom d’une ville
4. Clique sur **Rechercher**
5. Résultat :
   - Température, humidité, description
   - Alerte météo si applicable
   - Graphique des températures historiques

---

##  Auteur

- **Salma Harda**
- Projet réalisé lors du **Hackathon Python 2025**

