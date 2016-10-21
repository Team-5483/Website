from django.shortcuts import render, get_object_or_404
from .models import Item


# Create your views here.
def index(request):
    all_items = Item.objects.all()
    context = {'all_items': all_items}
    return render(request, "Inventory/index.html", context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "Inventory/detail.html", {'item': item})
