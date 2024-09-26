from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')

def accountpage(request):
    return render(request, 'accountpage.html')

def eventspage(request):
    return render(request, 'events_page.html', {'navbar_color': 'rgba(109, 162, 166, 1)'})

def talk_to_us(request):
    return render(request, 'talk_to_us_page.html')

def posts(request):
    return render(request, 'posts_page.html', {'navbar_color': 'rgba(101, 104, 104, 1)'})

def books(request):
    return render(request, 'books_page.html', {'navbar_color': 'rgba(101, 104, 104, 1)'})

def archieve(request):
    return render(request, 'archieve_page.html',{'navbar_color': 'rgba(148, 139, 122, 1)'})


def poets(request):
    return render(request, 'poets_page.html', {'navbar_color': 'rgba(101, 104, 104, 1)'})





