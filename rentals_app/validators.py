from django.core.exceptions import ValidationError
from .models import Rental_Item, Reservation

# ------------------------------------------------------------------- Validate New Rez

def validate_rez(today, item_id, length, start, end):
    if start < today:
        return "You cannot make reservations for the past, please speak with admin"
    if start > end:
        return 'Your start date must be before your end date'
    rental_period = end-start
    rental_period = rental_period.days
    if rental_period < length:
        return f"You must rent this item for at least {length} days"
    rez_list = Reservation.objects.filter(item_id=item_id)
    for booking in rez_list:
        if end >= booking.start_date:
            if start <= booking.end_date:
                return 'Sorry!  Those dates overlap with a current reservation'
    return ''

# ------------------------------------------------------------------- Validate Update Rez

def validate_rez_update(rez_id,today, item_id, length, start, end):
    if start < today:
        return "You cannot make reservations for the past, please speak with admin"
    if start > end:
        return 'Your start date must be before your end date'
    rental_period = end-start
    rental_period = rental_period.days
    if rental_period < length:
        return f"You must rent this item for at least {length} days"
    rez_list = Reservation.objects.filter(item_id=item_id).exclude(id=rez_id)
    for booking in rez_list:
        if end >= booking.start_date:
            if start <= booking.end_date:
                return 'Sorry!  Those dates overlap with a current reservation'
    return ''