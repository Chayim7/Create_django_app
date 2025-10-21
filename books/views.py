from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import BookForm, ReviewForm
from accounts.models import Follow

def all_reviews(request):
    reviews = Review.objects.select_related('book', 'author').all()
    return render(request, 'books/feed.html', {'reviews': reviews})

@login_required
def following_feed(request):
    following_users = [f.follows for f in Follow.objects.filter(follower=request.user)]
    reviews = Review.objects.filter(author__in=following_users)
    return render(request, 'books/feed.html', {'reviews': reviews})

def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'books/search.html', {'books': books, 'query': query})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_search')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(book=book, author=request.user).first()
    return render(request, 'books/book_detail.html', {'book': book, 'user_review': user_review})

@login_required
def review_create(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()
            return redirect('book_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'books/review_form.html', {'form': form, 'book': book})
