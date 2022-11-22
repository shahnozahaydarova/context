from django.urls import path
from .views import *

urlpatterns = [
    path('chartjs/',chart),
    path('car/',func1),
    path('telephone/',func2),
    path('flower/',func3),
    path('komputer/',func4),
    path('tvset/',func5)
]
