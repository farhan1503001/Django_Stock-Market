from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('about.html',views.about,name='about'),
   path('add_stock.html',views.add_stock,name='add_stock'),
   path('delete/<id>',views.delete,name='delete')
]