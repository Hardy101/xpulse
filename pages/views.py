from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html') 

def posts(request):
    return render(request, 'pages/posts.html') 

def messages(request):
    return render(request, 'pages/messages.html') 

def analytics(request):
    return render(request, 'pages/analytics.html') 

def notifications(request):
    return render(request, 'pages/notifications.html') 
