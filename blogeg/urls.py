from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import index, about, blog, blog_single, cat, search
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('blog/', blog),
    path('contact/', contact_view, name="contact-us"),
    path('post/<int:id>/', blog_single, name='blog_single'),
    path('category/<slug:slug>/', cat, name='cat_view'),
    path('search/', search, name='search'),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
