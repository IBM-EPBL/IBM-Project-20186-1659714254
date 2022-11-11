from django.contrib import admin

# Register your models here.


from .models import UserProfile , Addmoney_info


admin.site.register(UserProfile)
admin.site.register(Addmoney_info)
