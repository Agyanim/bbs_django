from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    