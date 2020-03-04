from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def page_403(request):
    return render(request, 'page_403.html')


@login_required
def page_404(request):
    return render(request, 'page_404.html')


@login_required
def page_500(request):
    return render(request, 'page_500.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def detail(request):
    return render(request, 'detail.html')


@login_required
def contacts(request):
    return render(request, 'contacts.html')
