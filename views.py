from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, Login,AddNewPost,AddNewComments,ContactPage
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import AddPost,AddComment,ContactUs
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    posts = AddPost.objects.all()
    if request.method == "POST":
        form = AddNewComments(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']


            addnew = AddComment(comment=comment)
            addnew.save()
            messages.success(request, 'comment added successfully.')
            return HttpResponseRedirect('/')
    else:
        cmfrm = AddNewComments()
    return render(request,'blog/index.html',{'posts':posts,'comment':cmfrm})



def about(request):
    return render(request,'blog/about.html')

def contact(request):
    if request.method=='POST':
        form = ContactPage(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'thank you for contacting us. We will reach you soon!')
            return HttpResponseRedirect('/')
    else:
        form = ContactPage()
    return render(request,'blog/contact.html',{'form':form})






def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,"ongratulation you are.")
                form.save()
                return HttpResponseRedirect('/login/')
        else:
            form = SignUpForm()
        return render(request,'blog/signup.html',{'FORM':form})
    else:
        return HttpResponseRedirect('/dashboard/')






def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=Login(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in Successfully.')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = Login()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')





def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')



# DASHBOARD
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        uname = user.get_username()
        if user.is_superuser:
            posts = AddPost.objects.all()
            return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': uname})
        else:
            posts = AddPost.objects.all().filter(un=uname)
            return render(request,'blog/dashboard.html',{'posts':posts, 'full_name':uname})

    else:
        return HttpResponseRedirect('/login/')
# EDIT POST







def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p=AddPost.objects.get(pk=id)
            p.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def addpost(request):
    if request.user.is_authenticated:
        user=request.user
        unm=user.get_username()
        if request.method=="POST":
            form = AddNewPost(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                post = form.cleaned_data['pst']

                addnew = AddPost(title=title, pst=post,un=unm)
                addnew.save()
                messages.success(request,'Post added successfully.')
                return HttpResponseRedirect('/dashboard/')
                form = AddNewPost()
        else:
            form = AddNewPost()
        return render(request,'blog/addp.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def edit(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            p=AddPost.objects.get(pk=id)

            form = AddNewPost(request.POST,instance=p)
            if form.is_valid():
                form.save()
                messages.success(request,'post edited  successfully.')
                return HttpResponseRedirect('/dashboard/')
        else:
            p=AddPost.objects.get(pk=id)
            form = AddNewPost(instance=p)
        return render(request,'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')




def readpost(request,id):
    if request.user.is_authenticated:
        posts = AddPost.objects.get(pk=id)
        c = AddComment.objects.all()
        user = request.user

        #usernam = user.get_username()
        if request.method == "POST":
            k=AddPost.objects.get(pk=id)

            form = AddNewComments(request.POST,instance=k)
            if form.is_valid():
                comment = form.cleaned_data['comment']


                addnew = AddComment(post=k, user=user, comment=comment)
                addnew.save()

                messages.success(request, 'comment added successfully.')
                return HttpResponseRedirect('/')
        else:
            k=AddPost.objects.get(pk=id)

            form = AddNewComments(instance=k)
        return render(request, 'blog/readcomment.html', {'posts': posts, 'form': form,'comments':c})

    else:
        posts = AddPost.objects.get(pk=id)
        #return (request, 'blog/readcomment.html',{'posts':posts,'form':form,})
        return HttpResponseRedirect('/login/')

def contactusread(request):
    data = ContactUs.objects.all()
    return render(request,'blog/contactusread.html',{'form':data})