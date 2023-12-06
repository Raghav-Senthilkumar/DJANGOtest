from django.urls import path
from reviews.views import AppDevClubReviewsView
from reviews.views import CreateAppDevClubReview

urlpatterns = [
    path('reviews', AppDevClubReviewsView.as_view()),
    path('add_reviews',CreateAppDevClubReview.as_view())
]
