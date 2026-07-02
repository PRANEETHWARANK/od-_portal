import os
import django
import requests
from io import BytesIO
from django.utils import timezone

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amrita_od_portal.settings')
django.setup()

from django.test import RequestFactory
from od_app.views import export_od_pdf

class MockProfile:
    def __init__(self, role):
        self.role = role

class MockUser:
    def __init__(self, role):
        self.profile = MockProfile(role)
        self.username = "test_user"
        self.is_authenticated = True

def test_pdf_with_logo_mocked():
    factory = RequestFactory()
    request = factory.get('/od/export/pdf/pending/')
    request.user = MockUser('advisor')
    
    print("Testing PDF export with logo (mocked user)...")
    try:
        response = export_od_pdf(request, 'pending')
        if response.status_code == 200 and response['Content-Type'] == 'application/pdf':
            print("PDF exported successfully!")
            with open('test_logo_output.pdf', 'wb') as f:
                f.write(response.content)
            print("Saved as test_logo_output.pdf")
        else:
            print(f"Failed with status {response.status_code}")
    except Exception as e:
        print(f"Error during PDF export test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pdf_with_logo_mocked()
