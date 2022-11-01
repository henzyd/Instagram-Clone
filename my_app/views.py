from django.shortcuts import render, redirect
from .forms import SignUpForm, CreatePostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import CreatePost, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def home_page(request):
    posts = CreatePost.objects.all()
    #### #### NOTE this is to get all the post by 'ucana'
    # the_uset = User.objects.get(username='ucana')
    # posts = the_uset.createpost_set.all()
    ####
    context = {
        'posts': posts
    }
    return render(request, 'my_app/home_page.html', context)



def signup_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
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
                user = User.objects.create(username=form_user_name, first_name=form_first_name, last_name=form_last_name, email=form_email, password=hashed_password)
                # print(user)
                # user.save()
                Profile.objects.create(user=user)
            messages.success(request, f'{form_user_name} Saved')
            # redirect to a new URL:
            return redirect('login_page')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'my_app/signup_page.html', {'form': form})



@login_required
def create_post_page(request):
    print(request.method)
    user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid(): #### returns a bool
            form_caption = form.cleaned_data.get('caption')
            form_body = form.cleaned_data.get('body')
            form_picture = form.cleaned_data.get('picture')
            CreatePost.objects.create(caption=form_caption, body=form_body, owner=user, picture=form_picture)
            return redirect('home_page')
    else:
        form = CreatePostForm()
    context = {
        'form': form
    }

    return render(request, 'my_app/create_post_page.html', context)



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
        
    the_user_searched = []
    if query is not None:
        try:
            all_users = Profile.objects.all()
            print(all_users)
            for prof_user in all_users:
                print(prof_user)
                if prof_user.user.username == query:
                    print(prof_user)
                    the_user_searched.append(prof_user)
                else:
                    print('not a user')
            print(the_user_searched)
        except:
            print('Error')

    if len(the_user_searched) == 0:
        print('yolo')
        return render(request, 'my_app/No_Items_page.html')

    context = {
        'the_user_searched': the_user_searched
    }

    return render(request, 'my_app/search_page.html', context)



def profile_page(request, slug):
    main_user = User.objects.get(username=slug)  ##### NOTE this is the built in user in django
    user_info = Profile.objects.get(user=main_user)  ##### NOTE this is the profile class in models.py
    print(main_user.pk)
    print(user_info.user)

    context = {
        'user_info': user_info,
        'main_user': main_user,
    }
    return render(request, 'my_app/profile_page.html', context) 