from django.shortcuts import render

from .models import Purchase, PurchaseCategory

def home(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        amount = float(request.POST.get('amount'))
        category = PurchaseCategory.objects.get(id=category_id)
        purchase = Purchase.objects.create(category=category, amount=amount)
        carbon_footprint = purchase.carbon_footprint()
        return render(request, 'tracker/result.html', {'carbon_footprint': carbon_footprint})

    categories = PurchaseCategory.objects.all()
    return render(request, 'tracker/home.html', {'categories': categories})

