from django.shortcuts import redirect, render
from app.models.reservation import Reservation
from app.forms import ReservationForm

def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_status')
    else:
        form = ReservationForm()
    return render(request, 'reservation/create.html', {'form': form})

def manage_reservations(request):
    reservations = Reservation.objects.filter(is_taken=False)
    return render(request, 'reservation/manage.html', {'reservations': reservations})

def update_reservation_status(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.is_taken = True
    reservation.save()
    return redirect('manage_reservations')

def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('manage_reservations')
