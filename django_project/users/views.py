from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import login

from .forms import SignupForm
from .models import CustomUser
from blog.models import Post  # Example: show user's posts
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello from users!")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # login(request, user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # ✅ Add backend
            return redirect('user_profile')
    else:
        form = SignupForm()
    
    return render(request, 'users/signup.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request, 'users/profile.html', {'user': user, 'posts': posts})
