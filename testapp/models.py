from django.db import models

# Create your models here.
class report(models.Model):
    fullname_staff = models.CharField(max_length = 50)
    username_staff = models.CharField(max_length = 50)
    complain_id = models.CharField(max_length = 50)
    engg = models.CharField(max_length = 100, default = "not given")
    total_points = models.IntegerField()
    feedbacktxt = models.TextField(max_length = 500)
    feedbackpos = models.CharField(max_length = 100, default = "0")
    feedbackneg = models.CharField(max_length = 100,default = "0")
    feedbacknul = models.CharField(max_length = 100,default = "0")
    fedbackcomp = models.CharField(max_length = 200, default = "neutral")

class enggdetails(models.Model):
    engg_username = models.CharField(max_length = 50)
    engg_fullname = models.CharField(max_length = 50)
    complainid = models.CharField(max_length = 50)
    point = models.IntegerField()
