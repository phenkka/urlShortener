from django.db import models
from django.utils import timezone
import string, random

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    click_count = models.PositiveIntegerField(default=0)

    def is_expired(self):
        return timezone.now() > self.expires_at
