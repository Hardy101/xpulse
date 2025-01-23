from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'x_handle', 'date_joined', 'is_active')
    search_fields = ('email', 'x_handle')

# admin.site.register(CustomUser, CustomUserAdmin)