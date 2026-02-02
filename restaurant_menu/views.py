from django.views import generic

# Import MEAL_TYPE to pass meal category choices to the template context for menu filtering/display
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    # **kwargs captures additional keyword arguments from the parent class
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
