from django.contrib import admin
from .models import Holes

# Register your models here.
# admin.site.register(Holes)
from django.utils import timezone
from django.contrib import admin
from .models import Holes

@admin.register(Holes)
class HolesAdmin(admin.ModelAdmin):
    list_display = ('HoleId', 'Latitude', 'Longitude', 'Modified')

    def get_modified_local(self, obj):
        # Convert the UTC timestamp to local time (Asia/Bangkok)
        return timezone.localtime(obj.Modified)
    
    get_modified_local.admin_order_field = 'Modified'  # Allows sorting by this field
    get_modified_local.short_description = 'Modified (Local Time)'  # Label in the admin interface
