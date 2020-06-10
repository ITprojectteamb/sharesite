from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sharesite/post_list.html', {'posts': posts})


def give_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sharesite/give_list.html', {'posts': posts})

def want_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sharesite/want_list.html', {'posts': posts})



def give_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('give_new', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'sharesite/give_new.html', {'form': form})

def want_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('want_new', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'sharesite/want_new.html', {'form': form})

def profile_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('profile_new', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'sharesite/profile_new.html', {'form': form})

def give_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('give_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sharesite/give_edit.html', {'form': form})

def want_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('want_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sharesite/want_edit.html', {'form': form})

def want_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'sharesite/want_detail.html', {'post': post})

def give_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'sharesite/give_detail.html', {'post': post})