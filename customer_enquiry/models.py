from django.db import models
import uuid
from django.db.models import Max


class Enquiry(models.Model):
    Id = models.IntegerField(default=1)
    EnquiryId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    CustomerName = models.CharField(max_length=1000, null=True, blank=True, default=None)
    PhoneNo = models.CharField(max_length=1000, null=True, blank=True, default=None)
    Email = models.CharField(max_length=1000, null=True, blank=True, default=None)
    Expiry = models.DateTimeField(null=True, blank=True, auto_now=True)
    Query = models.CharField(max_length=10000, null=True, blank=True, default=None)
    Feedback = models.CharField(max_length=10000, null=True, blank=True, default=None)
    Review = models.CharField(max_length=1000, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Enquiry.objects.all().aggregate(Max('Id'))['Id__max']
            if last_id is not None:
                self.Id = last_id + 1
        super(Enquiry, self).save(*args, **kwargs)

    # This Method Marks Model Object with a string
    def __str__(self):
        return str(self.CustomerName)
    class Meta:
        verbose_name_plural = "Enquiry"