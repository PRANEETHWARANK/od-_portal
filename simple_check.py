import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amrita_od_portal.settings')

import django
django.setup()

from django.template.loader import get_template

try:
    template = get_template('od/od_staff_history.html')
    print("✓ od_staff_history.html is OK")
except Exception as e:
    print(f"✗ ERROR in od_staff_history.html:")
    print(f"  {type(e).__name__}: {str(e)}")
    import traceback
    traceback.print_exc()

try:
    template = get_template('od/od_history.html')
    print("✓ od_history.html is OK")
except Exception as e:
    print(f"✗ ERROR in od_history.html:")
    print(f"  {type(e).__name__}: {str(e)}")
    import traceback
    traceback.print_exc()
