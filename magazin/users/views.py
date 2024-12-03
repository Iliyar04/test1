

from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm

def login_view(request):
    next_url = request.GET.get('next', '/users/profile/')  # Адрес, куда перенаправлять после входа

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверяем пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Авторизуем пользователя
            return redirect(next_url)  # Перенаправляем на нужный адрес
        else:
            # Если логин или пароль неверные
            return render(request, 'users/login.html', {'error': 'Неверные данные для входа'})

    # Показываем форму, если метод GET
    return render(request, 'users/login.html')




def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Добавляем request.FILES для обработки файлов
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
            user.save()
            login(request, user)  # Авторизуем сразу после регистрации
            return redirect('profile')  # Перенаправляем на профиль
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


from .forms import ProductForm
from .models import Product

# Профиль пользователя
@login_required
def profile_view(request):
    products = Product.objects.filter(user=request.user)  # Товары, загруженные текущим пользователем
    return render(request, 'users/profile.html', {'products': products})

from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Привязываем товар к текущему пользователю
            product.save()
            return redirect('profile')  # Перенаправляем на профиль после добавления товара
    else:
        form = ProductForm()

    return render(request, 'users/add_product.html', {'form': form})



# Страница с подробной информацией о товаре
from django.shortcuts import render, get_object_or_404
from .models import Product

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'users/product_detail.html', {'product': product})

from django.shortcuts import render
from .models import Product

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'users/product_list.html', {'products': products})


def search_product_view(request):
    form = ProductSearchForm(request.GET)
    products = []

    # Показываем товары только если форма отправлена (метод GET с параметром 'query')
    if request.GET.get('query') and form.is_valid():
        query = form.cleaned_data['query']
        products = Product.objects.filter(name__icontains=query)

    return render(request, 'users/search_results.html', {'form': form, 'products': products})