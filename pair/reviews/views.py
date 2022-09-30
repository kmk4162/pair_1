from django.shortcuts import render,redirect
from .models import Review 

# Create your views here.
def index(request):
  reviews = Review.objects.all()
  context = {
    'reviews' : reviews,
  }
  return render(request,'reviews/index.html',context)
def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  
  Review.objects.create(
    title=title,
    content=content,
  )
  return redirect('reviews:index')
def new(request):
  return render(request,'reviews/new.html')