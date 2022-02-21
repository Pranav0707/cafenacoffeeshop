from django.shortcuts import render

from coffee.models import CoffeeReview

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        print(name,email,number,message)
        review=CoffeeReview(name=name,email=email,number=number,message=message)
        review.save()
    return render(request,'coffee/index.html')