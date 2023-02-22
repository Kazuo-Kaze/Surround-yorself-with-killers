from django.db import models
from PIL import Image
from slugify import slugify

# Create your models here.


class UserEmail(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Email'
        ordering = ['-date']

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    first_para = models.TextField(null=True)
    second_para = models.TextField(null=True, blank=True)
    third_para = models.TextField(null=True, blank=True)
    fourth_para = models.TextField(null=True, blank=True)
    fifth_para = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField(max_length=255, allow_unicode=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(MailMessage, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Message'
        ordering = ['-date']

    def __str__(self):
        return self.title