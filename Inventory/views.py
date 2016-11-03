from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Item

from django import forms


def index(request):
    test = ''
    all_items = Item.objects.all()
    if request.method == 'POST':
        action = request.POST.get('AddRemove')
        if 'additem' in request.POST:
            return HttpResponseRedirect('/Inventory/additem')
        else:
            for item in all_items:
                if 'removeitem/' + str(item.id) in request.POST:
                    return HttpResponseRedirect('/Inventory/' + str(item.id) + '/removeitem')

    return render(request, "Inventory/index.html", {'all_items': all_items})


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

                return HttpResponseRedirect('/Inventory/' + str(item_id))

    return render(request, "Inventory/detail.html", {'item': item})


def additem(request):
    newitem = Item()
    newitem.item_name = 'New Item'
    newitem.save()
    return HttpResponseRedirect('/Inventory/')


def removeitem(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/Inventory/')



