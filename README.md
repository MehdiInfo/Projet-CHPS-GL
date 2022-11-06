# Projet-CHPS-GL

## création d'un environnement local (all os)

```python
python3 -m venv env  # à faire une fois
#windows
env/Scripts/Activate.ps1 # env activé, à faire à chaque fois que vous voulez utiliser l'env local
#En cas d'erreur de droits d'execution de scripts, utiliser cette commande dans le powershell en admin:
set-executionpolicy unrestricted
#Mac OS / Linux
source env/bin/activate # env activé, à faire à chaque fois que vous voulez utiliser l'env local
# Pour les deux
pip install -r requirements.txt # à faire un fois pour installer les modules nécessaires
# si vous avez une erreur lors de l'installation des modules requits, suffit de mettre à jour votre python vers une version plus récente
```
## pour quitter l'env locale
```python
deactivate
```
## Lancer l'appli (doit se faire sous env local)

une fois votre env activé :
```python
python manage.py runserver
```
## Accès aux applications
http://127.0.0.1:8000/ -> beta-testeur(rapport de bugs..etc)
http://127.0.0.1:8000/dashboard -> pour le dashboard

## Erreur
Si vous avez des erreurs lors de l'installation je vous conseille de mettre à jour votre python, préviligiez une version récente.
