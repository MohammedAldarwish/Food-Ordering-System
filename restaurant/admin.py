from django.contrib import admin
from .models import Restaurant
from django.contrib import messages

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'user', 'is_approved']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

<<<<<<< HEAD
=======
        # إذا تمت الموافقة، عدّل الدور
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
        if obj.is_approved and obj.user.role != 'owner':
            obj.user.role = 'owner'
            obj.user.save()