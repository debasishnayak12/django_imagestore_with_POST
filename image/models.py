from django.db import models


class user(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name