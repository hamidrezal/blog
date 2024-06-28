from django.urls import path
from management import views
app_name = 'management'

urlpatterns = [
    path('',views.ManagementView.as_view(),name='admin-dashboard'),

]
