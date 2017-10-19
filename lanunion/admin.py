from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Staff)
admin.site.register(RepairOrder)
admin.site.register(Applications)
admin.site.register(Advices)
admin.site.register(News)
