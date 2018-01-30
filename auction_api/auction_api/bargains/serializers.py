from rest_framework import serializers
from .models import Bargain, BargainType, BargainBet, BargainComment
from auction_api.users.serializers import UserSerializer
from auction_api.products.serializers import ProductSerializer
from auction_api.categories.serializers import CategorySerializer
from auction_api.categories.models import Category
from auction_api.administrative_division.serializers import AdministrativeDivisionSerializer, AdministrativeDivisionDetailSerializer

class BargainTypeSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    updated_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )

    class Meta:
        model = BargainType
        fields = ('url', 'id', 'name', 'created_by', 'updated_by', 'created_at', 'updated_at')

class BargainCommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BargainComment
        fields = ('url', 'id', 'bargain', 'comment', 'created_by', 'updated_by')
        depth = 2

class BargainSerializer(serializers.HyperlinkedModelSerializer):
    # products = ProductSerializer(many=True)
    participants = UserSerializer(many=True)
    participants_count = serializers.SerializerMethodField()
    category = CategorySerializer()
    bargain_type = BargainTypeSerializer()
    created_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    updated_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    address = AdministrativeDivisionDetailSerializer()
    full_address = serializers.SerializerMethodField()
    comments = BargainCommentSerializer(many=True)

    class Meta:
        model = Bargain
        fields = ('url', 'id', 'end_date', 'bargain_type',
                  'start_price', 'current_price', 'name', 'image', 'products', 'seen', 'participants',
                  'participants_count', 'category', 'comments',
                  'address', 'full_address', 'created_by', 'updated_by', 'created_at', 'updated_at')

    def get_participants_count(self, obj):
        return len(obj.participants.all())

    def get_full_address(self, obj):
        if obj.address:
            return obj.address.get_full_address()
        else:
            return ''

class BargainBetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BargainBet
        fields = ('url', 'id', 'bargain', 'price', 'created_by', 'updated_by')
        depth = 2
