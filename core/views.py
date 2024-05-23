# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from item.models import Category, Item
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Prepare email
        subject = f"Contact Form Submission from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['***@mail.com']

        # Send email
        send_mail(subject, message_body, from_email, recipient_list)

        # Redirect to a success page or show a success message
        return redirect('core:contact_success')

    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def policy_view(request):
    return render(request, 'core/policy.html')