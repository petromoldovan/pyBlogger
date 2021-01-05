
Docs
---------------
The `blogger`(http://petromoldovan.pythonanywhere.com/) is Django app that provides basic blog functionality.

Home view of the app is a list of all existing blog posts. Any user can read and comment on 
any post. To facilitate navigation, users can filter blogs by their category property.

Authenticated users may write/edit blog posts, like or dislike particular posts, edit 
profiles and create categories.

`blogger` is organized in two apps: blogs and users.
- `blogs` - contains logic(posts, likes, categories, comments) related to blog itself.
- `users` - contains logic related to user management, profiles and authentication. 

###Dependencies
`blogger` uses number of external dependencies all of which are documented in `requirements.txt`

Deployment
---------------
Follow the steps from
https://www.youtube.com/watch?v=Y4c4ickks2A

Development
---------------

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
python3 ./src/blogger/manage.py makemigrations && python3 ./src/blogger/manage.py migrate
```

Go to db shell
```
python3 ./src/blogger/manage.py dbshell
```

Show deps
```
pip freeze
```