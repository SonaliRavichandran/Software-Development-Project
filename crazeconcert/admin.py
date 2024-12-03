from django.contrib import admin

# Register your models here.
from .models import ContactMessage,Feedback,Event,Payment  # Replace with your actual model names


admin.site.register(ContactMessage)
admin.site.register(Feedback)
admin.site.register(Event)
admin.site.register(Payment)




