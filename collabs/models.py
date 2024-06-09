from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint



class Collab(models.Model):
    title = models.TextField(max_length=30)
    title_en = models.TextField(max_length=30, null=True, blank=True)
    desc = models.TextField(max_length=300, null=True, blank=True)
    desc_en = models.TextField(max_length=300, null=True, blank=True)
    desc2 = models.TextField(max_length=300, null=True, blank=True)
    desc2_en = models.TextField(max_length=300, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(null= True, blank= True)
    pic = models.FileField(upload_to="collabs/demos", null=True)

    # the pack
    download_pack = models.FileField(upload_to='collabs/downloads', null=True, blank=True)
    backing_track = models.FileField(upload_to='collabs/demos', null=True, blank=True)
    demo = models.BooleanField(default=False)
    score = models.BooleanField(default=False)
    midi = models.BooleanField(default=False)
    ableton = models.BooleanField(default=False)
    reaper = models.BooleanField(default=False)
    logic = models.BooleanField(default=False)

    
    
    wokal = models.BooleanField(default=False)
    instrument = models.BooleanField(default=False)
    rap = models.BooleanField(default=False)
    votingActive = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.title} - {self.date.date()} - id: {self.id}'
    
    
class PackDownloads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            UniqueConstraint(
                'user',
                'collab',
                name='pack-download',
            )
        ]
    

class CollabSub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE, related_name='responses')
    title = models.TextField(max_length=40, null=True)
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='collabs/responses', null=True)
    approved = models.BooleanField(default=False)
    demoCreated = models.BooleanField(default=False, blank=True, null=True)
    demo_file_url = models.CharField(max_length=200, null=True, blank=True)
    checked = models.BooleanField(default=False, null=True, blank=True) #if che
    volumeOffset = models.FloatField(null=True, blank=True)
    modComment = models.TextField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.title} - Approved: {self.approved} - Vol: {self.volumeOffset}"
    
    
    def vote_count(self):
        return Vote.objects.filter(vote_on=self).count()
    
   


class Voting(models.Model):
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True)
    name_en = models.CharField(max_length=40, blank=True)
    active = models.BooleanField(default= True)
    description = models.TextField(max_length=150, blank=True)
    description_en = models.TextField(max_length=150, blank=True)
    tags = models.CharField(max_length=50, blank=True)
    
    def tagList(self):
        return self.tags.split(',')
    
    def __str__(self):
        return f'Glosowanie - {self.collab.title}'
    
    def save(self, *args, **kwargs):
        if not self.name.endswith(f"-{self.collab.title}"):
            self.name = f"{self.name}-{self.collab.title}"
        super(Voting, self).save(*args, **kwargs)

class Vote(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    vote_on = models.ForeignKey(CollabSub, on_delete=models.CASCADE)
    voter_ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.voter_ip == None:
            return f'{self.voting.name} - glos na - {self.vote_on.title} - {self.vote_on.user}'
        else:
            return f'{self.voting.name} - glos na - {self.vote_on.title} - {self.vote_on.user} - {self.voter_ip}'
