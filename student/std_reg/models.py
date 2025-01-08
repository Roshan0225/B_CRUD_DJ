from django.db import models

# Create your models here.

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    std_name = models.CharField(max_length=255, null=True)
    std_pass = models.CharField(max_length=12, null=False)
    std_email = models.CharField(max_length=35, null=True, unique=True)
    std_joindt = models.DateField(null=False)
    std_img = models.ImageField(upload_to="profile/")

    def __str__(self):
        return self.std_email
