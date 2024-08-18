from django.urls import path
from rest_framework import routers

from .api import FilmWorkViewSet

# from movies.api.v1 import views

# urlpatterns = [
#     path('movies/', views.api),
# ]
router = routers.DefaultRouter()
router.register(r'filmwork', FilmWorkViewSet)
urlpatterns = router.urls