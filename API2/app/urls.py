from django.urls import path
from . views import validate_user
urlpatterns = [
  path("user/", validate_user )
]
