from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=30)
    bpub_data = models.DateTimeField()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)

