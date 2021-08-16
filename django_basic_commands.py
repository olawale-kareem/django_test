
# part 1

# create a django project
# run the server
# create app
# configure app view
# create app url.py
# configure the project url, to include your new app url


#  python3 -m django --version  # to check django version
#  django-admin startproject <project_name>      # to start a project <project_name>
#  python manage.py runserver        # run this command from the outer directory given when u create a new django project.
#  python manage.py startapp polls


# The difference between an app and a polls app.
# An app is a web application that does something e.g a weblog system, adb public records, a small poll app.
# A project is a collection of configuration and apps for a particular website, a project can contain multiple site.

# The include() function allows referencing other URLconfs
# The idea behind include() is to make it easy to plug-and-play URLs
# when to use include? You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.

# The path()
# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
#  At this point, it’s worth reviewing what these arguments are for.

# path() argument : route
# route is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
# Patterns don’t search GET and POST parameters, or the domain name.
# For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/.
# In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

# path() argument : view
# When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.
# We’ll give an example of this in a bit.


# part 2
# set-up db: a db of choice
# python manage.py migrate  # run migrations to register your changes
# create models, models are database table eqivalent of what happens when you use the db.
# models in django are like apps
# python manage.py makemigrations polls : run makemigrations to install or plug your model
# python manage.py sqlmigrate polls 0001 : displays the models created and their relationships
# python manage.py migrate :run again after makemigrations to create the models in db

# ----- django API/ shell is use to explore the database, here we can import the models created and play with it
# python manage.py shell  # to enter the shell
# use the django API TO QUERY the models we just created

# from polls.models import Choice, Question
# from django.utils import timezone
# Question.objects.all() # to check the question model
# Choice.objects.all() # to check the choice model
# q = Question(question_text="What's new?", pub_date=timezone.now()) # create an instance of the Question model.
# q.save() # to commit the changes to the db
# q.id # displays the object or question id.
# q.question_text. displays the object field value
# q.pub_date. the publication date.
# q.question_text = "What's up?"  # changing a model field
# q.save() # save immediately after the change.

#  Question.objects.filter(id=1)
#   Question.objects.filter(question_text__startswith='What')
#   from django.utils import timezone
#   current_year = timezone.now().year
#   Question.objects.get(pub_date__year=current_year)
#   Question.objects.get(id=2)
#   q = Question.objects.get(pk=1) #get the question with a primary key of one.
#   q.choice_set.all() # display choices
#   q.choice_set.create(choice_text='Not much', votes=0)
#   q.choice_set.create(choice_text='The sky', votes=0)
#   c = q.choice_set.create(choice_text='Just hacking again', votes=0)
#   c.question
#   q.choice_set.all()
#   q.choice_set.count()

#  The API automatically follows relationships as far as you need.
#  Use double underscores to separate relationships.
#  This works as many levels deep as you want; there's no limit.
#  Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
# Choice.objects.filter(question__pub_date__year=current_year)
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
#  Let's delete one of the choices. Use delete() for that.
#  c = q.choice_set.filter(choice_text__startswith='Just hacking')
#  c.delete()

# part 2 continuation
# creating an admin user
# python manage.py createsuperuser
# admin parameters:
                # admin name: mark
                #. admin mail: olawalekareemdev@gmail.com
                # password: saviourjesus11
# make the app modifiable in admin by making neccessary changes in the admin file of the app.


# part 3
# views
# The view returns primary an hhttp response or an exception
# our view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not.
# It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

# you could hardcode anything in hte views and display it with the urll call.
# This is the use of the template.
# Template namespacing: This is pointing django to the right template folder of an application, this is done by putting those templates inside another directory named for the app itself.

# The render(): shortcut
# it is used to return a  request or HttpResponse, load a template and fill a context.
# No need to use the HttpResponse module and the loader module.
# you will only need the HttpResponse modeule for stub functions.
# raising a 404 error


# part4
# write  a norminal form
# write corresponding view to process it
# a race condition: a condition caused by two users demanding access to your web  infrastructure that requires the view to perform an operation and return result at the same time.

#  generic views
#  django has in-built generic view, instead of writing your oown view that when called by a url fetches from a db, loads a template and return a rendered template.
#  it saves time and results in less code.
# to use generic views you need to do the following...
        # Convert the URLconf.
        # Delete some of the old, unneeded views.
        # Introduce new views based on Django’s generic views.




# part 5
# automated test
# Tests are routines that check the operation of your code.
# What’s different in automated tests is that the testing work is done for you by the system.
# You create a set of tests once, and then as you make changes to your app, you can check that your code still works as you originally intended,
# without having to perform time consuming manual testing.


# part 6
# working with static files
# Warning

# The {% static %} template tag is not available for use in static files which aren’t generated by Django,
# like your stylesheet. You should always use relative paths to link your static files between each other,
# because then you can change STATIC_URL (used by the static template tag to generate its URLs) without having to modify a bunch of paths in your static files as well.


# part 7
# customizing the automatically generated admin site
# to customise the admin ..  follow the pattern below
# You’ll follow this pattern – create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.
#
# This particular change above makes the “Publication date” come before the “Question” field:
