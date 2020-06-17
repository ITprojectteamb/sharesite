from django.shortcuts import render
from django.utils import timezone
from .models import  Post,Give,Want,Profile,Item,Employee,Give_comment,Want_comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,GiveCreateForm,WantCreateForm,ProfileForm,GiveCommentForm,WantCommentForm
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
        wants = Want.objects.order_by('-open_date')
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


class WantCreateView(LoginRequiredMixin, generic.CreateView):
    model = Want
    template_name = 'want_new.html'
    form_class = WantCreateForm
    success_url = reverse_lazy('want_list')

    def form_valid(self, form):
        want = form.save(commit=False)
        want.user = self.request.user
        want.save()
        messages.success(self.request, '品物を登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "品物が登録できませんできた。")
        return super().form_invalid(form)

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

class GiveDetailView(LoginRequiredMixin, generic.DetailView):
    model = Give
    template_name = 'give_detail.html'


class WantDetailView(LoginRequiredMixin, generic.DetailView):
    model = Want
    template_name = 'want_detail.html'


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


def add_comment_to_want(request, pk):
    want = get_object_or_404(Want, pk=pk)
    if request.method == "POST":
        form = WantCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.want = want
            comment.save()
            return redirect('want_detail', pk=want.pk)
    else:
        form = WantCommentForm()
    return render(request, 'sharesite/add_comment_to_want.html', {'form': form})

@login_required
def want_comment_remove(request, pk):
    comment = get_object_or_404(Want_comment, pk=pk)
    comment.delete()
    return redirect('want_detail', pk=comment.want.pk)
