from django.urls import path
from .views import ShortenURLView, ListURLsView, DeactivateURLView, RedirectView

urlpatterns = [
    path('api/shorten/', ShortenURLView.as_view(), name='shorten'),
    path('api/links/', ListURLsView.as_view(), name='links'),
    path('api/deactivate/<str:code>/', DeactivateURLView.as_view(), name='deactivate'),
    path('<str:code>/', RedirectView.as_view(), name='redirect'),
]