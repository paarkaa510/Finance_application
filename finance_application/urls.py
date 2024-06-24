
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView  
from finance.views import home,logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),
    path('finance/', include('finance.urls')),
    path('logout/', logout_view, name='logout'),

]
