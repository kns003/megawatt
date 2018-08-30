from django.db import models

# Create your models here.

class SiteName(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Sites(models.Model):
    site_name = models.ForeignKey(SiteName, null=True, blank=True, on_delete=models.PROTECT)
    a_value = models.FloatField(verbose_name='A Value', default=0.0)
    b_value = models.FloatField(verbose_name='B Value', default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name.name