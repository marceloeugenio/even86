from django.urls import path

from .views import FeedbackView

urlpatterns = [path("listar/", FeedbackView.as_view(), name="feedback_listar")]
