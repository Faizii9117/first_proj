from django.contrib import admin
from django.urls import path, include
from api_app import views
from api_app.views import LoginAPIView, api_data_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginAPIView.as_view(), name='login_api'),  # URL to access the view
    path('api-data/', api_data_view, name='api_data'),


    
    
    ]