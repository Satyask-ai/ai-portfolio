from django.contrib import admin
from django.urls import path
from core.views import home  # Import the view we just made

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This points the homepage to your resume
]