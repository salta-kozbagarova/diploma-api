from rest_framework import serializers
from .models import Bargain, BargainType, BargainBet, BargainComment, BargainAddress
from auction_api.users.serializers import UserSerializer
from auction_api.products.serializers import ProductSerializer
from auction_api.categories.serializers import CategorySerializer

class BargainSerializer(serializers.HyperlinkedModelSerializer):
    # full_address = serializers.StringRelatedField(many=True)
    # products = ProductSerializer(many=True)
    # participants = UserSerializer()
    # category = CategorySerializer()

    class Meta:
        model = Bargain
        fields = ('url', 'id', 'end_date', 'bargain_type',
                  'start_price', 'current_price', 'name', 'image', 'products', 'seen', 'participants', 'category',
                  'addresses')

class BargainTypeSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = BargainType
        fields = ('url', 'id', 'name', 'created_by', 'updated_by')

class BargainBetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BargainBet
        fields = ('url', 'id', 'bargain', 'price', 'created_by', 'updated_by')
        depth = 2

class BargainCommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BargainComment
        fields = ('url', 'id', 'bargain', 'comment', 'created_by', 'updated_by')
        depth = 2

class BargainAddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BargainAddress
        fields = ('url', 'id', 'bargain', 'address', 'created_by', 'updated_by')
        depth = 2
