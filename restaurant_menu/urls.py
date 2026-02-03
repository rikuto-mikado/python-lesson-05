from django.urls import path
from . import views

# as_view() converts a class-based view into a callable view function
# that Django's URL resolver can use. It's required for all class-based views.
urlpatterns = [
    path("", views.MenuList.as_view(), name="home"),
    # URL pattern for menu item detail page, referenced in templates as {% url 'menu_item' row.id %}
    path("item/<int:pk>/", views.MenuItemDetail.as_view(), name="menu_item"),
]
