from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    path('accounts/', include('accounts.urls')),
    
]