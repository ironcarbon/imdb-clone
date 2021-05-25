from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # NESTED SERIALIZER: 'watchlist' name come from model's "related_name". many= True because watchlist can have many movies
    watchlist = WatchListSerializer(many = True, read_only = True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
