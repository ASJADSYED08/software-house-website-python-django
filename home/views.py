from django.db.models.fields import DateTimeField
from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # Context={
    #     "variable":"DJANGO PROGRAMMING"
    # }
    # return render(request,'index.html',Context)
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        contact=Contact(name=name, email=email , query=query )
        contact.save()
        messages.success(request, 'Your feedback has been sent!')
    return render(request,'contact.html')
    # return HttpResponse("contact")