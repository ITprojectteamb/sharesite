from django.shortcuts import render
from django.utils import timezone
from .models import  Give,Want,Profile,Give_comment,Want_comment,Profile_comment
from django.shortcuts import render, get_object_or_404
from .forms import GiveCreateForm,WantCreateForm,ProfileCreateForm,GiveCommentForm,WantCommentForm,ProfileCommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import PermissionDenied


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Want
    template_name = 'post_list.html'
    paginate_by = 6

    def get_queryset(self):
        wants = Want.objects.filter(emergency_attribute__contains='1').order_by('-final_update_time')
        return wants

class GiveListView(LoginRequiredMixin, generic.ListView):
    model = Give
    template_name = 'give_list.html'
    paginate_by = 6
    
    def get_queryset(self):
        gives = Give.objects.order_by('-final_update_time')
        return gives

class WantListView(LoginRequiredMixin, generic.ListView):
    model = Want
    template_name = 'want_list.html'
    paginate_by = 6
    
    def get_queryset(self):
        wants = Want.objects.order_by('-final_update_time')
        return wants


class GiveCreateView(LoginRequiredMixin, generic.CreateView):
    model = Give
    form_class = GiveCreateForm
    template_name = 'give_new.html'
    success_url = reverse_lazy('give_list')

    def form_valid(self, form):
        give = form.save(commit=False)
        form.instance.author = self.request.user
        give.save()
        messages.success(self.request, '品物を登録しました。')
        return super(GiveCreateView, self).form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, "品物が登録できませんでした。")
        return super().form_invalid(form)


class WantCreateView(LoginRequiredMixin, generic.CreateView):
    model = Want
    template_name = 'want_new.html'
    form_class = WantCreateForm
    success_url = reverse_lazy('want_list')

    def form_valid(self, form):
        want = form.save(commit=False)
        form.instance.author = self.request.user
        want.save()
        messages.success(self.request, '品物を登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "品物が登録できませんでした。")
        return super().form_invalid(form)

def give_edit(request, pk):
    give = get_object_or_404(Give, pk=pk)
    if request.method == "POST":
        form = GiveForm(request.POST, instance=give)
        if form.is_valid():
            give = form.save(commit=False)
            give.author = request.user
            give.published_date = timezone.now()
            give.save()
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

class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'profile_list.html'
    paginate_by = 6
    
    def get_queryset(self):
        profiles = Profile.objects.all()
        return profiles

class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = Profile
    template_name = 'profile_new.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('profile_list')

    def form_valid(self, form):
        profile = form.save(commit=False)
        form.instance.author = self.request.user
        profile.save()
        messages.success(self.request, 'プロフィールを登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "プロフィールが登録できませんでした。")
        return super().form_invalid(form)

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    
    
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

def add_comment_to_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = profile
            comment.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileCommentForm()
    return render(request, 'sharesite/add_comment_to_profile.html', {'form': form})

@login_required
def profile_comment_remove(request, pk):
    comment = get_object_or_404(Profile_comment, pk=pk)
    comment.delete()
    return redirect('profile_detail', pk=comment.profile.pk)

@login_required
def want_comment_remove(request, pk):
    comment = get_object_or_404(Want_comment, pk=pk)
    comment.delete()
    return redirect('want_detail', pk=comment.want.pk)  
  

class GiveDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Give
    template_name = 'give_delete.html'
    success_url = reverse_lazy('give_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(GiveDeleteView, self).dispatch(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "投稿を削除しました。")
        return super().delete(request, *args, **kwargs)

class GiveUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Give
    template_name = 'give_update.html'
    form_class = GiveCreateForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(GiveUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('give_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '投稿を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿を更新できませんでした。")
        return super().form_invalid(form)

class WantDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Want
    template_name = 'want_delete.html'
    success_url = reverse_lazy('want_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(WantDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "投稿を削除しました。")
        return super().delete(request, *args, **kwargs)

class WantUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Want
    template_name = 'want_update.html'
    form_class = WantCreateForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(WantUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('want_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '投稿を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿を更新できませんでした。")
        return super().form_invalid(form)

class ProfileDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('profile_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(ProfileDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "投稿を削除しました。")
        return super().delete(request, *args, **kwargs)

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    form_class = ProfileCreateForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '投稿を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿を更新できませんでした。")
        return super().form_invalid(form)
