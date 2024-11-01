from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
from django.conf import settings
from django.contrib import messages
# Create your views here.
def homePage(request):
    return render(request,'index.html')

def headerSliderClassicPage(request):
    return render(request,'index--header-slider-classic.html')

def headerSliderPage(request):
    return render(request,'index--header-slider.html')

def homeClassicPage(request):
    return render(request,'index--home-classic.html')

def selfhostedClassicPage(request):
    return render(request,'index--selfhosted-classic.html')

def selfhostedPage(request):
    return render(request,'index--selfhosted.html')

def youtubeClassicPage(request):
    return render(request,'index--youtube-classic.html')

def youtubePage(request):
    return render(request,'index--youtube.html')

def cloudPage(request):
    return render(request,'cloudcomputing.html')

def courses(request):
    return render(request,'courses.html')

def course2(request):
    return render(request,'course2.html')


def course3(request):
    return render(request,'course3.html')

def course4(request):
    return render(request,'course4.html')

def course5(request):
    return render(request,'course5.html')

def course6(request):
    return render(request,'course6.html')

def course7(request):
    return render(request,'course7.html')


def pasteventsPage(request):
    return render(request,'pastevents.html')

def testimonialPage(request):
    return render(request,'testimonial.html')


def cloudkingPage(request):
    return render(request,'Life@cloudking.html')

def placementPage(request):
    return render(request,'placement.html')

def registration_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        state = request.POST.get('state')
        country = request.POST.get('country')
        
        # Save data to the model
        registration = RegistrationForm(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            course=course,
            state=state,
            country=country
        )
        registration.save()  # Save the instance to the database
        
        # Send confirmation email
        send_mail(
            'Registration Successful',
            f'Thank you for registering , {first_name} {last_name}!',
            'your_email@example.com',  # From email
            [email],  # To email
            fail_silently=False,
        )
        
        return redirect('success')  # Redirect to a success page or another view

    return render(request, 'index.html')

def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Debugging prints
        print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}, Message: {message}")

        # Ensure all fields are received
        if not all([name, phone, email, address, message]):
            return HttpResponse("Missing fields", status=400)

        try:
            contact = ContactForm(name=name, phone=phone, email=email, address=address, message=message)
            contact.save()
            return redirect('success')
        except Exception as e:
            print(f"Error saving contact: {e}")
            return HttpResponse("Error saving contact", status=500)
    
    return render(request, 'contact.html')


def contact_form_home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Debugging prints
        print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}, Message: {message}")

        # Ensure all fields are received
        if not all([name, phone, email, address, message]):
            return HttpResponse("Missing fields", status=400)

        try:
            # Save the form data to the database
            contact = ContactForm(name=name, phone=phone, email=email, address=address, message=message)
            contact.save()
            return redirect('success')
        except Exception as e:
            print(f"Error saving contact: {e}")
            return HttpResponse("Error saving contact", status=500)
    
    return render(request, 'index.html')

def success_page(request):
    return render(request, 'success.html')



import logging
logger = logging.getLogger(__name__)

def my_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course = request.POST.get('course')

        logger.debug(f"Received: {name}, {phone}, {email}, {course}")

        if name and phone and email and course:
            MyFormData.objects.create(name=name, phone=phone, email=email, course=course)
            messages.success(request, "Data saved successfully!")
            return redirect('success')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'index.html')


logger = logging.getLogger(__name__)

def ModalFormView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course = request.POST.get('course')
        logger.debug(f"Received: {name}, {phone}, {email}, {course}")

        if name and phone and email and course:
            # Save data to the database
            ModalForm.objects.create(name=name, phone=phone, email=email, course=course)
            messages.success(request, "Data saved successfully!")
            return redirect('success')  # Ensure you have a success URL or view
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'index.html')