from django.contrib import admin
from .models import SnsappPost, FollowUser, Like

class SnsappPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')

    list_display_links = ('id', 'comment')

admin.site.register(SnsappPost, SnsappPostAdmin)

# class FollowUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'followee', '')

#     list_display_links = ('id', 'followee')

# admin.site.register(FollowUser, FollowUserAdmin)

# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username')

#     list_display_links = ('id', 'username')

# admin.site.register(Like, LikeAdmin)