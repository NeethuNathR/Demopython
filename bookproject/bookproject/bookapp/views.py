from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksForm

# Create your views here.
def index(request):
    book=Books.objects.all()
    context={
      'book_list':book
     }
    return render(request,'index.html',context)
def detail(request,book_id):
    book=Books.objects.get(id=book_id)
    return render(request,'detail.html',{'book':book})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        price=request.POST.get('price')
        img=request.FILES['img']
        book=Books(name=name,year=year,price=price,img=img)
        book.save()
    return render(request,'add.html')
def update(request,id):
    book=Books.objects.get(id=id)
    form=BooksForm(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'book':book})

def delete(request,id):
    if request.method=='POST':
        book=Books.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')