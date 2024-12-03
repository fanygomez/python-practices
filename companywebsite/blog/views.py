from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    
    return render(request, "blog/blog.html", { 'posts': posts })

def category(request, category_id):
    category_found = get_object_or_404(Category,id= category_id)
    posts = Post.objects.filter(categories=category_found)
        
    return render(request= request, template_name="blog/category.html",context= {'category': category, 'posts': posts })
    