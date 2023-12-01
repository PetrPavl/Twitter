from django.shortcuts import render, get_object_or_404, redirect
from .models import User
#from .forms import UserForm


def user_list(request):
    users = User.objects.all()
    context = {'users': users, 'title': 'List of Users'}
    return render(request=request, template_name='users/user_list.html', context=context)


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {"user": user}
    return render(request, "users/user_detail.html", context)


# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail')
#     else:
#         form = UserForm()
#     return render(request, 'users/create_user.html', {'form': form})
