from django.db import models

class joints(models.Model):
    zahod = models.TextField()
    counter = models.TextField()

    def __str__(self):
        return self.zahod
    
    class Meta:
        verbose_name = 'Joint'
        verbose_name_plural = 'Joints'