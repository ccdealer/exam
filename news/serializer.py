from rest_framework import serializers

from news.models import Article

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "source_id",
            "source_name",
            "author",
            "title",
            "description",
            "url",
            "url_to_image",
            "published_at",
            "content",
        ]

class FindSerializer(serializers.Serializer):
    q = serializers.CharField()
    domains = serializers.CharField()
    sources = serializers.CharField()
    language = serializers.CharField()
    sortBy = serializers.CharField() 

