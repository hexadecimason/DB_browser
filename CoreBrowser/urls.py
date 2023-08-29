from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'CoreBrowser'

urlpatterns = [
		path("index", views.index, name = "index"),
		path("", views.browser_app, name = "browser_app"),
		path("search", views.search, name = "search")
		#path("search_error", views.search_error, name="error"),
] + static(settings.STATIC_URL)