from django.contrib import admin
from .models import Collab, CollabSub, Voting, Vote, PackDownloads

admin.site.register(Collab)
admin.site.register(CollabSub)
admin.site.register(Voting)
admin.site.register(Vote)
admin.site.register(PackDownloads)