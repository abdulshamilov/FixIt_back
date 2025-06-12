from django.conf import settings
from django.db import models

STATUS_CHOICES = (
    (1, 'модерация'),
    (2, 'активный сбор'),
    (3, 'сбор завершён')
)

class Collection(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ← всегда через settings
        on_delete=models.CASCADE,
        related_name='collections'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo_url = models.ImageField(upload_to='collections_photos/', blank=True, null=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50, default='active')
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='listPhoto')
    image = models.ImageField(upload_to='collections/')
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
