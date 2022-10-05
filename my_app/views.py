from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_page(request):
    posts = models.CreatePost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'my_app/home_page.html', context)


def signup_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form_user_name = form.cleaned_data.get('user_name')
            form_first_name = form.cleaned_data.get('first_name')
            form_last_name = form.cleaned_data.get('last_name')
            form_email = form.cleaned_data.get('email')
            form_password1 = form.cleaned_data.get('password1')
            form_password2 = form.cleaned_data.get('password2')
            hashed_password = make_password(form_password1, salt=None, hasher='default')
            if form_password1 == form_password2:
                User.objects.create(username=form_user_name, first_name=form_first_name, last_name=form_last_name, email=form_email, password=hashed_password)
            #     form.save()

            messages.success(request, f'{form_user_name} Saved')
            # redirect to a new URL:
            return redirect('login_page')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.SignUpForm()

    return render(request, 'my_app/signup_page.html', {'form': form})


@login_required
def create_post_page(request):
    print(request.method)
    user = request.user
    if request.method == 'POST':
        form = forms.CreatePostForm(request.POST)
        if form.is_valid(): #### returns a bool
            form_caption = form.cleaned_data.get('caption')
            form_body = form.cleaned_data.get('body')
            form_picture = form.cleaned_data.get('picture')
            models.CreatePost.objects.create(caption=form_caption, body=form_body, owner=user, picture=form_picture)
            return redirect('home_page')
    else:
        form = forms.CreatePostForm()
    context = {
        'form': form
    }

    return render(request, 'my_app/create_post_page.html', context)


    # FIXME
def search_page(request):
    query_dict = request.GET
    print(query_dict)
    query = query_dict.get('p')
    print(type(query))

    try:
        query = str(query)
    except:
        print('can\'t work')
        query = None

    print(type(query))
    return render(request, 'my_app/search_page.html')


def profile_page(request):
    user = request.user
    user_info = models.User.objects.filter(id=user).first()
    context = {
        'user_info': user_info
    }
    return render(request, 'my_app/profile_page.html', context) 