from django.contrib import admin
#Models
from resume.models import Experience,Education

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['employment_status','status']
    list_editable = ['status']
admin.site.register(Experience,ExperienceAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['field_of_Study','status']
    list_editable = ['status']
admin.site.register(Education,EducationAdmin)

