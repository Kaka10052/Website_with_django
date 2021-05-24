from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('HORROR', 'Horror'),
        ('FANTASY', 'Fantasy, sci-fi'),
        ('NONFICTION', 'Non-fiction'),
        ('FICTION', 'Fiction'),
        ('CRIME', 'Crime story, thriller'),
        # ('', '')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank = True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_read = models.BooleanField(default=False)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='None'
    )
    cover = models.ImageField(default='books/default_cover.jpg', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={"id": self.id})
