from django.contrib import admin
from .models import*

# Register your models here.
@admin.register((RegistrationForm))
class RegistrationAdmin(admin.ModelAdmin):
    list_display=("id","first_name","last_name","phone","email","course","state")
    
    
@admin.register((ContactForm))
class ContactFormAdmin(admin.ModelAdmin):
    list_display=("name","phone","email","address","message")
    

@admin.register((MyFormData))
class MyFormDataAdmin(admin.ModelAdmin):
    list_display=("name","phone","email","course")
    
    
@admin.register((ModalForm))
class ModalFormAdmin(admin.ModelAdmin):
    list_display=("name","phone","email","course")