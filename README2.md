
Activate virtual env
```
source ./venv/bin/activate
```
To deactive venv:
```
deactivate
```

Start project
```
django-admin startproject blogger
```

Run all migration
```
python3 src/blogger/manage.py migrate
```

Create superuser
```
python3 src/blogger/manage.py createsuperuser
```


Start server
```
python3 src/blogger/manage.py runserver
```

Start app(component).
From src/blogger:
```
python3 manage.py startapp blogs
```

Change models:
```
python3 manage.py makemigrations && python3 manage.py migrate
```