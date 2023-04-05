from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pinCode',
                     'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
