from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    new = "This is a string"
    return render(request, "home/index.html", {

    })


def about(request):
    return render(request, "home/about.html", {

    })


def projects(request):
    """
    The projects can be a list, with an initial scroll feature (found in the index.html) of my best projects, the list can then have several options, for timescale of project, complexity and otehr values.
    """
    return render(request, "home/projects.html", {})


def articles(request):
    """
    List of all the articles I have published.
    Smae here have a carousel on the home page, with search features on the article page - articles can be stored in the database?
    """
    return render(request, "home/articles.html", {})
