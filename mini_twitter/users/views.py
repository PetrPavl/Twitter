from django.shortcuts import render, get_object_or_404
from .models import User


def user_list(request):
    users = User.objects.all()
    context = {'users': users, 'title': 'List of Users'}
    return render(request=request, template_name='users/user_list.html', context=context)


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {"user": user}
    return render(request, "users/user_detail.html", context)
