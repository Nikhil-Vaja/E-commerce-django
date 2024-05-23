from django.db import models

# Create your models here.

class blogpost(models.Model):
   post_id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=600, default="")
   desc = models.CharField(max_length=2000, default="")
   heading1 = models.CharField(max_length=99, default="")
   content1 = models.CharField(max_length=600, default="")
   heading2 = models.CharField(max_length=99, default="")
   content2 = models.CharField(max_length=600, default="")
   pub_date = models.DateField()
   thumnail = models.ImageField(upload_to='blog/images', default="")

   def __str__(self):
      return self.title
