from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser,Store,Book
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
import requests
import json

def Home(request):
    return render(request,"index.html")
def SignUp(request):
    form = CustomUserCreationForm
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_user = True
            f.save()
            print(request,"success")
            return Home(request)
    return render(request,"SignUp.html",{"form":form})


def Booksearch(request):
    return render(request,"booksearch.html")


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password = password)
        if user and user.is_user == True:
            login(request,user)
            return Booksearch(request)
        else:
            return HttpResponse('Invalid login details')
    return render(request,"login.html")

def Showbook(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            url = 'https://www.googleapis.com/books/v1/volumes?q='
            search = request.POST.get('search')
            response = requests.get(url + search)
            obj = json.loads(response.text)
            bookdata =[]
            user = request.user
            stname = Store.objects.filter(user=user)
            try:
                for i in range(len(obj['items'])):
                    x = obj['items'][i]['volumeInfo']['authors']
                    y = obj['items'][i]['volumeInfo']['title']
                    w = obj['items'][i]['volumeInfo']['imageLinks']['thumbnail']
                    i = obj['items'][i]['id']
                    book = {"author":x[0],
                            "title":y,
                            "img":w,
                            "bkid":i
                            }
                    bookdata.append(book)
            except KeyError:
                for i in range(len(obj['items'])):
                    # x = obj['items'][i]['volumeInfo']['authors']
                    y = obj['items'][i]['volumeInfo']['title']
                    w = obj['items'][i]['volumeInfo']['imageLinks']['thumbnail']
                    i = obj['items'][i]['id']
                    book = {
                        # "author":x[0],
                            "title":y,
                            "img":w,
                            "bkid":i
                            }
                    bookdata.append(book)
            finally:
                return render(request, "showbook.html", {"bookdata": bookdata, "stname": stname})
        else:
            print(request,"login show search books")
            return redirect('showbook')
    else:
        return Home(request)
def Bookstore(request):
    if request.method == "POST":
        idd = request.POST.get("id")
        name = request.POST.get("name")
        user = request.user
        store = Store.objects.filter(user=user,store_name=name)
        for i in store:
            if i.store_name == name:
                book = Book(Book_id=idd,store=i)
                book.save()
                return redirect('showbook')
            else:
                return HttpResponse("failed")
    return Home(request)
def CreateStore(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            stname = Store.objects.filter(user=user)
            name = request.POST.get("name")
            data = Store(store_name=name,user=request.user)
            data.save()
            return render(request,"createstore.html",{"stname":stname})
        user = request.user
        stname = Store.objects.filter(user=user)
        return render(request,"createstore.html",{"stname":stname})
    else:
        return Home(request)
def ShowStore(request):
    user = request.user
    if user.is_authenticated:
        if request.method=="POST":
            name = request.POST.get("stname")
            user = request.user
            store = Store.objects.filter(user=user,store_name=name)
            bookdata = []
            for i in store:
                if i.store_name == name:
                    book = Book.objects.filter(store=i)
                    bookdata=[]
                    for j in book.iterator():
                        url = 'https://www.googleapis.com/books/v1/volumes?q='
                        response = requests.get(url + j.Book_id)
                        obj = json.loads(response.text)
                        x = obj['items'][0]['volumeInfo']['authors']
                        y = obj['items'][0]['volumeInfo']['title']
                        w = obj['items'][0]['volumeInfo']['imageLinks']['thumbnail']
                        c = obj['items'][0]['id']
                        book = {"author": x[0],
                                "title": y,
                                "img": w,
                                "bkid":c,
                                "copy":j.no_copis,
                                "name" : name
                                }
                        bookdata.append(book)
                    return render(request,"showstore.html",{"data":bookdata,"name":name})
        else:
            return redirect('showstore')
    else:
        return Home(request)
def UpdateCopies(request):
    if request.method == "POST":
        copies = request.POST.get("copy")
        idd = request.POST.get("idd")
        name = request.POST.get("stname")
        user = request.user
        store = Store.objects.filter(user=user, store_name=name)
        for i in store:
            if i.store_name == name:
                book = Book.objects.get(Book_id=idd,store=i)
                book.no_copis = copies
                book.save()
    return ShowStore(request)

def DeleteBook(request):
    if request.method == "POST":
        idd = request.POST.get("dtid")
        name = request.POST.get("ssname")
        user = request.user
        store = Store.objects.filter(user=user,store_name = name)
        for i in store:
            if i.store_name == name:
                book = Book.objects.get(Book_id=idd,store =i)
                book.delete()
    return redirect('createstore')
def DeleteStore(request):
    if request.method == "POST":
        name = request.POST.get("sname")
        user = request.user
        store = Store.objects.get(user=user,store_name=name)
        store.delete()
    return redirect('createstore')

def Logout(request):
    logout(request)
    return Home(request)

# Create your views here.
