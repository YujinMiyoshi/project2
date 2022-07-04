from django.db.models.deletion import CASCADE
from django.db import models
from matplotlib.pyplot import title

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pic = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

# Create your models here.
