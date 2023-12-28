from django.shortcuts import redirect, render
from pages.models import *

def home_page_view(request):
    categories = CategoryModel.objects.all().order_by('-created_at')[:8]
    products = ProductesModel.objects.all().order_by('-created_at')[:8]
    photoes = photoesModel.objects.all().order_by('-created_at')[:8]
    context = {
        "categorie": categories,
        "product": products,
        "photoes": photoes
    }
    return render(request, 'index.html', context=context)

def booking_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        booking = BookingModel(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            message=message
        )
        booking.save()
        return redirect('pages:home')
    else:
        return render(request, 'index.html')