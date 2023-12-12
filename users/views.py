from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, LoginForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('login_view')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if check_password(form.cleaned_data['password'], user.password):
                login(request, user)
                return redirect('post_list')
            else:
                print("Incorrect password")
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'users/login_user.html', {'form': form})


class UserLogoutView(TemplateView):
    template_name = 'users/logout_user.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('login_view'))

@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.user.has_liked_post(post):
        request.user.unlike_post(post)
    else:
        request.user.like_post(post)

    return redirect('post_detail', pk=post_id)