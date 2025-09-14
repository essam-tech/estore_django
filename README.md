# متجر Essam الإلكتروني | Essam E-Store

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.1.13-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---


**متجر Essam الإلكتروني** هو مشروع Django لإنشاء متجر إلكتروني كامل لإدارة وعرض المنتجات بطريقة سهلة وجذابة.

### المميزات الرئيسية

* **الصفحة الرئيسية**: عرض صور مميزة في الكاروسيل، وتصنيفات المنتجات الرئيسية، وإعلانات.
* **قائمة المنتجات**: عرض المنتجات حسب التصنيف مع تصفية المنتجات النشطة فقط.
* **صفحة تفاصيل المنتج**:

  * صورة المنتج الرئيسية.
  * اختيار اللون (اختياري).
  * تحديد الكمية.
  * عرض السعر وزر إضافة للسلة.
* **سلة التسوق**: إدارة المنتجات المختارة والكميات لكل مستخدم.
* **إدارة المستخدمين**: تسجيل الدخول وتسجيل المستخدمين الجدد.

### التقنيات المستخدمة

* Django 4.1.13
* Python 3.13
* HTML5 + CSS3 + Bootstrap 5
* SQLite (يمكن استبدالها بـ PostgreSQL أو MySQL)

### كيفية التشغيل محلياً

1. استنساخ المشروع:

```bash
git clone https://github.com/essam-tech/estore_django.git
cd estore_django
```

2. إنشاء بيئة افتراضية وتثبيت المتطلبات:

```bash
python -m venv venv
venv\Scripts\activate   # على Windows
pip install -r requirements.txt
```

3. تطبيق المايجريشنات:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. تشغيل السيرفر:

```bash
python manage.py runserver
```

5. الوصول إلى المتجر:

```
http://127.0.0.1:8000/
```

---

## 🇺🇸 English

**Essam E-Store** is a Django project for creating a fully functional online store to manage and display products easily and efficiently.

### Key Features

* **Home Page**: Display featured products in a carousel, main product categories, and simple ads.
* **Product Listing**: Show products by category, filtering only active products.
* **Product Detail Page**:

  * Main product image.
  * Color selection (optional).
  * Quantity selector.
  * Price display and add-to-cart button.
* **Shopping Cart**: Manage selected products and quantities for each user.
* **User Management**: Login and registration functionality.

### Technologies Used

* Django 4.1.13
* Python 3.13
* HTML5 + CSS3 + Bootstrap 5
* SQLite (can be replaced with PostgreSQL or MySQL)

### Running Locally

1. Clone the repository:

```bash
git clone https://github.com/essam-tech/estore_django.git
cd estore_django
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate   # on Windows
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the server:

```bash
python manage.py runserver
```
5. Open the store in your browser:
http://127.0.0.1:8000/
```

---
