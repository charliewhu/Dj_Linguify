from django.urls import path

from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
    # path("text_words/<int:pk>/", views.text_word, name="text_word"),
]

router = SimpleRouter()
router.register("texts", views.TextViewSet, basename="texts")
router.register("words", views.WordViewSet, basename="words")
router.register("text_words", views.TextWordViewSet, basename="text_words")

urlpatterns += router.urls
