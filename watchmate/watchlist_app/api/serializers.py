from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # NESTED SERIALIZER: 'watchlist' name come from model's "related_name". many= True because watchlist can have many movies

    watchlist = WatchListSerializer(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"


#HyperlinkedModelSerializer helps us to access url for any particular element.