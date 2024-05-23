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

        # Prepare email for the website admin
        admin_subject = f"Kitchen Comfort Contact Form Submission from {name}"
        admin_message_body = f"Client Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        admin_from_email = settings.DEFAULT_FROM_EMAIL
        admin_recipient_list = [settings.DEFAULT_FROM_EMAIL]

        # Send email to the website admin
        send_mail(admin_subject, admin_message_body, admin_from_email, admin_recipient_list)

        # Prepare email for the user
        user_subject = f"Hello {name}"
        user_message_body = f"Kitchen Comfort just received your mail and we want you to know you'll be hearing back from us in a bit.\n\nThank you"
        user_from_email = settings.DEFAULT_FROM_EMAIL
        user_recipient_list = [email]

        # Send email to the user
        send_mail(user_subject, user_message_body, user_from_email, user_recipient_list)


        # Redirect to a success page or show a success message
        return render (request, 'core/contact_success.html')

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