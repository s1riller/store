from django.shortcuts import render


# Create your views here.

# Функция = контроллер = въюха = обработчик запроса

def index(request):
    context = {'title': 'Store',
               }
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Store - Каталог',
               'products': [
                   {'image': '/static/vendor/img/products/Adidas-hoodie.png',
                    'name': 'Худи черного цвета с монограммами adidas Originals',
                    'price': '6090',
                    'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
                   {'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                    'name': 'Синяя куртка The North Face',
                    'price': '12090',
                    'description': ' Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
                   {'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                    'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': '5090',
                    'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'}
               ]}
    return render(request, 'products/products.html', context)
