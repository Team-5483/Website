from django.shortcuts import render, get_object_or_404
from .models import Item

from django import forms

# Create your views here.
def index(request):
    all_items = Item.objects.all()

    context = {'all_items': all_items}

    return render(request, "Inventory/index.html", context)


def detail(request, item_id):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        if search_id is not None:
            user = Item.objects.get(id=item_id)
            user.item_name = search_id
            user.save()
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "Inventory/detail.html", {'item': item})
