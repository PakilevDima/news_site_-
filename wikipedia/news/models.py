from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=40)
    def __str__(self):
        return self.category


class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    name_author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    image = models.ImageField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    content_text = models.TextField()
    date = models.DateTimeField(u'Дата и время', default=timezone.now)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name_author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=150)



    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')