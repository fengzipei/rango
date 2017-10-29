from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Profile)
admin.site.register(RepairOrder)
admin.site.register(Application)
admin.site.register(Advice)
admin.site.register(News)
