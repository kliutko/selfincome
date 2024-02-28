from django.urls import path

from .views import FeedbackCreateView

app_name = 'system'

urlpatterns = [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]