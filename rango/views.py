from django.shortcuts import render
#Import the Category Model
from models import  Category, Page
from django.http import HttpResponse


#each view exists within the views.py file as a series of individual functions
#each view takes at least one argument - a HttpRequest object whichalso lives in the django.http module
#Each view must return a HttpResponse object. A simple HttpResponse object takes a string
#parameter representing the content of the page we wish to send to the client requesting the view
def index(request):
    # Query the db for a list of all categories currently stored
    # Order them by no lines in descending order
    # retrieve the top 5 only - or all if less than 5
    # place the list in our context_dict which will be passed to the template engine
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = { 'categories' : category_list}

    # Render the response and sent it back
    return render( request, 'rango/index.html', context_dict )


def category(request, category_name_slug):
    #create a context dictionary which we can pass to the template
    context_dict = {}
    try:
        #Can we find a category name slugh with the given name
        # if we can't, the .get(_ method raised a DoesNotExist exception
        #So the .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug = category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        pages = Page.objects.filter( category = category )
        #adds our result list to the template context under name pages.
        context_dict['pages'] = pages
        # Also add the category object from the database to the context_ dict
        # We'll use this in the template to verify that the category exists
        context_dict['category'] = category
    except:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays "no category" message
        pass

    #Render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

