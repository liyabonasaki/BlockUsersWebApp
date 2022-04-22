from django.db import connections
from django.db import models

class Blockedusers(models.Model):
    date = models.CharField(max_length=100)
    servername = models.CharField(max_length=100)
    domainname = models.CharField(max_length=100)
    blockedemail = models.CharField(max_length=100)

    class Meta:
        db_table ="data"

