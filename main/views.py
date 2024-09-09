from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Adam Caldipawell Sembiring',
        'class' : 'PBP F'
    }
    return render(request, "main.html", context)
