from django import forms
from .models import YD_Reservation, YD_RentalAgreement, YD_RentalAssignment

class ReservationForm(forms.ModelForm):
    class Meta:
        model = YD_Reservation
        fields = ['pick_up_date', 'pickup_time', 'drop_off_date', 'dropoff_time', 'location_id', 'class_id', 'customer_id', 'emp_id']

class RentalAgreementForm(forms.ModelForm):
    class Meta:
        model = YD_RentalAgreement
        fields = ['start_date', 'start_time', 'end_date', 'end_time', 'odo_read_start', 'odo_read_end', 'rental_cost', 'customer_id', 'reservation_id']

class RentalAssignmentForm(forms.ModelForm):
    class Meta:
        model = YD_RentalAssignment
        fields = ['contract_no', 'vin', 'customer_id']
