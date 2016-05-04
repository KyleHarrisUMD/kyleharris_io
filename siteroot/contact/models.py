from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
    name  = models.CharField(max_length=36)
    email = models.EmailField()
    message_text = models.CharField(max_length=2000)

    def __str__(self):
        return_string = "\nName: "+self.name + '\n' + "Email:"+self.email \
                        + '\n' + "Message :" +self.message_text+"\n\n"
        return return_string

