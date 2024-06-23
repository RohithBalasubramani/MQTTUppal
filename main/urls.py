from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *  # Import all dynamically created viewsets

# Create a router instance
router = DefaultRouter()

# Register dynamically created viewsets with the router
app_models = apps.get_app_config('main').get_models()

for model in app_models:
    viewset = globals()[f"{model.__name__}ViewSet"]
    model_name = model.__name__.lower()
    router.register(model_name, viewset, basename=model_name)

# Define the URL patterns by including the router's URLs
urlpatterns = [
    path('api/', include(router.urls)),
    # other URL patterns of your project...
]
