from django.conf import settings
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_score(self):
        agg = self.reviews.aggregate(models.Avg('rating'))
        return agg['rating__avg'] or 0

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('book', 'author')

