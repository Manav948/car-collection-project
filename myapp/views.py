from django.shortcuts import render, redirect, get_object_or_404
from .models import Order , Car , Collections

def index(request):
    return render(request, 'index.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html',{'cars': cars})

def collection_list(request):
    if request.method == 'POST':
        selected_car_id = request.POST.get('car_id')
        if selected_car_id:
            selected_car = get_object_or_404(Car, id=selected_car_id)
            return render(request, 'collection_list.html', {'selected_car': selected_car})
    
    return redirect('car_list')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Car, Collections

def order_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        car_id = request.POST.get('car_id')

        if not car_id:  # Check if car_id is missing
            return redirect('collection_list')

        print(f"car_id received: {car_id}")  

        car = get_object_or_404(Car, id=car_id)  #  Get the car object

        #  Create or get the customer
        customer, created = Collections.objects.get_or_create(name=user_name, phone=user_email)

        #  Save the order
        Order.objects.create(customer=customer, car_name=car.name)

        return render(request, 'order_page.html', {
            'message': 'Order placed successfully',
            'selected_car': car , # Pass selected car to template
            'order' : Order.objects.last() #  Pass the las
        })

    return redirect('collection_list')

def manage_order(request):
    orders = Order.objects.all()
    return render(request, 'manage_orders.html', {'orders': orders})

def update_order(request, order_id, status):
    order = get_object_or_404(Order, id=order_id)  
    if status == 'confirmed': 
        order.status = 'confirmed' 
        order.save()
    elif status == 'cancelled': 
        order.delete()
    return redirect('manage_order')  
