from django.urls import path
from blog import views
urlpatterns = [
    path('',views.HomeScreenView.as_view(),name='homescreen'),
]
