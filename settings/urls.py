"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from clients.views import ClientModelViewSet, ClientRegistrationModelVIewSet, ClientActivation
from news.views import ArticleFillModelViewSet, ArticleModelViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version="v1",
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(prefix="client", viewset=ClientModelViewSet, basename="client")
router.register(prefix="registration", viewset=ClientRegistrationModelVIewSet, basename="registration")
router.register(prefix="articles", viewset=ArticleModelViewSet, basename="articles")


urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('admin/', admin.site.urls),
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("activate/<int:pk>/", ClientActivation.as_view({"get":"retrieve"}), name="activate-account",),
    path("articles/update", ArticleFillModelViewSet.as_view({"post":"create"}), name="article-update"),
    # path("auth/login", CustomTokenObtainPairView.as_view(), name="auth/login")
] 
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]