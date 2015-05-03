from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import core.views as coreviews

urlpatterns = [
    # Examples:
    # url(r'^$', 'coffeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',coreviews.SplashView.as_view()),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
