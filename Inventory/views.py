from django.shortcuts import render, get_object_or_404
from .models import Item

from django import forms

# Create your views here.
def index(request):
    all_items = Item.objects.all()

    context = {'all_items': all_items}

    return render(request, "Inventory/index.html", context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        # drop down box

        item.item_category = request.POST.get('category', None)

        # Text fields
        for name in item.item_field_names:
            request_text = request.POST.get(name, None)
            if request_text is not None and request_text is not '':
                setattr(item, name, request_text)
    item.save()

    return render(request, "Inventory/detail.html", {'item': item})

