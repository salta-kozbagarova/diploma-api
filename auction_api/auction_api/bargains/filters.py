from .models import Bargain
from auction_api.categories.models import Category
import rest_framework_filters as filters
from django.db.models.constants import LOOKUP_SEP
from auction_api.administrative_division.models import AdministrativeDivision
from auction_api.products.models import Product

def categories(request):
    category_code = request.query_params.get('category__code')
    category = Category.objects.get(code=category_code)
    return Category.objects.filter(id__in=category.all_children_id)

class BargainCategoryFilter(filters.FilterSet):
    id = filters.NumberFilter(name='id', method='categories_in_id')
    code = filters.CharFilter(name='id', method='categories_in_code')
    name = filters.CharFilter(name='id', method='categories_in_name')

    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'is_active', 'code')

    def categories_in_id(self, qs, name, value):
        # TODO: may be to improve try catch block
        try:
            category = Category.objects.get(pk=value)
            cat_ids = category.all_children_id
            lookup_expr = LOOKUP_SEP.join([name, 'in'])
            return qs.filter(**{lookup_expr: cat_ids})
        except Category.DoesNotExist:
            return None

    def categories_in_code(self, qs, name, value):
        # TODO: may be to improve try catch block
        try:
            category = Category.objects.get(code=value)
            cat_ids = category.all_children_id
            lookup_expr = LOOKUP_SEP.join([name, 'in'])
            return qs.filter(**{lookup_expr: cat_ids})
        except Category.DoesNotExist:
            return None

    def categories_in_name(self, qs, name, value):
        # TODO: may be to improve try catch block
        try:
            category = Category.objects.get(name=value)
            cat_ids = category.all_children_id
            lookup_expr = LOOKUP_SEP.join([name, 'in'])
            return qs.filter(**{lookup_expr: cat_ids})
        except Category.DoesNotExist:
            return None

class BargainAddressFilter(filters.FilterSet):
    id = filters.NumberFilter(name='id', method='addresses_in_id')
    name = filters.CharFilter(name='id', method='addresses_in_name')

    class Meta:
        model = AdministrativeDivision
        fields = ('id', 'name', 'parent', 'administrative_level')

    def addresses_in_id(self, qs, name, value):
        # TODO: may be to improve try catch block
        try:
            adm = AdministrativeDivision.objects.get(pk=value)
            adm_ids = adm.all_children_id
            lookup_expr = LOOKUP_SEP.join([name, 'in'])
            return qs.filter(**{lookup_expr: adm_ids})
        except AdministrativeDivision.DoesNotExist:
            return None

    def addresses_in_name(self, qs, name, value):
        # TODO: may be to improve try catch block
        try:
            adm = AdministrativeDivision.objects.get(name=value)
            adm_ids = adm.all_children_id
            lookup_expr = LOOKUP_SEP.join([name, 'in'])
            return qs.filter(**{lookup_expr: adm_ids})
        except AdministrativeDivision.DoesNotExist:
            return None

class BargainProductFilter(filters.FilterSet):
    name = filters.AllLookupsFilter(name='name')
    class Meta:
        model = Product
        fields = ('name',)

class BargainFilter(filters.FilterSet):
    category = filters.RelatedFilter(BargainCategoryFilter, name='category', queryset=Category.objects.all())
    address = filters.RelatedFilter(BargainAddressFilter, name='address', queryset=AdministrativeDivision.objects.all())
    current_price_min = filters.NumberFilter(name='current_price', lookup_expr='gt', label='Minimum price')
    current_price_max = filters.NumberFilter(name='current_price', lookup_expr='lt', label='Maximum price')
    product = filters.RelatedFilter(BargainProductFilter, name='product', queryset=Product.objects.all())

    class Meta:
        model = Bargain
        fields = ('id', 'bargain_type', 'start_price', 'current_price', 'category', 'address', 'is_active', 'on_top', 'product')
