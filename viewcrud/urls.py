from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[

    path('',views.read, name='home'),
    path('newblog/', views.create, name='newblog'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>',views.delete, name='delete'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('newport/',views.new_port,name='new_port'),
    
]