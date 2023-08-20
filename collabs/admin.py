from django.contrib import admin
from .models import Collab, CollabSub, Voting, Vote

admin.site.register(Collab)
admin.site.register(CollabSub)
admin.site.register(Voting)
admin.site.register(Vote)
# Register your models here.
