from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.db import models
# from uuid import uuid4
# from time import strftime
# import os

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class AppUser(User):
    """
        Create a new user of the application.
    """

    # def get_upload_path(instance, filename):
    #     fname, dot, extension = filename.rpartition('.')
    #     new_name = '%s.%s' % (str(uuid4().hex), extension)
    #     return os.path.join("images", "avatars", "%s/%s/%s" % (strftime("%Y"), strftime("%m"), strftime("%d")), new_name

    # avatar = models.ImageField("Display Picture", upload_to=get_upload_path, null=True, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    gender= models.CharField(max_length = 10, blank=True, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.username