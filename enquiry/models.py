from django.db import models

class Enquiry(models.Model):
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Enquiry #{self.id}: Phone - {self.phone}"
