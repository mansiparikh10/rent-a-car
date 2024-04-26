from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import YD_Car, YD_Reservation, YD_RentalAgreement, YD_RentalAssignment, YD_Model
from .forms import ReservationForm, RentalAgreementForm, RentalAssignmentForm

def customer_signin(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('car_listing')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def car_listing(request):
    models = YD_Model.objects.all()
    params = {'model':models}
    context = params
    return render(request, 'vehicles.html', context)

def customer_signout(request):
    logout(request)
    return redirect('customer_signin')

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            # Perform any additional logic if needed
            return redirect('car_listing')
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})

def make_rental_agreement(request):
    if request.method == 'POST':
        form = RentalAgreementForm(request.POST)
        if form.is_valid():
            rental_agreement = form.save()
            # Perform any additional logic if needed
            return redirect('car_listing')
    else:
        form = RentalAgreementForm()
    return render(request, 'make_rental_agreement.html', {'form': form})

def do_rental_assignment(request):
    if request.method == 'POST':
        form = RentalAssignmentForm(request.POST)
        if form.is_valid():
            rental_assignment = form.save()
            # Perform any additional logic if needed
            return redirect('car_listing')
    else:
        form = RentalAssignmentForm()
    return render(request, 'do_rental_assignment.html', {'form': form})

def about(request):
    return render(request,'about.html')