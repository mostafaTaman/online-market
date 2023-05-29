from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)