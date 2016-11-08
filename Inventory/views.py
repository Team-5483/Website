from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Item
from django.db.models import Q
from django import forms


def index(request):
    all_items = Item.objects.all()
    if request.method == 'POST':
        if 'additem' in request.POST:
            return HttpResponseRedirect('/Inventory/additem')
        else:
            for item in all_items:
                if 'removeitem/' + str(item.id) in request.POST:
                    return HttpResponseRedirect('/Inventory/' + str(item.id) + '/removeitem')
    if request.method == 'GET':
        search_query = request.GET.get('search', None)
        if search_query != '' and search_query is not None:
            return search(request, search_query=search_query)
    return render(request, "Inventory/index.html", {'all_items': all_items})


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.item_category = request.POST.get('category', None)

        # Text fields
        for name in item.item_field_names:
            request_text = request.POST.get(name, None)
            if request_text is not None and request_text is not '':
                setattr(item, name, request_text)
                item.save()

                return HttpResponseRedirect('/Inventory/' + str(item_id))
    item.save()
    return render(request, "Inventory/detail.html", {'item': item})


def search(request, search_query):
    return render(request, "Inventory/index.html",
                  {'all_items': Item.objects.filter(Q(item_name__contains=search_query) | Q(item_category=search_query)
                                                    | Q(item_reference=search_query) | Q(item_source=search_query))})


def additem(request):
    newitem = Item()
    newitem.item_name = 'New Item'
    newitem.save()
    return HttpResponseRedirect('/Inventory/')


def removeitem(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/Inventory/')



