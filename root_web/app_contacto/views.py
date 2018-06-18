from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from app_contacto.models import Topic, Webpage, AccessRecord


# Create your views here.
def contacto(request):
    return render(request,"contacto.html",{})

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict ={'access_records':webpages_list}
    return render(request, "index.html", context=date_dict)

#def vista_formulario(request):
    #return render(request,"basicapp/index.html")

def form_name_view(request):
    form = forms.FormName(request.POST)

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation Success")
            print("NAME:" + form.cleaned_data['name'])
            print("EMAIL:" + form.cleaned_data['email'])
            print("TEXT:"+form.cleaned_data['text'])
    return render(request,"basicapp/form_page.html", {'form':form})
