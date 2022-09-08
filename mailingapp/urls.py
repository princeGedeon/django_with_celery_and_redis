from django.urls import path
from mailingapp.views import ReviewEmailView

urlpatterns = [
 path('',ReviewEmailView.as_view(),name="reviews")
]
