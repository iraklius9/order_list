# Order Management System

A modern order management system built with Django that allows you to track orders in process and completed orders.

## Features

- Real-time order updates
- Dark/Light mode
- Search functionality
- Order sorting
- Mobile responsive design
- Toast notifications
- Auto-refresh

## Deployment Instructions (PythonAnywhere)

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com/)

2. Once logged in:
   - Go to the Dashboard
   - Click on "Web" tab
   - Click "Add a new web app"
   - Choose "Manual Configuration"
   - Choose Python 3.9

3. Set up your virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 myenv
   pip install -r requirements.txt
   ```

4. Configure your web app:
   - Set the working directory to your project directory
   - Set the WSGI configuration file:
     ```python
     import os
     import sys

     path = '/home/yourusername/order_list'
     if path not in sys.path:
         sys.path.append(path)

     os.environ['DJANGO_SETTINGS_MODULE'] = 'order_list.settings'

     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```

5. Configure static files:
   - Add STATIC_ROOT in settings.py
   - Run `python manage.py collectstatic`

6. Configure your database:
   ```bash
   python manage.py migrate
   ```

7. Reload your web app

Your site will be available at: yourusername.pythonanywhere.com
