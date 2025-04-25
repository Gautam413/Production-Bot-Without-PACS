from django.db import models

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=20, unique=True)
    FirstName = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    Password = models.CharField(max_length=255)  # Increased length for password (hashed passwords)
    Email = models.EmailField(max_length=100, null=True, blank=True)  # Added Email field

    def __str__(self):
        return f"{self.FirstName} {self.LastName} ({self.UserName})"

    def full_name(self):
        return f"{self.FirstName} {self.LastName}"
