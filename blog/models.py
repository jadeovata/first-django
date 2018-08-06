from django.db import models
from django.utils import timezone
# Create your models here

class Story(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title
