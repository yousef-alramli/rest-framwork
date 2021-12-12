from django.db import models
from django.contrib.auth import get_user_model


class Car(models.Model):
    name = models.CharField(max_length=77)
    specifications = models.TextField()
    time_stamp = models.DateTimeField(auto_now=True , auto_now_add= False)
    updated = models.DateTimeField(auto_now=False , auto_now_add= False)
    user = models.ForeignKey(get_user_model() , on_delete = models.CASCADE)
    post = models.BooleanField(default=False)

    def __str__(self):
        return self.name
