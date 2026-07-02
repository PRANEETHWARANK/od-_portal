import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amrita_od_portal.settings')
django.setup()

from od_app.models import ODApplication

def test_total_days():
    print("Testing total_days property...")
    # Create a dummy object (not saved to DB)
    app = ODApplication(from_date=date(2026, 3, 1), to_date=date(2026, 3, 3))
    print(f"From: {app.from_date}, To: {app.to_date}")
    print(f"Calculated Days: {app.total_days} (Expected: 3)")
    assert app.total_days == 3
    
    app2 = ODApplication(from_date=date(2026, 3, 1), to_date=date(2026, 3, 1))
    print(f"From: {app2.from_date}, To: {app2.to_date}")
    print(f"Calculated Days: {app2.total_days} (Expected: 1)")
    assert app2.total_days == 1
    print("total_days test passed!")

if __name__ == "__main__":
    try:
        test_total_days()
    except Exception as e:
        print(f"Verification failed: {e}")
