from django.urls import path
from resume import views

app_name = 'resume'

urlpatterns = [
    path('',views.ResumeView.as_view(),name='resume')
]
