from django.shortcuts import render
from django.utils import timezone
from .models import  Post,Give,Want,Profile,Item,Employee,Give_comment,Want_info,Want_comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,GiveCreateForm,WantForm,ProfileForm,GiveCommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 2

class GiveListView(LoginRequiredMixin, generic.ListView):
    model = Give
    template_name = 'give_list.html'
    paginate_by = 6
    
    def get_queryset(self):
        gives = Give.objects.order_by('-open_date')
        return gives

class WantListView(LoginRequiredMixin, generic.ListView):
    model = Want
    template_name = 'want_list.html'
    paginate_by = 3
    
    def get_queryset(self):
        wants = Want.objects.order_by('-published_date')
        return wants


class GiveCreateView(LoginRequiredMixin, generic.CreateView):
    model = Give
    template_name = 'give_new.html'
    form_class = GiveCreateForm
    success_url = reverse_lazy('give_list')

    def form_valid(self, form):
        give = form.save(commit=False)
        give.user = self.request.user
        give.save()
        messages.success(self.request, '品物を登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "品物が登録できませんできた。")
        return super().form_invalid(form)

def want_new(request):
    if request.method == "POST":
        form = WantForm(request.POST)
        if form.is_valid():
            want = form.save(commit=False)
            want.author = request.user
            want.published_date = timezone.now()
            want.save()
            return redirect('want_list')
    else:
        form = WantForm()
    return render(request, 'sharesite/want_new.html', {'form': form})

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
    want = get_object_or_404(Want, pk=pk)
    return render(request, 'sharesite/want_detail.html', {'want': want})

class GiveDetailView(LoginRequiredMixin, generic.DetailView):
    model = Give
    template_name = 'give_detail.html'

##################################################################
#ここから先追加箇所＃
##################################################################

def profile_new(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.published_date = timezone.now()
            profile.photo = request.FILES['photo']
            profile.save()
            return redirect('mypage')
    else:
        form = ProfileForm()
    return render(request, 'sharesite/profile_new.html', {'form': form})

def mypage(request):
    profiles = Profile.objects.filter(author__lte=request.user)
    return render(request, 'sharesite/mypage.html', {'profiles': profiles })

def add_comment_to_give(request, pk):
    give = get_object_or_404(Give, pk=pk)
    if request.method == "POST":
        form = GiveCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.give = give
            comment.save()
            return redirect('give_detail', pk=give.pk)
    else:
        form = GiveCommentForm()
    return render(request, 'sharesite/add_comment_to_give.html', {'form': form})

@login_required
def give_comment_remove(request, pk):
    comment = get_object_or_404(Give_comment, pk=pk)
    comment.delete()
    return redirect('give_detail', pk=comment.give.pk)
