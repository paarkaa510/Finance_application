from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password:
            raise ValueError("Password cannot be empty.")
        if not self.email:
            raise ValueError("Email cannot be empty.")
        if not self.first_name or not self.last_name:
            raise ValueError("Name cannot be empty.")
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name

