from django.core.exceptions import ValidationError
from .models import Rental_Item, Reservation

def get_reservations(item_id):
    rez_list = Reservation.objects.filter(item_id=item_id)
    bookings = []
    for booking in rez_list:
        bookings.append(f"""
        {booking.start_date} 
        thru 
        {booking.end_date}
        """)
    return bookings


def validate_date_range(item_id, start_date, end_date):
    rez_list = Reservation.objects.filter(item_id=item_id)
    for booking in rez_list:
        if end_date >= booking.start_date:
            if start_date <= booking.end_date:
                return False
    return True