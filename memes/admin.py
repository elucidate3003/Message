from django.contrib import admin
from .models import Home,Message

# Register your models here.
class MessageInline(admin.StackedInline):
    model = Message    
    extra = 1

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ["caption",]
    list_display_links = ["caption",]
    search_fields = ['id', 'caption']
    inlines = [MessageInline]

@admin.register(Message)

class MessageAdmin(admin.ModelAdmin):
    list_display = ["post","user","message"]
    autocomplete_fields = ['post',]




