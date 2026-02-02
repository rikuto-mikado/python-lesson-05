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

### 5. Django Templates (`index.html`)

- Template tags: `{% for %}`, `{% if %}`, `{{ variable }}`
- Accessing tuple elements: `meal.0` (key), `meal.1` (label)
- Conditional rendering based on item status (strikethrough for unavailable)

### 6. QR Code Generation (`qr.py`)

- Using the `qrcode` library to generate a QR code image pointing to the dev server

---

## What Was Difficult

**Q: What is the difference between `auto_now_add` and `auto_now`?**
A: `auto_now_add=True` sets the field only once at creation time. `auto_now=True` updates the field every time the object is saved.

**Q: Why do we need `as_view()` for class-based views?**
A: Django's URL resolver expects a callable function. `as_view()` converts a CBV class into a view function that handles the request/response cycle.

**Q: How does `get_context_data(**kwargs)`work?**
A: It collects the default context from the parent class via`super()`, then lets you add extra variables (like `MEAL_TYPE`) before passing the context to the template.

**Q: How does tuple-based `choices` work in models and templates?**
A: Choices are defined as `(stored_value, display_label)` tuples. In the database, `stored_value` is saved. In templates, `.0` accesses the stored value and `.1` accesses the display label.

**Q: What does `on_delete=models.PROTECT` mean?**
A: It prevents deleting a `User` if any `Item` references them. Other options: `CASCADE` (delete related items too), `SET_NULL` (set FK to null), `DO_NOTHING`.

---

## Memo
