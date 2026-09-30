# cafe
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models, forms
from cafe.models import Posting
from user import models
from django.contrib import messages, auth
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'index.html', locals())

# 全部列表
def listing(request):
    cafes = models.Posting.objects.filter(enabled=True)
    if request.user.is_authenticated:
        username = request.user.username
        user = request.user
        if request.method == 'POST':
            favor_id = request.POST.get('is_favorite')
            if favor_id:
                fav_posting = models.Posting.objects.get(id=favor_id)
                try:
                    fav_exist = models.Favorite.objects.get(user=user, posting=fav_posting)
                    if fav_exist:
                        fav_exist.delete()
                except:
                    fav_cafe = models.Favorite.objects.create(user=user, posting=fav_posting)
                    fav_cafe.save()
        for cafe in cafes:
            cafe.is_favorite = models.Favorite.objects.filter(user=request.user, posting=cafe).exists()
    return render(request, 'listing.html', locals())

# 單一頁面
def cafe(request, id=1):
    if request.user.is_authenticated:
        username = request.user.username
    cafe = models.Posting.objects.get(id=id)
    return render(request, 'cafe.html', locals())

# 搜尋結果
def search(request):
    search_target = None
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        try:
            search_target = request.POST['search']
        except:
            favor_id = request.POST.get('is_favorite')
            if 'search' in request.session:
                search_target = request.session['search']
                fav_posting = models.Posting.objects.get(id=favor_id)
                try:
                    user = request.user
                    if user:
                        try:
                            fav_exist = models.Favorite.objects.get(user=user, posting=fav_posting)
                            fav_exist.delete()
                        except:
                            fav_cafe = models.Favorite.objects.create(user=user, posting=fav_posting)
                            fav_cafe.save()
                except:
                    pass
        if search_target:
            request.session['search'] = search_target
            matches = models.Posting.objects.filter(enabled=True, title__icontains=search_target) | \
            models.Posting.objects.filter(enabled=True, address__icontains=search_target)
            nums = len(matches)
    else:
        return HttpResponseRedirect('/listing/')
    try:
        user = request.user
        for cafe in matches:
            cafe.is_favorite = models.Favorite.objects.filter(user=request.user, posting=cafe).exists()
    except:
        pass
    return render(request, 'search.html', locals())

# 交叉搜尋
def search_match(request):
    if request.user.is_authenticated:
        username = request.user.username
    cities = Posting.CITY
    if request.method == 'POST':
        favor_id = request.POST.get('is_favorite')
        search_form = forms.SearchForm()
        try:
            w_wifi = request.POST.get('w_wifi')
            w_limit = request.POST.get('w_limit')
            w_plugin = request.POST.get('w_plugin')
            city = request.POST.get('city')
            if city == None:
                wants_params = request.session.get('wants_params')
                if wants_params:
                    wants = Q(city=wants_params['city'], enabled=wants_params['enabled'])
                    if wants_params.get('wifi'):
                        wants &= Q(wifi=True)
                    if wants_params.get('limit'):
                        wants &= Q(limit=True)
                    if wants_params.get('plugin'):
                        wants &= Q(plugin=True)
                fav_posting = models.Posting.objects.get(id=favor_id)
                cafes = models.Posting.objects.filter(wants)
                try:
                    user = request.user
                    try:
                        fav_exist = models.Favorite.objects.get(user=user, posting=fav_posting)
                        if fav_exist:
                            fav_exist.delete()
                    except:
                        fav_cafe = models.Favorite.objects.create(user=user, posting=fav_posting)
                        fav_cafe.save()
                except:
                    pass
        except:
            pass
        if city != None:
            wants = Q(city=city, enabled=True)
            if w_wifi:
                wants &= Q(wifi=True)
            if w_limit:
                wants &= Q(limit=True)
            if w_plugin:
                wants &= Q(plugin=True)
            cafes = models.Posting.objects.filter(wants)
            nums = len(cafes)
            wants_params = {
                'city': city,
                'enabled': True,
                'wifi': w_wifi,
                'limit': w_limit,
                'plugin': w_plugin
            }
            request.session['wants_params'] = wants_params
        try:
            user = request.user
            if cafes:
                for cafe in cafes:
                    cafe.is_favorite = models.Favorite.objects.filter\
                    (user=request.user, posting=cafe).exists()
            else:
                None
        except:
            pass
    else:
        search_form = forms.SearchForm()
    return render(request, 'search_com.html', locals())
