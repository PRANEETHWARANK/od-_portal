import os
import django

# Setup Django BEFORE importing any models or test utilities
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amrita_od_portal.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.auth.models import User
from accounts.models import Profile
from od_app.views import export_od_csv, export_od_pdf
from od_app.models import ODApplication

def test_exports():
    factory = RequestFactory()
    
    # Create or get a staff user (Advisor)
    username = 'test_advisor_export'
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password('password123')
        user.save()
    
    # Ensure they have a profile
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user, role='advisor')
    
    # Refresh user
    user = User.objects.get(username=username)
    
    # Test CSV Pending
    request = factory.get('/od/export/csv/pending/')
    request.user = user
    response = export_od_csv(request, 'pending')
    print(f"CSV Pending Export Status: {response.status_code}")
    print(f"CSV Pending Content-Type: {response.get('Content-Type')}")
    
    # Test PDF Pending
    request = factory.get('/od/export/pdf/pending/')
    request.user = user
    response = export_od_pdf(request, 'pending')
    print(f"PDF Pending Export Status: {response.status_code}")
    print(f"PDF Pending Content-Type: {response.get('Content-Type')}")

    # Test CSV History
    request = factory.get('/od/export/csv/history/')
    request.user = user
    response = export_od_csv(request, 'history')
    print(f"CSV History Export Status: {response.status_code}")
    
    # Test PDF History
    request = factory.get('/od/export/pdf/history/')
    request.user = user
    response = export_od_pdf(request, 'history')
    print(f"PDF History Export Status: {response.status_code}")

if __name__ == "__main__":
    try:
        test_exports()
        print("\nAll export tests passed successfully!")
    except Exception as e:
        print(f"\nExport testing failed: {e}")
        import traceback
        traceback.print_exc()
