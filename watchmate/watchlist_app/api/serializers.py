from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many = True, read_only = True)

    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # NESTED SERIALIZER: 'watchlist' name come from model's "related_name". many= True because watchlist can have many movies
    watchlist = WatchListSerializer(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
