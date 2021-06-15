from django.urls import path, include

from . import views
from information.views import listMenuCategories

urlpatterns = [
    path('makeCSV/', views.getCSV),
    path('list_menu_categories/', listMenuCategories)  
]