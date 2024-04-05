from calculator import views
from django.urls import path

urlpatterns = [
    path("", views.consumer_list, name="consumer"),
    path("form", views.add_consumer, name="form")
]
