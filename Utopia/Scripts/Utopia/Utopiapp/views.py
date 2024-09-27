from django.shortcuts import render

def HomePage(request):
    return render(request, 'HomePage.html')
def Service(request):
    return render(request,'Services.html')
def News(request):
    return render(request,'News.html')
def Tickets(request):
    return render(request,'Tickets.html')
def About(request):
    return render(request,'About.html')
def Contact(request):
    return render(request,'Contact.html')
def Entry(request):
    return render(request,'Entry.html')
