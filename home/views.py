
from django.shortcuts import render
from .forms import ImageForms
from .models import Image
# Create your views here.
def home(request):
    if request.method == "POST":
     form = ImageForms(request.POST, request.FILES)
     if form.is_valid():
      form.save()
    form =ImageForms()
    img = Image.objects.all()
    return render(request,"home.html",{'img':img,'form':form})