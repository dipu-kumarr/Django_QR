import uuid
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class QRUserLink(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='qr_link')
    qr_unique_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.qr_unique_id}"
