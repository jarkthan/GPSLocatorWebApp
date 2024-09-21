from django.urls import path
from . import views
# login_view, update_hole_location

urlpatterns = [
    # path('staff/', staff, name='staff'),
    path('login/', views.login_view, name='login'),
    path('update-location/', views.update_hole_location, name='update-location'),
]