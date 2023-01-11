rm -rf venv/ &&
  sudo find . -path "*/migrations/*.py" -not -name "__init__.py" -delete &&
  sudo find . -path "*/migrations/*.pyc" -delete &&
  sudo find . -path "*/__pycache__/*" -delete &&
  rm ./mpmu/db.sqlite3
python -m venv venv &&
  source venv/bin/activate &&
  pip install -r requirements.txt &&
  export DJANGO_ENV=development &&
  python manage.py makemigrations &&
  python manage.py migrate &&
  python manage.py seed project &&
  python manage.py runserver 0.0.0.0:8000