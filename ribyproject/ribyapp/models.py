from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify




class Post(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:detail",kwargs={"id":self.id})
        #return "/posts/%s" %(self.id)

    class Meta:
        ordering=["-timestamp","-updated"]