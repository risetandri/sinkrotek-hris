from django.urls import path
from .views.employee import EmployeeView

urlpatterns = [
    path("employee/", EmployeeView.as_view(), name="employee"),
    path("employee/<str:pk>", EmployeeView.as_view(), name="employee-detail"),
]
