from django.urls import path
from .views import PlanFormView, PlanUpdateView, DeletePlanView
app_name = "web"

urlpatterns = [
    path('plans', PlanFormView.as_view(), name='create_plan' ),
    path('plans/<pk>', PlanUpdateView.as_view(), name='update_plan' ),
    path('plans/<pk>/delete', DeletePlanView.as_view(), name='delete_plan' )
]