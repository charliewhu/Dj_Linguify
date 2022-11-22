from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = []

router = SimpleRouter()
router.register("texts", views.TextViewSet, basename="texts")
