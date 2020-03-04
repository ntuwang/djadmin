from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def form(request):
    return render(request, 'form.html')


@login_required
def form_advanced(request):
    return render(request, 'form_advanced.html')


@login_required
def form_validation(request):
    return render(request, 'form_validation.html')


@login_required
def form_wizards(request):
    return render(request, 'form_wizards.html')


@login_required
def form_upload(request):
    return render(request, 'form_upload.html')


@login_required
def form_buttons(request):
    return render(request, 'form_buttons.html')
