from django.contrib import admin
from .models import CustomUser, Post

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    readonly_fields = ['key']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'msg', 'timestamp']
    readonly_fields = ['key']