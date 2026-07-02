import os
import django
from django.template.loader import get_template
from django.conf import settings

# Configure minimal Django settings
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(os.getcwd(), 'templates')],
            'APP_DIRS': True,
        }],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.staticfiles',
            'od_app',
        ],
        BASE_DIR=os.getcwd(),
        STATIC_URL='/static/',
    )
    django.setup()

def check_template(template_name):
    try:
        get_template(template_name)
        print(f"Template '{template_name}' loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading template '{template_name}': {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    templates = ['base.html', 'accounts/login.html', 'od/od_requests.html', 'od/od_staff_history.html', 'od/od_history.html']
    all_ok = True
    for t in templates:
        if not check_template(t):
            all_ok = False
    
    if all_ok:
        exit(0)
    else:
        exit(1)
