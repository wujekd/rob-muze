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

    
    def __str__(self):
        return f'{self.title} - {self.date.date()} - id: {self.id}' 
    

class Stages(models.Model):
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=75)
    name_pl = models.CharField(max_length=35, blank=True)
    desc = models.TextField(max_length=200)
    desc_pl = models.TextField(max_length=200, blank=True)
    open = models.BooleanField(default=False, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    duration = models.IntegerField(null= True, blank= True)
    tags = models.CharField(max_length=50, blank=True)
    
    winner = models.ForeignKey('CollabSub', on_delete=models.SET_NULL, null=True, blank=True)
    
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
    
    def tagList(self):
        return self.tags.split(',')
    
    def __str__(self):
        return f'Stage: {self.name}, of: {self.collab.title}'
    
    def save(self, *args, **kwargs):
        if not self.name.endswith(f"-{self.collab.title}"):
            self.name = f"{self.name}-{self.collab.title}"
        super(Stages, self).save(*args, **kwargs)
        
    
class CollabSub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stages, on_delete=models.CASCADE, related_name='responses', null=True, blank=True)
    title = models.TextField(max_length=40, null=True)
    msg = models.TextField(max_length=300, blank=True)
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
    
    
        

class PackDownloads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stages, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            UniqueConstraint(
                'user',
                'stage',
                name='pack-download',
            )
        ]





class Vote(models.Model):
    stage = models.ForeignKey(Stages, on_delete=models.CASCADE, blank=True, null=True)
    vote_on = models.ForeignKey(CollabSub, on_delete=models.CASCADE)
    voter_ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.voter_ip == None:
            return f'{self.stage.name} - glos na - {self.vote_on.title} - {self.vote_on.user}'
        else:
            return f'{self.stage.name} - glos na - {self.vote_on.title} - {self.vote_on.user} - {self.voter_ip}'