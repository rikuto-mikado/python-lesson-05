from django.db import models

# Import Django's built-in User model for authentication and user management
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Saladas"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)

STATUS = ((0, "Unavaliable"), (1, "Avaliable"))


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    # PROTECT prevents deletion of User if they have associated Items
    # Other options: CASCADE (delete items), SET_NULL (set to null), SET_DEFAULT, DO_NOTHING
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    # Automatically set to current time when item is created
    date_created = models.DateTimeField(auto_now_add=True)
    # Automatically update to current time whenever item is modified
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
