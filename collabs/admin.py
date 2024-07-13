from django.contrib import admin
from .models import Collab, CollabSub, Stages, Vote, PackDownloads

admin.site.register(Collab)
admin.site.register(CollabSub)
admin.site.register(Stages)
admin.site.register(Vote)
admin.site.register(PackDownloads)