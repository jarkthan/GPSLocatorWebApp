from django.db import models

# Create your models here.
class Holes(models.Model):
    HoleId = models.IntegerField(primary_key=True)
    Latitude = models.FloatField(blank=False)  
    Longitude = models.FloatField(blank=False) 
    Description = models.TextField(blank=True, null=False)
    Image = models.ImageField(upload_to='hole_image/', blank=True)  # Adjust upload_to path as needed
    Modified = models.DateTimeField(auto_now=True) # Timestamp of the last update

    def __str__(self):
        # return f"Hole {self.hole_number}" what is the difference?
        return f"Hole {self.HoleId} - Latitude: {self.Latitude}, Longitude: {self.Longitude}, Description: {self.Description}, Image: {self.Image}, Modified: {self.Modified}"
