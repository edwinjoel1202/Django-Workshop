from django.contrib import admin
from django.urls import path
from myapp.views import create, display, edit, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create, name='create'),
    path('display/', display, name='display'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
