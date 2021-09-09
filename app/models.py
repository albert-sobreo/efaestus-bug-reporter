from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bug(models.Model):
    bugCode = models.CharField(max_length=10, null=True, blank=True)
    mainFeature = models.CharField(max_length=20, null=True, blank=True)
    subFeature = models.CharField(max_length=100, null=True, blank=True)
    bugTitle = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, default='Unresolved')
    projectFolder = models.CharField(max_length=255, null=True, blank=True)
    discoveredBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='bugDiscoveredBy')
    resolvedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="bugResolvedBy")
    dateFound = models.DateField(null=True, blank=True)
    dateResolved = models.DateField(null=True, blank=True)
    duplicate = models.ForeignKey('self', related_name='bug', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bugCode