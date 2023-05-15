from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_type', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

