from django.shortcuts import render

# Create your views here.




def bus(request):

  return render(request, 'bus/bus.html')


def bus_line(request):

  return render(request, 'bus/busline.html')