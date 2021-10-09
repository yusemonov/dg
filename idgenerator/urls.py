from django.urls import path
from .views import *

urlpatterns = [
    path('', DocListView.as_view()),
]
