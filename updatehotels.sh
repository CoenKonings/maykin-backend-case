# Activate python environment.
source .venv/bin/activate
cd src
# Update city and hotel data
python manage.py updatehotels
# Deactivate python environment
deactivate
