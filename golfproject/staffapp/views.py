from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# for login page
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# for update_hole_location page
from .models import Holes

# Create your views here.
# def staff(request):
#     template = loader.get_template('input_panel.html')
#     return HttpResponse(template.render())

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            user = authenticate(password=password)
            if user is not None:
                login(request, user)
                return redirect('update_hole_location')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def update_hole_location(request):
    if request.method == 'POST':
        hole_id = int(request.POST.get('HoleId'))
        hole = get_object_or_404(Holes, HoleId=hole_id)
        print(f'current hole: {hole}\n')
        latitude = request.POST.get('Latitude')
        longitude = request.POST.get('Longitude')
        print(f'New Latitude: {latitude}, New Longitude: {longitude}\n')

        if latitude and longitude: 
            hole.Latitude = latitude
            hole.Longitude = longitude
            hole.save()
            messages.success(request, f'Hole {hole_id} location updated successfully!')
        else:
            messages.error(request, "Cannot save lat and long, or there is not lat and long in the variable")
        return redirect('update-location')
    holes = Holes.objects.all()
    return render(request, 'update_location.html', {'holes': holes})

