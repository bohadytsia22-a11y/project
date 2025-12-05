from django.contrib import admin
from django.urls import path, include
from currency.views import converter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', converter),
    path('', include('currency.urls')),
]