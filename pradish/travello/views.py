from django.shortcuts import render
from .models import Destination,Destination2,Destination3
# Create your views here.

def index(request):
    dest1=Destination()
    dest1.name  = 'Mumbai'
    dest1.price = 1000
    dest1.desc  = 'The City In The North and The most famous city in india'
    dest1.img   = 'destination_1.jpg'
    dest2=Destination2()
    dest2.name='Chennai'
    dest2.price=5000
    dest2.desc='The Modern City and the capital of Tamil Nadu'
    dest2.img   = 'destination_2.jpg'

    dest3=Destination3()
    dest3.name='Delhi'
    dest3.price=3000
    dest3.desc='Capital city of India and the home of the president of India'
    dest3.img   = 'destination_3.jpg'
    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})