from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from trading_bot import views as bot_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bot/status/', bot_views.bot_status, name='bot_status'),
]

# Add static files serving during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
