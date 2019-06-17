# Social_login_Django_Python_App
This is a test app which handles the facebook login button using python and django. When the user connects, it fetches the name and profile picture of the user (other things can be added) and gets the user access token of the user which is stored in the database.

# Requirements 

Prerequisites
1. Python3
2. Virtual environment



# Installation Instruction
1. Clone or download the repository.
2. Create a new virtual environment for the project. 

```
virtualenv -p python3 myenv
source myenv/bin/activate

```
 Dependencies
1. social-auth-app-django
```
pip install django social-auth-app-django 

```
2. Djago restframe work
```
pip install django djangorestframework
```
Running the App 
1. Run the migration 
```
python manage.py migrate
```
2. Start the application 
```
python manage.py runserver
```

# Important Notes
1. Add your app key and app secret in settings.py before starting the app

2. After starting the app change the address 127.0.0.1:8000 to localhost:8000 because facebook does not allow insecure http connection coming from local machine. One way to avoid this is install werkzeug for the certificates

3. Go to developers.facebook.com/ click on My Apps and then Add a New App.
4. Fill in the app name.
5. From Settings > Basic, copy your app id and secret key to SOCIAL_AUTH_FACEBOOK_KEY and SOCIAL_AUTH_FACEBOOK_SECRET
6.Click on Add a Platform and select Website
7. For site url put http://localhost:8000 , if running locally else your app web url.
8. And then in App Domains put localhost if running locally else put your website domain.
9. Now go to Products > Facebook Login > Settings and put http://localhost:8000/app/deauthorize/ in the Deauthorize Callback URL. Or '/app/deauthorize/' if not running locally.

# Extensions 

Chaging the URL can be avoided by instalaling SSL certificates. This can be done via Werkzeug.
```
pip install django_extensions Werkzeug pyOpen SSL
```
2. After that add django-extensions in settings.py 
```
'django_extensions',
```
3. To start the app runserver command changes after this, becuase to point to the location of the downloaded certificates for SSL. 
```
python manage.py runserver_plus --cert -file /tmp/cert

```
