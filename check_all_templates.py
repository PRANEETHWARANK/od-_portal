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

def check_all_templates():
    template_dir = os.path.join(os.getcwd(), 'templates')
    all_ok = True
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html'):
                # Get relative path from templates dir
                rel_path = os.path.relpath(os.path.join(root, file), template_dir)
                # Normalize path for Django (forward slashes)
                rel_path = rel_path.replace(os.sep, '/')
                try:
                    get_template(rel_path)
                    print(f"OK: {rel_path}")
                except Exception as e:
                    print(f"ERROR: {rel_path} - {e}")
                    # import traceback
                    # traceback.print_exc()
                    all_ok = False
    return all_ok

if __name__ == "__main__":
    if check_all_templates():
        exit(0)
    else:
        exit(1)
