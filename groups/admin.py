from django.contrib import admin
from .models import Group, GroupMembership, MembershipRequest

admin.site.register(Group)
admin.site.register(GroupMembership)
admin.site.register(MembershipRequest)
