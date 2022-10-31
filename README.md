# Projet-CHPS-GL

## création d'un environement locale all os

```python
python -m venv env  # A faire une fois
env/Scripts/Activate.ps1 # env activé, à faire à chaque fois que vous voulez utiliser l'env local
pip install -r requirements.txt # à faire un fois pour installer les modules nécessaires
```
## pour quitter l'env locale
```python
deactivate
```
## Déployer le serveur

une fois votre env activé :
```python
python manage.py runserver
```