# models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
import os
from django.core.exceptions import ValidationError
from datetime import timedelta

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('announcement-detail',kwargs={'pk':self.pk})

    def is_expired(self):
        """Check if announcement is older than 14 days"""
        return timezone.now() - self.date_posted > timedelta(days=14)

    def clean(self):
        # Check daily post limit
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_posts = Announcement.objects.filter(
            author=self.author,
            date_posted__gte=today_start
        ).count()

        if today_posts >= 4 and not self.pk:
            raise ValidationError("You can only create 4 announcements per day.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Hey there I am using campus connect!')
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        # First save to get the model instance
        super().save(*args, **kwargs)

        # Only process if image exists
        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)
            # Resize if needed
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)