
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User

class Sampel(models.Model):
    title = models.CharField(max_length=200)
    mp3_file = models.FileField(upload_to='music/')  # 'music/' is the subdirectory within 'media' to store the files
    description = models.TextField()
    tags = models.CharField(max_length=100, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='music/images/', blank=True, null=True)
    artist = models.CharField(max_length=100)
    cena = models.IntegerField(
        # verbose_name='Points Required',  # Customizes the field name for display in forms and admin
        # help_text='Enter the amount of points required to make a purchase.',  # Provides a help text for the field
        default=30,  # Sets a default value for the field (change '0' to your desired default points)
        # blank=False,  # Specifies whether the field is required (True) or not (False)
        # null=False,  # Specifies whether the field can be set to None (True) or not (False)
        # validators=[models.MinValidator(0)],  # Adds a minimum value validator (change '0' to your desired minimum points)
    )
    
    
class Downloads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sampel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     unique_together = ('user', 'sample')
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('user'),
                Lower('sample').desc(),
                name='download',
            ),
        ]
