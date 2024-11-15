from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)

def home(request):
    logger.debug("home called")
    return render(request, 'events/home.html', {})

def vision(request):
    logger.debug("vision called")
    return render(request, 'events/vision.html', {'vision': vision})

def blog(request):
    logger.debug("blog called")
    return render(request, 'events/blog.html', {'blog': blog})

def firstblog(request):
    logger.debug("firstblog called")
    return render(request, 'events/firstblog.html', {'firstblog': firstblog})