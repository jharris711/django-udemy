from django.urls import path
from users.views import profiles


urlpatterns = [
  path('', profiles, name="profiles")
]