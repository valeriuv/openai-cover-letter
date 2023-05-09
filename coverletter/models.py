from django.db import models
from accounts.models import CustomUser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

class Application(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    company = models.CharField(max_length=150)
    job_title = models.CharField(max_length=200)
    job_description = models.CharField(max_length=5000)
    cv = models.FileField(upload_to=user_directory_path, max_length=250)
    cover_letter = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job_title