from django.contrib import admin
from .models import Accounts, Tree, PlantedTree, Profile

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    search_fields = ('name',)

class TreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    search_fields = ('name',)

class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'tree', 'latitude', 'longitude',)
    search_fields = ('user__username',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about')
    search_fields = ('user',)

admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Tree, TreeAdmin)
admin.site.register(PlantedTree, PlantedTreeAdmin)
admin.site.register(Profile, ProfileAdmin)
