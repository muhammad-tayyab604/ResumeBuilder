from django.contrib import admin
from django.urls import path
from resumeapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='index'),
    path('<int:pk>', views.CandidateView.as_view(), name='CandidateView'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
