from django.contrib import admin
from .models import UserAccount

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email')
    list_display_links = ('user_id',)
    search_fields = ('user_id', 'email')
    list_per_page = 25

admin.site.register(UserAccount, UserAccountAdmin)