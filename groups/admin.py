from django.contrib import admin

# Register your models here.
from .models import Group, GroupMembership, Admins, Mods, Users

admin.site.register(Group)
admin.site.register(GroupMembership)
admin.site.register(Admins)
admin.site.register(Mods)
admin.site.register(Users)