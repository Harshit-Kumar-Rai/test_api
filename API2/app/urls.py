from django.urls import path
from . views import validate_user
urlpatterns = [
  path("user/<str:username>/<str:password>/", validate_user )
]