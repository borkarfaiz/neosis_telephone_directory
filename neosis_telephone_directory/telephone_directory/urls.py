from django.urls import path

from neosis_telephone_directory.telephone_directory.views import contact_list_view1, contact_list_view2

app_name = "contacts"
urlpatterns = [
    path("", view=contact_list_view2, name="contact_list_view")
]