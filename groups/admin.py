from django.contrib import admin

# Register your models here.
from .models import Group, GroupMembership
admin.site.register(Group)
admin.site.register(GroupMembership)
