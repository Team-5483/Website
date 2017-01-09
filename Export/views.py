from django.shortcuts import render
from openpyxl import load_workbook
from Inventory.models import Item
from django.shortcuts import HttpResponseRedirect


# Create your views here.


def index(request):
    file_not_found = ''
    if request.method == 'POST':
        file_path = request.POST.get('file_path', None)
        if file_path is not None and file_path is not '':
            try:
                excel = export_excel(file_path)
                save(excel[0], excel[1])
                return HttpResponseRedirect('/Inventory/')
            except FileNotFoundError:
                file_not_found = 'File Not Found'

def export_excel(fileName):
    wb = load_workbook(fileName)
    ws = wb.active
    items = []
    #turn items into cellssssssss bbyyyy
    return items, ws

    return render(request, "ExcelParser/index.html", {'file_not_found' : file_not_found})

