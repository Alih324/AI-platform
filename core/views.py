from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your message. We will get back to you soon.')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')

