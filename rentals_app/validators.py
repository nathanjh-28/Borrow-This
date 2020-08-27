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

def validate_dates(start_date, end_date):
    if start_date > end_date:
        return False
    return True

def validate_date_range_update(rez_id, item_id, start_date, end_date):
    rez_list = Reservation.objects.filter(item_id=item_id).exclude(id=rez_id)
    for booking in rez_list:
        if end_date >= booking.start_date:
            if start_date <= booking.end_date:
                return False
    return True

def validate_min_rental(length, start, end):
    rental_period = end-start
    rental_period = rental_period.days
    if rental_period >= length:
        return True
    else:
        return False
