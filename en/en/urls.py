from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from en import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('news/', include('news.urls'), name='news'),
    path('polls/',include('polls.urls'), name='polls')
  #  path('news/',include('news.urls'),name='news')



]

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

