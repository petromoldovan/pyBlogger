
Docs
---------------
The `blogger`(http://petromoldovan.pythonanywhere.com/) is Django app that provides basic blog functionality.

Home view of the app is a list of all existing blog posts. Any user can read and comment on 
any post. To facilitate navigation, users can filter blogs by their category property.

Authenticated users may write/edit blog posts, like or dislike particular posts, edit 
profiles and create categories.

Blog posts are created with `django-ckeditor` rich text editor that enables usage of formatted
html text as well usage of media. The library does it job but is susceptible to js attacks. 
I would like to substitute the library with a markdown parser in the future. 

`blogger` is organized in two apps: blogs and users.
- `blogs` - contains logic(posts, likes, categories, comments) related to blog itself.
- `users` - contains logic related to user management, profiles and authentication. 

###Dependencies
`blogger` uses number of external dependencies all of which are documented in `requirements.txt`

Deployment
---------------
Follow the steps from
https://www.youtube.com/watch?v=Y4c4ickks2A

Useful commands:
```
mkvirtualenv --python=/usr/bin/python3.8 myenv
pip install -r requirements.txt
```

Add this line in the setting
```
STATIC_ROOT = '/home/petromoldovan/pyBlogger/static'
python manage.py collectstatic 
```

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