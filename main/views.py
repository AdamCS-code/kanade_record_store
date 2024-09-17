from django.shortcuts import render, redirect
from main.forms import ItemEntryForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_main(request):
    items = Item.objects.all()
    context = {
        'name' : 'Adam Caldipawell Sembiring',
        'class' : 'PBP F',
        'items' : items,
    }
    return render(request, "main.html", context)
