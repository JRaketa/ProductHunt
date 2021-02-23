from django.db import models
from django.contrib.auth.models import User



class product(models.Model):
    title = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    votes_total = models.IntegerField(default = 1)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y ')
