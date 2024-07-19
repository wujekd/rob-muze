from django.contrib import admin
from .models import Group, GroupMembership, MembershipRequest, Invitation

admin.site.register(Group)
admin.site.register(GroupMembership)
admin.site.register(MembershipRequest)
admin.site.register(Invitation)
