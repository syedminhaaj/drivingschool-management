from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from management.views import StudentViewSet, InstructorViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
