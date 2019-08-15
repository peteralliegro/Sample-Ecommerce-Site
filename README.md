# Sample-Ecommerce-Site
A simple one page ecommerce template. Built using Django.


# Getting Started
Once the repository is cloned you will need to migrate, ```python manage.py makemigrations```, ```python manage.py migrate```. Then create an admin user in order to add products via the admin panel,```python manage.py createsuperuser```. Once created you can upload products.

# Limitations
There is no application for ordering. If you would like to use this as a template for an ecommerce site, you will need to integrate Stripe, or a similar API.
