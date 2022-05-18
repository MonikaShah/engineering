from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.EnggIndia, name='engineering_colleges'),
    path('engineering_colleges/',views.EnggIndia, name='engineering_colleges'),
    # path('edit/<int:id>', views.edit),
    # path('export/<int:proj_id>', views.export),
    # path('search',views.search, name='search')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
