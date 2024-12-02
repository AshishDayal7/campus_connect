from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
        return self.title
    
# User model
class User(models.Model):
    
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username

# News model
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# Placements model
class Placement(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.name} - {self.company}"

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.sport.name}"

class Result(models.Model):
    fixture = models.OneToOneField(Fixture, on_delete=models.CASCADE)
    winner = models.CharField(max_length=100)
    score = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fixture} - Winner: {self.winner}"
    



