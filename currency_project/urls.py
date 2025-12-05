from django.contrib import admin
from django.urls import path, include
from currency.views import converter   # ← добавляем

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', converter),                # ← теперь главная страница
    path('', include('currency.urls')),
]