from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, CartItem

# first view testing how its work
def index(request):
    #all data get from database post_table
    category = request.GET.get('category')
    if category:
        post_category = Post.objects.filter(category = category)
    else:
        post_category = Post.objects.all()[:12]
    return render(request, 'index.html',{'posts':post_category})


def detailview(request, id):

    # posts = Post.objects.all()
    
    detail_category = Post.objects.filter(category=id)

    title_category  = Post.objects.filter(category=id)[:1]

    return render(request, 'detail.html', {'posts':detail_category, 'post1':title_category})

def textview(request):
    return render(request, 'parse.html')


def cartview(request):
    # `get()` returns a single Post instance which is not iterable.
    # The template expects `posts` to be iterable (it does `{% for post in posts %}`).
    # Return a queryset containing the post so the template loop works.
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)
    print(cart_items)
    total_price = sum(item.total() for item in cart_items)

    return render(request, 'cart.html',{'items':cart_items, 'total':total_price})



def cartproductdetail(request, slug):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    food = get_object_or_404(Post, slug=slug)
    item, created = CartItem.objects.get_or_create(session_key=session_key, food=food)

    if not created:
        item.quantity += 1
        item.save()
    return redirect('blog:cart_page')


def update_cart(request, id):
    item = get_object_or_404(CartItem, id=id)
    action = request.POST.get("action")

    if action == 'increase':
        item.quantity += 1

    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1

    elif action == 'delete':
        item.delete()
        return redirect('blog:cart_page')
    
    item.save()

    return redirect('blog:cart_page')