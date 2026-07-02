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
            'accounts',
        ],
        BASE_DIR=os.getcwd(),
        STATIC_URL='/static/',
    )
    django.setup()

# Test specific templates
templates_to_check = [
    'od/od_history.html',
    'od/od_staff_history.html',
]

print("Checking specific templates...")
for template_name in templates_to_check:
    try:
        get_template(template_name)
        print(f"✓ OK: {template_name}")
    except Exception as e:
        print(f"✗ ERROR: {template_name}")
        print(f"  {str(e)}")
        import traceback
        traceback.print_exc()
