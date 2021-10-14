from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors = related name in many-to-many relationship

    def __repr__(self):
        return f"<User object: {self.title} {self.desc} ({self.id})>"

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(blank=True)    # field added subsequent to original migration and some records created; 
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<User object: {self.first_name} {self.last_name} ({self.id})>"


# Create your models here.
