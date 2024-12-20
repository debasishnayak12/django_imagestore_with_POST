## for creating admin user and password
my user = admin
my password = admin@123

 for creating superuser
** python manage.py createsuperuser
**<Username: admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.>**

 ## for running the server
** python manage.py runserver
**<Performing system checks...

## when run in debug=False 
**static files will not found so set in settings as <STATIC_URL = '/static/'
                                                        STATIC_ROOT = BASE_DIR / 'staticfiles'>
