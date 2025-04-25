from django.db import models

class Status(models.Model):
    StatusID = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.StatusID