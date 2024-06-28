from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin-management/', admin.site.urls),
    path('',include('blog.urls')),
    path('resume',include('resume.urls')),
    path('admin/',include('management.urls')),
]
