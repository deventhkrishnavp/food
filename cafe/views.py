from django.shortcuts import render, redirect
from .models import Category, MenuItem, Review, GalleryImage, ContactMessage

def home(request):
    featured_items = MenuItem.objects.filter(is_featured=True)[:6]
    if not featured_items.exists():
        featured_items = MenuItem.objects.all().order_by('-id')[:6]
    reviews = Review.objects.all().order_by('-date')[:5]
    return render(request, 'cafe/home.html', {
        'featured_items': featured_items,
        'reviews': reviews
    })

def about(request):
    return render(request, 'cafe/about.html')

def menu(request):
    categories = Category.objects.all().prefetch_related('items')
    return render(request, 'cafe/menu.html', {'categories': categories})

def reviews(request):
    reviews_list = Review.objects.all().order_by('-date')
    return render(request, 'cafe/reviews.html', {'reviews': reviews_list})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'cafe/gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('contact')
    return render(request, 'cafe/contact.html')
