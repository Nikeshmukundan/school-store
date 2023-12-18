
from django.urls import path

from . import views
app_name='demo_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
    path('logout/',views.logout,name='logout'),
]