# Readings: Django Custom User

## Django Custom User Model:

  - The official Django documentation highly recommends using a custom user model for new projects.
  - The reason is if you want to make any changes to the User model down the road--for example adding a date of birth field--using a custom user model from the beginning makes this quite easy.
  - But if you do not, updating the default User model in an existing Django project is very, very challenging.
  
  - **Setup**:

     - 1 - create a new auth directory for our code on the Desktop
     - 2 - install Django with Pipenv
     - 3 - start the virtual environment shell
     - 4 - create a new Django project called config
     - 5 - create a new Sqlite database with migrate
     - 6 - run the local server
     
 - **The Django auth app**:
    - Django automatically installs the auth app when a new project is created.
    - Look in the config/settings.py file under INSTALLED_APPS and you can see auth is one of several built-in apps Django has installed for us.
    
- **Login Page**:
  - To make our login page! Django by default will look within a templates folder called registration for auth templates.
  - The login template is called login.html.
  - Create a new directory called registration and the requisite login.html file within it. 
  - From the command line type Control-c to quit our local server and enter the following commands: 
  -  ```
      (accounts) $ mkdir templates
      (accounts) $ mkdir templates/registration
      (accounts) $ touch templates/registration/login.html
     ```
- **Create users**:
  - we haven't created any users yet. Let's do that by making a superuser account from the command line.
  - Quit the server with Control+c and then run the command python manage.py createsuperuser.
  - Answer the prompts and note that your password will not appear on the screen when typing for security reasons.
  
- **Create a homepage**
  - We want a simple homepage that will display one message to logged out users and another to logged in users.
  - First quit the local server with Control+c and then create new base.html and home.html files.
  - Note that these are located within the templates folder but not within templates/registration/ where Django auth looks by default for user auth templates.
  
- **Logout link**:
  - Let's add a logout link to our page so users can easily toggle back and forth between the two states.
  - Fortunately, the Django auth app already provides us with a built-in URL and view for this.
  - And if you think about it, we don't need to display anything on logout so there's no need for a template.
  - All really we do after a successful "logout" request is redirected to another page.

- **Conclusion**:
  - With very little code we have a robust login and logout authentication system.
  - One of the nice things about Django is while it provides a lot of functionality out-of-the-box, it's designed to be customizable too.
  
---

## Substituting a custom User model:
  - Some kinds of projects may have authentication requirements for which Django’s built-in User model is not always appropriate.
  - For instance, on some sites it makes more sense to use an email address as your identification token instead of a username.
  - Django allows you to override the default user model by providing a value for the AUTH_USER_MODEL setting that references a custom model:
  - **Using a custom user model when starting a project**:
      If you’re starting a new project, it’s highly recommended to set up a custom user model, even if the default User model is sufficient for you. This model behaves identically to the default user model, but you’ll be able to customize it in the future if the need arises:
      ```
        from django.contrib.auth.models import AbstractUser

        class User(AbstractUser):
            pass
      ```
      Don’t forget to point AUTH_USER_MODEL to it. Do this before creating any migrations or running manage.py migrate for the first time.

      Also, register the model in the app’s admin.py:
      ```
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User
        
        admin.site.register(User, UserAdmin)
        
      ```