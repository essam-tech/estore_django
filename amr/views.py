from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Category, Product, ProductImage, Cart, CartItem

# ===========================
# الصفحة الرئيسية
# ===========================
def home(request):
    # صور الكاروسيل: نستخدم صور مميزة أولاً، وإذا لم توجد نأخذ أول 5 صور
    carousel_images = ProductImage.objects.filter(is_featured=True)[:5]
    if not carousel_images.exists():
        carousel_images = ProductImage.objects.all()[:5]

    # قائمة التصنيفات الرئيسية فقط (بدون الأبناء)
    categories = Category.objects.filter(parent=None)

    # إعلانات بسيطة (يمكن لاحقًا تخزينها في DB)
    ads = [
        {"title": "زورونا تجدوا ما يسركم", "text": "أفضل العروض لهذا الأسبوع", "image": None},
        {"title": "خصم على الستائر", "text": "خصومات حتى 20%", "image": None},
    ]

    context = {
        "carousel_images": carousel_images,
        "categories": categories,
        "ads": ads,
    }
    return render(request, "home.html", context)


# ===========================
# صفحة قائمة المنتجات حسب التصنيف
# ===========================
def product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    # فقط المنتجات النشطة
    products = category.products.filter(is_active=True)

    context = {
        "category": category,
        "products": products,
    }
    return render(request, "product_list.html", context)


# ===========================
# صفحة تفاصيل المنتج
# ===========================
def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    # لو لديك موديل للألوان أو الـ Variants يمكن تعديل هذا الجزء لاحقًا
    colors = ["بيج", "أبيض", "بني"]  # مثال مؤقت
    main_image = product.images.first()  # الصورة الرئيسية

    context = {
        "product": product,
        "colors": colors,
        "main_image": main_image,
    }
    return render(request, "product_detail.html", context)


# ===========================
# إضافة المنتج للسلة مع كمية محددة
# ===========================
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    # جلب الكمية من POST request، إذا لم توجد فـ 1
    quantity = int(request.POST.get("quantity", 1))
    if quantity < 1:
        quantity = 1

    # إضافة المنتج للسلة
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()

    # يرجع للصفحة السابقة أو صفحة تفاصيل المنتج إذا لم تتوفر
    return redirect(request.META.get("HTTP_REFERER", reverse("product_detail", args=[product.slug])))


# ===========================
# صفحة عرض السلة
# ===========================
@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    subtotal = sum(item.product.price * item.quantity for item in items)

    context = {
        "cart": cart,
        "items": items,
        "subtotal": subtotal,
    }
    return render(request, "cart.html", context)


# ===========================
# تحديث كمية المنتج في السلة
# ===========================
@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()  # لو الكمية صفر نحذف المنتج

    return redirect("cart_view")


# ===========================
# إتمام الشراء (تصفير السلة)
# ===========================
@login_required
def checkout(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    subtotal = sum(item.product.price * item.quantity for item in items)

    if request.method == "POST":
        # هنا لاحقًا ممكن تضيف إنشاء Order وحفظها في DB
        items.delete()  # 🧹 تصفير السلة بعد الإتمام
        return render(request, "checkout_success.html", {"subtotal": subtotal})

    return render(request, "checkout.html", {"cart": cart, "items": items, "subtotal": subtotal})
