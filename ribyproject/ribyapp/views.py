from django.shortcuts import render
from django.conf import settings
from .forms import PostForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post


def home(request):
    return render(request,"home.html",{})


def create(request):
    title=""
    form=PostForm(request.POST or None)
    context={
        "title":title,
        "form":form,
    }
    if form.is_valid():
        instance=form.save(commit=False)
        name=form.cleaned_data.get("name")
        email=form.cleaned_data.get("email")
        instance.name=name
        instance.email=email
        instance.save()
        context={
            #"title":"Thank You"
        }
    return render(request,"create.html",context)

def post_list(request):
    queryset_list=Post.objects.all()#.order_by("-timestamp")
    paginator=Paginator(queryset_list,5)#shows 5 posts per list
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer, deliver first page
        queryset=paginator.page(1)
    except EmptyPage:
        #if page is out of range, deliver last page
        queryset=paginator.page(paginator.num_pages)

    context={
        "object_list":queryset,
        "title":"Registered Users of Riby.me",
        "page_request_var":page_request_var,
    }
    return render(request,"post_list.html",context)

# Create your views here.
