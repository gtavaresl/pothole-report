from django.conf import settings
from django.db import models
from django.utils import timezone


class Report(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.TextField(max_length=100)
    number = models.IntegerField()
    district = models.TextField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    resolved = models.BooleanField()

    def publish(self, author):
        self.author = author
        self.address = self.street + ", " + str(self.number) + ", " + self.district
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.address