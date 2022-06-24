from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import Post


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        # * confirming that the user owns the post and the id is equal to the post before deleting
        # todo: get the post,
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

        
    return render(request, 'mainapp/home.html', {"posts" : posts})


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # ===> user that is logged in
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()


    return render(request, 'mainapp/create_post.html', {"form": form})
            

# ? Sign up views ?

def sign_up(request): 
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            # After creating the user
            user = form.save()
            # Login the user
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()


    return render(request, 'registration/sign_up.html', {"form": form})