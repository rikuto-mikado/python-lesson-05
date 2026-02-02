from django.urls import path
from . import views

# as_view() converts a class-based view into a callable view function
# that Django's URL resolver can use. It's required for all class-based views.
urlpatterns = [path("", views.MenuList.as_view(), name="home")]
