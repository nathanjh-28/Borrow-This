from django.core.exceptions import ValidationError
from .models import Rental_Item, Reservation

# def get_reservations(item_id):
#     rez_list = Reservation.objects.filter(item_id=item_id)
#     bookings = []
#     for booking in rez_list:
#         bookings.append(f"""
#         {booking.start_date} 
#         thru 
#         {booking.end_date}
#         """)
#     return bookings


# def validate_date_range(item_id, start_date, end_date):
#     rez_list = Reservation.objects.filter(item_id=item_id)
#     for booking in rez_list:
#         if end_date >= booking.start_date:
#             if start_date <= booking.end_date:
#                 return False
#     return True

# def validate_dates(start_date, end_date):
#     if start_date > end_date:
#         return False
#     return True

# def validate_date_range_update(rez_id, item_id, start_date, end_date):
#     rez_list = Reservation.objects.filter(item_id=item_id).exclude(id=rez_id)
#     for booking in rez_list:
#         if end_date >= booking.start_date:
#             if start_date <= booking.end_date:
#                 return False
#     return True

# def validate_min_rental(length, start, end):
#     rental_period = end-start
#     rental_period = rental_period.days
#     if rental_period >= length:
#         return True
#     else:
#         return False


# # -------------------------------------------------------------------------------

# def validate_date_range_msg(item_id, start, end):
#     rez_list = Reservation.objects.filter(item_id=item_id)
#     for booking in rez_list:
#         if end >= booking.start_date:
#             if start <= booking.end_date:
#                 return 'Sorry!  Those dates overlap with a current reservation...refactored'
#     return ''

# def validate_dates_msg(start, end):
#     if start > end_date:
#         return 'Your start date must be before your end date...refactored'
#     return ''

# def validate_min_rental_msg(length, start, end):
#     rental_period = end-start
#     rental_period = rental_period.days
#     print(f"if {rental_period} < {length} ")
#     if rental_period < length:
#         print(f"You must rent this item for at least {length} days")
#         return f"You must rent this item for at least {length} days"
#     else:
#         print('did not validate dawg')
#         return ''

# def validate_no_past_rentals_msg(today,start):
#     if start < today:
#         return "You cannot make reservations for the past, please speak with admin"
#     else:
#         return ''

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