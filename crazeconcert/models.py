
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

# models.py

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)  # Rating field (1-5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email}) - Rating: {self.rating}"
 
# models.py
from django.db import models

class EventBooking(models.Model):
    SEATING_CHOICES = [
        ('Front Stage', 'Front Stage'),
        ('Middle', 'Middle'),
        ('Balcony', 'Balcony'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    seating = models.CharField(max_length=20, choices=SEATING_CHOICES)
    tickets = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} for {self.tickets} ticket(s)"

class Concert(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    tickets_count = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=50)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking for {self.concert.name} by {self.user.username}'
    
from django.db import models

from django.db import models

class Payment(models.Model):
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)  # Save only the last 4 digits for security
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)  # Avoid saving CVV in production!
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.card_name} on {self.timestamp}"

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)  # Store the name (e.g., event name)
    location = models.CharField(max_length=255)  # Store the location (e.g., city, venue)
    date = models.DateField()  # Store the date of the event

    def __str__(self):
        return self.name


