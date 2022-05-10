from django.urls import path
from . import views
from loanbank import settings

from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.profilescreens, name = 'create'),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)