
# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserCreationFormWithProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .models import ContactMessage  # Import your model to save data to the database
from .models import Feedback
from .forms import EventBookingForm
from django.http import HttpResponse
from .models import Payment
from .models import Event
from datetime import datetime
from .models import Event




def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'concert/register.html')



def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, f"Welcome back,{username}!")
            return redirect('home')  # Redirect to home page or any other page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'concert/login.html')



def home(request):
    return render(request,"concert/index.html")

def search_events(request):
    events = Event.objects.all()  # Fetch events from the database
    return render(request, 'search_result.html', {'events': events})

def forgetpassword(request):
    return render(request,"concert/forgetpassword.html")
def events(request):
    return render(request,"concert/events.html")
def anirudh(request):
    return render(request,"concert/anirudh.html")
def yuvan(request):
    return render(request,"concert/yuvan.html")
def harris(request):
    return render(request,"concert/harris.html")
def arrahman(request):
    return render(request,"concert/arrahman.html")
def bookticket(request):
    return render(request,"concert/bookticket.html" )
def Newsletter(request):
    return render(request,"concert/Newsletter.html" )


def book_ticket(request):
    if request.method == "POST":
        # Handle form data and process the ticket booking
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        seating = request.POST.get('seating')
        tickets = request.POST.get('tickets')

        # Here, you can save the data or process the payment
        # You can also send an email or confirm the booking.

        return render(request, 'payment.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'seating': seating,
            'tickets': tickets,
        })
    else:
        return render(request, 'bookticket.html')  # In case of non-POST request

def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        # Logic to save feedback (e.g., save to database)
        print(f"Feedback Received: {name}, {email}, {rating}, {feedback}")

        # Redirect to a thank-you page or display success message
        return render(request, "concert/thank_you.html", {'name': name})
    else:
        return render(request, "concert/feedback.html")
def feedback(request):
    return render(request,"concert/feedback.html" )

def subscribe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Save to database or send to email service
        print(f"New Subscriber: {name} ({email})")

        # Redirect to a thank-you page or confirmation message
        return render(request, 'concert/thank__you.html', {'name': name})
    else:
        return render(request, 'concert/Newsletter.html')
def contactus(request):
    if request.method == 'POST':
        # Get data from the form fields
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Basic validation (e.g., ensure fields are not empty)
        if name and email and subject and message:
            # Save the message to the database (optional)
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            # Add a success message
            messages.success(request, "Your message has been submitted successfully!")

            # Redirect to avoid form resubmission on page refresh
            return redirect('contactus')
        else:
            # Add an error message if any field is empty
            messages.error(request, "Please fill in all fields.")

    # Render the contact us page with an empty form initially
    return render(request, 'concert/contactus.html')

# views.py

def feedback(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')
        rating = request.POST.get('rating')

        # Validate the form data (check that rating is a valid number)
        if name and email and feedback_text and rating.isdigit() and 1 <= int(rating) <= 5:
            # Save feedback to the database
            Feedback.objects.create(
                name=name,
                email=email,
                feedback=feedback_text,
                rating=int(rating)
            )

            # Display a success message
            messages.success(request, "Thank you for your feedback!")

            # Redirect to avoid form resubmission
            return redirect('feedback')  # Use the same view name for redirect
        else:
            # Display an error message if validation fails
            messages.error(request, "Please fill in all fields and provide a valid rating.")

    return render(request, 'concert/feedback.html')


def book_event(request):
    if request.method == 'POST':
        form = EventBookingForm(request.POST)
        if form.is_valid():
            # Save the booking data
            form.save()

            # Display a success message
            messages.success(request, "Your booking has been successfully saved!")

            # Redirect to the payment page
            return redirect('payment')  # Ensure you have a 'payment' URL set in urls.py
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = EventBookingForm()

    return render(request, 'concert/bookticket.html', {'form': form})





from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment
from datetime import datetime

def process_payment(request):
    if request.method == 'POST':
        # Extract data from the POST request
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')  # In YYYY-MM format
        cvv = request.POST.get('cvv')

        try:
            # Convert expiry_date to YYYY-MM-DD format
            expiry_date = datetime.strptime(expiry_date + '-01', '%Y-%m-%d').date()

            # Save payment details
            payment = Payment.objects.create(
                card_name=card_name,
                card_number=card_number[-4:],  # Store only the last 4 digits for security
                expiry_date=expiry_date,
                cvv=cvv  # Avoid saving CVV in production!
            )
            payment.save()

            # Return a confirmation page with last 4 digits
            return render(request, 'concert/paymentsuccess.html', {
                'last_4_digits': card_number[-4:]
            })

        except ValueError:
            return HttpResponse("Invalid date format.", status=400)

    # Render the payment form template if not a POST request
    return render(request, 'concert/payment.html')

from django.shortcuts import render
from .models import Event
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Event

def create_event(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST['name']
        location = request.POST['location']
        date = request.POST['date']

        # Save the event to the database
        new_event = Event(name=name, location=location, date=date)
        new_event.save()

        # Render the success page with a message
        return render(request, 'concert/successevent.html', {'message': 'Event Created Successfully!'})

    return render(request, 'concert/create_event.html')


def event_list(request):
    # Retrieve all events from the database
    events = Event.objects.all()

    return render(request, 'concert/event_list.html', {'events': events})



def search_events(request):
    # Default filter values
    location = request.GET.get('location', '')
    date = request.GET.get('date', '')
    num_people = request.GET.get('num_people', '')

    # Filter events based on query parameters
    events = Event.objects.all()

    if location:
        events = events.filter(location__icontains=location)
    
    if date:
        try:
            # Parse the date if provided in 'YYYY-MM-DD' format
            event_date = datetime.strptime(date, '%Y-%m-%d').date()
            events = events.filter(date=event_date)
        except ValueError:
            # If the date format is invalid, return all events
            events = events.all()

    if num_people:
        try:
            num_people = int(num_people)
            events = events.filter(available_tickets__gte=num_people)
        except ValueError:
            events = events.all()

    return render(request, 'concert/search_result.html', {'events': events})




from django.shortcuts import get_object_or_404, render

def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'book_ticket.html', {'event': event})

