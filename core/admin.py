from django.contrib import admin
from .models import UserEmail, MailMessage

admin.site.register(UserEmail)
admin.site.register(MailMessage)


# Register your models here.
