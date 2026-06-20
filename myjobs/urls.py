from django.contrib import admin
from django.urls import path, include
from accounts import views as acc
from companies.views import company_list
from django.conf import settings
from django.conf.urls.static import static
from .views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    
    path('companies/', include('companies.urls')),
    path('salary/', include('compensation.urls')),
    path('reviews/', include('reviews.urls')),
    path('analytics/',include('analytics.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)