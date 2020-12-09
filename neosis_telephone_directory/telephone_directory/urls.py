from django.urls import path

from .views import contact_list_view2, contact_create_view, contact_detail_view

app_name = "contacts"
urlpatterns = [
    path("", view=contact_list_view2, name="contact_list_view"),
    path("create", view=contact_create_view, name="contact_create_view"),
    path("<slug:pk>", view=contact_detail_view, name="contact_detail_view"),
]