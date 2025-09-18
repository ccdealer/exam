from datetime import timedelta

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from news.models import Article
from news.serializer import ArticlesSerializer, FindSerializer
from common.newsApi import get_news


class ArticleFillModelViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(timeout=600))
    @swagger_auto_schema(request_body=FindSerializer)
    def create(self, request, *args, **kwargs):
        data = get_news(q=request.data.get("q"))
        created_count = 0

        for item in data:
            if Article.objects.filter(url=item.get("url")).exists():
                continue

            Article.objects.create(
                source_id=item.get("source", {}).get("id"),
                source_name=item.get("source", {}).get("name"),
                url=item.get("url"),
                title=item.get("title"),
                description=item.get("description"),
                author=item.get("author"),
                url_to_image=item.get("urlToImage"),
                published_at=item.get("publishedAt"),
                content=item.get("content"),
            )
            created_count += 1

        return Response({"status": "ok", "created": created_count}, status=201)
    

class ArticleModelViewSet(ViewSet):
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    # @method_decorator(cache_page(timeout=1800))
    def list(self, request:Request, *args, **kwargs):
        queryset = self.queryset

        if request.query_params.get("fresh"):
            l24h = timezone.now() - timedelta(hours=24)
            queryset = queryset.filter(published_at__gte=l24h)

        if temp := request.query_params.get("q-title"):
            queryset = queryset.filter(title__icontains = temp)

        serial = self.serializer_class(queryset, many = True)
        return Response(serial.data)
    
