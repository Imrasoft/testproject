from __future__ import unicode_literals

from django.db import models

from temba_client.v2 import TembaClient

from django.db import models
from django.conf import settings
from temba_client.v2 import TembaClient


# Create your models here.

class Group(models.Model):
    uuid = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    count = models.IntegerField(null=False)
    query = models.CharField(max_length=50, null=True)

    @classmethod
    def add_groups(cls):
        client = TembaClient(settings.HOST, settings.KEY)
        groups = client.get_groups().all()
        added = 0
        for group in groups:
            if not cls.group_exists(group):
                cls.objects.create(uuid=group.uuid, name=group.name, query=group.query, count=group.count)
                added += 1

        return added

    @classmethod
    def group_exists(cls, group):
        return cls.objects.filter(uuid=group.uuid).exists()

    def __unicode__(self):
        return self.id

#contact_groups = Group.fetch('http://localhost:8000', '9af0741e535fe308b6f529aac764babfe19ee091')

'''
i created a new class, Group with uuid, name, count and query as parameters.

classmethod: A way to add functionaality or change the functionality of a given method or function

I created a class method (add_groups) to add groups into the model. The method is using TembaClient to import
groups from rapidpro. before it imports any groups, it checks whether the group has already
been imported into the local database. The second class method is invoked to check if the group exists or not. If not, it creaates an object with the given parameter
and increses the value of the variable "added" by 1.
'''