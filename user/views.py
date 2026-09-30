# user
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from cafe import forms
from user import forms
# from cafe.forms import PostingForm
from user.forms import LoginForm
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
# 登入
def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_pass = request.POST['password']
            user = authenticate(username=login_name, password=login_pass)
            if user != None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/listing/')
    else:
        login_form = forms.LoginForm()
    return render(request, "login.html", locals())

# 登出
@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# 註冊
def signup(request):
    return render(request, "signup.html", locals())

# 貼文
@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        user = auth.models.User.objects.get(username=username)
        cafe_post = models.Posting(user=user)
        cafe_post_form = forms.PostingForm(request.POST, request.FILES, instance=cafe_post)
        if cafe_post_form.is_valid():
                cafe_post_form.save()
                return HttpResponseRedirect('/mypost/')
    else:
        cafe_post_form = forms.PostingForm()
    return render(request, 'posting.html', locals())

# 我的貼文
@login_required(login_url='/login/')
def mypost(request):
    if request.user.is_authenticated:
        username = request.user.username
    try:
        user = request.user
        my_posts = models.Posting.objects.filter(user=user)
    except:
        pass
    if request.method == 'POST':
        delete_id = request.POST.get('delete_post')
        if delete_id:
            user = request.user
            delete_posting = models.Posting.objects.get(id=delete_id)
            delete_posting.delete()
    else:
        None
    return render(request, 'my_post.html', locals())

# 修改
@login_required(login_url='/login/')
def revise(request, id=1):
    if request.user.is_authenticated:
        username = request.user.username
        revise_post = models.Posting.objects.get(id=id)
        revise_form = forms.PostingForm(request.POST, request.FILES, instance=revise_post)
    if request.method == 'POST':
        user = auth.models.User.objects.get(username=username)
        revise_form = forms.PostingForm(request.POST, request.FILES, instance=revise_post)
        if revise_form.is_valid():
            if not request.FILES.get('picture'):
                revise_form.picture = revise_form.cleaned_data['picture']
                revise_form.save()
                return HttpResponseRedirect('/mypost/')
            else:
                revise_form.save()
                return HttpResponseRedirect('/mypost/')
    else:
        revise_form = forms.PostingForm(instance=revise_post)
    return render(request, 'revise.html', locals())

# 典藏
@login_required(login_url='/login/')
def favorite(request):
    if request.user.is_authenticated:
        username = request.user.username
    user = request.user
    fav_posts = models.Favorite.objects.filter(user = user)
    if request.method == 'POST':
        not_favor_id = request.POST.get('not_favorite')
        if not_favor_id:
            user = request.user
            not_fav_posting = models.Posting.objects.get(id=not_favor_id)
            try:
                not_fav_exist = models.Favorite.objects.get(user=user, posting=not_fav_posting)
                if not_fav_exist:
                    not_fav_exist.delete()
            except:
                pass
    return render(request, 'favorite.html', locals())
