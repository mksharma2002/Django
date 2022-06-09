

from django.shortcuts import render
from math import ceil
from django.http import HttpResponse
from . models import Product, Contact,Order, OrderUpdate
import json
from Paytm import Checksum

from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'v5jOS2q_cA#njvI&'

def index(request):
    #products= Product.objects.all()
    #n= len(products)

    #nslides= n//4 + ceil((n/4) - (n//4))
    all_products = []
    cat_product = Product.objects.values('category', 'id')
    categories = {item['category'] for item in cat_product}
    for cat in categories:
        products = Product.objects.filter(category = cat)
        n= len(products)
        nslides= n//4 + ceil((n/4) - (n//4))
        all_products.append([products ,  range(1, nslides), nslides])

    #params={'no_of_slides':nslides, 'range':range(1,nslides), 'product': products}
    #all_products = [[products, range(1, nslides), nslides], [products, range(1, nslides), nslides]]

    params = {'all_products': all_products}
    return render(request,"shop/index.html", params)

def search(request):
    query= request.GET.get('search')
    all_products = []
    cat_product = Product.objects.values('category', 'id')
    categories = {item['category'] for item in cat_product}
    for cat in categories:
        prodtemp = Product.objects.filter(category=cat)
        products=[item for item in prodtemp if searchMatch(query, item)]
        n = len(products)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(products)!= 0:
            all_products.append([products, range(1, nslides), nslides])
    params = {'all_products': all_products, "msg":""}
    if len(all_products)==0 or len(query)<2:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)
    

def searchMatch(query, item):
    if query in item.product_Name.lower() or query in item.category.lower() or query in item.product_Desc.lower():
        return True
    else:
        return False
    

def about(request):
    return render(request, "shop/about.html")





def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')
                   

def productView(request, myid):

    products = Product.objects.filter(id=myid)
    return render(request, "shop/productView.html", {'products':products[0]})

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()     
    return render(request, "shop/contact.html")



    

def checkout(request):
        if request.method=="POST":
            items_json = request.POST.get('itemsJson', '')
            amount = request.POST.get('amount', '')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            phone = request.POST.get('phone', '')
            order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone,  amount = amount)
            order.save()
            update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
            update.save()
            thank = True
            id = order.order_id
            #return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
            param_dict = {

                'MID': 'zIbLxi39328167136664',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return  render(request, 'shop/paytm.html', {'param_dict': param_dict})
    
        return render(request, 'shop/checkout.html')

# Create your views here.
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})