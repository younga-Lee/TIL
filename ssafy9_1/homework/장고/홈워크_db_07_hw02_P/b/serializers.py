# b- serializers.py


class ArticleSerializer(serializers.ModelSerializer):
    __(b)__ = __(a)__(
        __(c)__,
        __(d)__,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', '__(b)__')