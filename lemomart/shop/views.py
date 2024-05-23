from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from . models import Contact, Product, Order, OrderUpdate
import json

def index(request):
   # products = Product.objects.all()
   # params = {'no_of_slide': nSlides, 'range': range(nSlides), 'product': products}
   # allProds = [[products, range(nSlides), nSlides], [products, range(nSlides), nSlides]]

   allProds = []
   catProds = Product.objects.values('category', 'id')
   cats = {item['category'] for item in catProds}
   for cat in cats:
      prod = Product.objects.filter(category=cat)
      n = len(prod)
      nSlides = n//4 + ceil((n/4)-(n//4))
      allProds.append([prod, range(nSlides), nSlides])


   params = {'allProds':allProds}
   return render(request, 'shop/index.html', params)

def about(request):
   return render(request, "shop/about.html")

def contact(request):
   if request.method == 'POST':
      name = request.POST.get('name', '')
      email = request.POST.get('email', '')
      phone = request.POST.get('phone', '')
      city = request.POST.get('city', '')
      desc = request.POST.get('desc', '')
      # print(name, email, phone, city, desc)
      contact = Contact(name=name, email=email, phone=phone, city=city, desc=desc)
      contact.save()
   return render(request, "shop/contact.html")

def tracker(request):
   if request.method == 'POST':
      order_id = request.POST.get('order_id', '')
      email = request.POST.get('email', '')
      try:
         order = Order.objects.filter(order_id=order_id, email=email)
         if len(order)>0:
            update = OrderUpdate.objects.filter(order_id=order_id)
            updates = []
            for item in update:
               updates.append({'text': item.update_desc, 'time': item.timestamp})
               response = json.dumps([updates, order[0].items_json], default=str)
            return HttpResponse(response)
         else:
            return HttpResponse('{}')
      except Exception as e:
         return HttpResponse('{}')
   return render(request, "shop/tracker.html")

def search(request):
   return render(request, "shop/search.html")

def productView(request, myid):
   product = Product.objects.filter(id=myid)
   return render(request, "shop/porductView.html", {'product':product[0]})

def checkout(request):
   if request.method == 'POST':
      full_name = request.POST.get('full_name', '')
      items_json = request.POST.get('itemsJson', '')
      email = request.POST.get('email', '')
      address = request.POST.get('address', '')
      address2 = request.POST.get('address2', '')
      phone = request.POST.get('phone', '')
      city = request.POST.get('city', '')
      state = request.POST.get('state', '')
      pincode = request.POST.get('pincode', '')
      # print(name, email, phone, city, desc)
      order = Order(full_name=full_name, items_json=items_json, email=email, address=address, address2=address2, phone=phone, city=city, state=state, pincode=pincode)
      order.save()

      update = OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
      update.save()

      thank = True
      id = order.order_id
      return render(request, "shop/checkout.html", {'thank': thank, 'id': id})
   return render(request, "shop/checkout.html")