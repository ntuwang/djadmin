from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def general_elements(request):
    return render(request, 'general_elements.html')


@login_required
def calendar(request):
    return render(request, 'calendar.html')


@login_required
def icons(request):
    return render(request, 'icons.html')


@login_required
def glyphicons(request):
    return render(request, 'glyphicons.html')


@login_required
def inbox(request):
    return render(request, 'inbox.html')


@login_required
def invoice(request):
    return render(request, 'invoice.html')


@login_required
def media_gallery(request):
    return render(request, 'media_gallery.html')


@login_required
def typography(request):
    return render(request, 'typography.html')


@login_required
def widgets(request):
    return render(request, 'widgets.html')
