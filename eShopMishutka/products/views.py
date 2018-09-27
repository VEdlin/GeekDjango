from django.shortcuts import render

# Create your views here.
def uslugi(request):
    return render(request, 'uslugi.html')

def usluga_klyauza(request):
    return render(request, 'usluga_klyauza.html')

def usluga_vzyat_izmorom(request):
    return render(request, 'usluga_vzyat_izmorom.html')

def usluga_predstavlenie(request):
    return render(request, 'usluga_predstavlenie.html')

def usluga_geroi_smi(request):
    return render(request, 'usluga_geroi_smi.html')

def uslugi_samp(request):
    return render(request, 'usligi_samp.html')

def usluga_samp(request):
    return render(request, 'usluga_samp.html')