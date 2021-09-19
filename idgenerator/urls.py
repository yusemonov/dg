from django.urls import path
from .views import DocListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', DocListView.as_view()),
]
