from django.db import models

class Note(models.Model):
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True) #auto_now takes a timestamp for each time saved
    created = models.DateTimeField(auto_now_add=True) #auto_now_add only takes a timestamp from intial creation

    def __str__(self):
        #only grabs first 60 characters to display
        return self.body[0:60]
