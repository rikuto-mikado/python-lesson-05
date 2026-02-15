# Python Lesson 05 - Django Restaurant Menu App

A restaurant menu web app built with Django.

## What I Learned

### 1. Django Models (`models.py`)

- Defining database schema with Django ORM
- Field types: `CharField`, `DecimalField`, `IntegerField`, `DateTimeField`
- Using `choices` tuple for predefined options (meal type, status)
- `ForeignKey` with `on_delete` options (`PROTECT`, `CASCADE`, `SET_NULL`, etc.)
- Auto-timestamps: `auto_now_add=True` (created) vs `auto_now=True` (updated)

```python
author = models.ForeignKey(User, on_delete=models.PROTECT)
date_created = models.DateTimeField(auto_now_add=True)
date_updated = models.DateTimeField(auto_now=True)
```

### 2. Class-Based Views (`views.py`)

- `ListView` for listing objects, `DetailView` for single object display
- Overriding `get_context_data(**kwargs)` to pass extra variables to templates
- QuerySet ordering with `order_by("-date_created")`

```python
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context
```

### 3. URL Routing (`urls.py`)

- `as_view()` converts a class-based view into a callable for the URL resolver
- `include()` delegates app-level URL routing from the project `urls.py`

```python
path("", views.MenuList.as_view(), name="home")
```

### 4. Django Admin (`admin.py`)

| Option          | Purpose                          |
| --------------- | -------------------------------- |
| `list_display`  | Columns shown in admin list view |
| `list_filter`   | Sidebar filter options           |
| `search_fields` | Enable search on specific fields |

### 5. Django Templates (`index.html`, `menu_item_detail.html`, `base.html`)

- Template inheritance: `{% extends "base.html" %}` and `{% block content %}` to reuse a shared layout
- Template tags: `{% for %}`, `{% if %}`, `{{ variable }}`
- Accessing tuple elements: `meal.0` (key), `meal.1` (label)
- Conditional rendering based on item status (strikethrough `<del>` for unavailable items)
- `{% url 'name' arg %}` for reverse URL lookup (reference URLs by name instead of hardcoding)
- Bootstrap components: navbar, list-group, badge (`rounded-pill`)
- `d-flex justify-content-between align-items-center` to align elements side by side

### 6. URL Routing with Parameters (`urls.py`)

- `<int:pk>` captures a primary key from the URL and passes it to `DetailView`

```python
path("", views.MenuList.as_view(), name="home")
path("item/<int:pk>/", views.MenuItemDetail.as_view(), name="menu_item")
```

### 7. QR Code Generation (`qr.py`)

- Using the `qrcode` library to generate a QR code image pointing to the dev server

---

## What Was Difficult

**Q: What is the difference between `auto_now_add` and `auto_now`?**
A: `auto_now_add=True` sets the field only once at creation time. `auto_now=True` updates the field every time the object is saved.

**Q: Why do we need `as_view()` for class-based views?**
A: Django's URL resolver expects a callable function. `as_view()` converts a CBV class into a view function that handles the request/response cycle.

**Q: How does `get_context_data(**kwargs)` work?**
A: It collects the default context from the parent class via `super()`, then lets you add extra variables (like `MEAL_TYPE`) before passing the context to the template.

**Q: How does tuple-based `choices` work in models and templates?**
A: Choices are defined as `(stored_value, display_label)` tuples. In the database, `stored_value` is saved. In templates, `.0` accesses the stored value and `.1` accesses the display label.

**Q: What does `on_delete=models.PROTECT` mean?**
A: It prevents deleting a `User` if any `Item` references them. Other options: `CASCADE` (delete related items too), `SET_NULL` (set FK to null), `DO_NOTHING`.

**Q: Layout breaks when an HTML tag is prematurely closed**
A: Writing `<li class="..."></li>` (closing immediately) causes child elements (like badges) to fall outside the parent's Flexbox layout, breaking the design. Always verify that opening and closing tags are properly paired.

---

## Memo

### Key Django Methods & Classes

| Method / Class | Purpose |
| --- | --- |
| `generic.ListView` | View for listing model objects. Set `queryset` and `template_name` |
| `generic.DetailView` | View for a single object. Set `model` and `template_name` |
| `get_context_data(**kwargs)` | Override to add extra variables to the template context |
| `super().get_context_data(**kwargs)` | Get the default context from the parent class before adding to it |
| `objects.order_by("-field")` | Order a QuerySet. `-` prefix means descending |
| `models.ForeignKey(Model, on_delete=...)` | Foreign key relation. `on_delete` is required |
| `admin.site.register(Model, AdminClass)` | Register a model with a custom admin configuration |

### Template Syntax Cheat Sheet

```html
{% extends "base.html" %}            {# Template inheritance #}
{% block content %}...{% endblock %}  {# Block definition #}
{% for item in list %}...{% endfor %} {# Loop #}
{% if condition %}...{% endif %}      {# Conditional #}
{{ variable }}                        {# Variable output #}
{{ tuple.0 }}                         {# Tuple index access #}
{% url 'name' arg %}                  {# Reverse URL lookup #}
```

### Django Project Structure

```
mysite/           ... Project settings (settings.py, urls.py)
restaurant_menu/  ... App (models.py, views.py, urls.py, admin.py)
templates/        ... HTML templates (base.html, index.html, menu_item_detail.html)
```

### Common Commands

```bash
python manage.py runserver          # Start dev server
python manage.py makemigrations     # Create migration files
python manage.py migrate            # Apply migrations
python manage.py createsuperuser    # Create admin user
```
