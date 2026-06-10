from django.shortcuts import render, get_object_or_404
from .models import Post, UpdateNote, VideoTutorial, DynamicPage, HomePageContent

def home(request):
    home_content = HomePageContent.objects.first()
    return render(request, 'website/index.html', {'home': home_content})

def software(request):
    page = get_object_or_404(DynamicPage, slug='software')
    return render(request, 'website/pages/dynamic_page.html', {'page': page})

def marketing(request):
    page = get_object_or_404(DynamicPage, slug='marketing')
    return render(request, 'website/pages/dynamic_page.html', {'page': page})

def infraestrutura(request):
    page = get_object_or_404(DynamicPage, slug='infraestrutura')
    return render(request, 'website/pages/dynamic_page.html', {'page': page})

def suporte(request):
    videos = VideoTutorial.objects.all().order_by('title')
    return render(request, 'website/pages/suporte.html', {'videos': videos})

def contato(request):
    page = get_object_or_404(DynamicPage, slug='contato')
    return render(request, 'website/pages/dynamic_page.html', {'page': page})

def updates(request):
    notes = UpdateNote.objects.all().order_by('-date')
    return render(request, 'website/pages/updates.html', {'notes': notes})

def dynamic_page(request, slug):
    from .models import DynamicPage
    page = get_object_or_404(DynamicPage, slug=slug, is_active=True)
    return render(request, 'website/pages/dynamic_page.html', {'page': page})
