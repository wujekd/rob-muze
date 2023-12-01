from django.db import models
from django.contrib.auth.models import User

class Collab(models.Model):
    title = models.TextField(max_length=30)
    desc = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    download_pack = models.FileField(upload_to='collabs/downloads', null=True, blank=True)
    glosowanie = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} - {self.date.date()}'
    
class CollabSub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE)
    title = models.TextField(max_length=40, null=True)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='collabs/downloads', null=True)
    sprawdzone = models.BooleanField(default=False)
    odpowiedz = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.collab.title}"
    
class Voting(models.Model):
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    collab_name = models.TextField(max_length=30, blank=True)
    def __str__(self):
        return f'Glosowanie - {self.collab.title}'
    
    def save(self, *args, **kwargs):
        self.collab_name = self.collab.title  # Set collab name when saving
        super(Voting, self).save(*args, **kwargs)

    
class Vote(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    vote_on = models.ForeignKey(CollabSub, on_delete=models.CASCADE)
    voter_ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.voting.collab_name} - glos na - {self.vote_on.title} - {self.vote_on.user} - {self.voter_ip}'
