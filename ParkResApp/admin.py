from django.contrib import admin
from ParkResApp.models import User, LotA, LotB, LotC, LotD, Messages
# Register your models here.
admin.site.register(User)
admin.site.register(LotA)
admin.site.register(LotB)
admin.site.register(LotC)
admin.site.register(LotD)
admin.site.register(Messages)
