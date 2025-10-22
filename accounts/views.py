from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from .models import Follow

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    following = Follow.objects.filter(follower=request.user)
    followers = Follow.objects.filter(follows=request.user)
    return render(request, 'accounts/profile.html', {
        'following': following,
        'followers': followers,
        'user_reviews': request.user.reviews.all(),
    })

@login_required
def profile_other(request, username):
    user_obj = get_object_or_404(User, username=username)

    # Check if current user follows this profile
    is_following = Follow.objects.filter(follower=request.user, follows=user_obj).exists()

    # Check if this user follows the current user (for "Follows you" badge)
    follows_you = Follow.objects.filter(follower=user_obj, follows=request.user).exists()

    # Get their followers and who they follow
    followers = Follow.objects.filter(follows=user_obj)
    following = Follow.objects.filter(follower=user_obj)

    return render(request, 'accounts/profile_other.html', {
        'profile_user': user_obj,
        'is_following': is_following,
        'follows_you': follows_you,
        'followers': followers,
        'following': following,
        'reviews': user_obj.reviews.all(),
    })

@login_required
def follow_toggle(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    follow_obj = Follow.objects.filter(follower=request.user, follows=user_to_follow)
    if follow_obj.exists():
        follow_obj.delete()
    else:
        Follow.objects.create(follower=request.user, follows=user_to_follow)
    return redirect('profile_other', username=username)

@login_required
def user_search(request):
    query = request.GET.get('q', '')
    results = User.objects.filter(username__icontains=query) if query else []
    return render(request, 'accounts/user_search.html', {'results': results, 'query': query})
