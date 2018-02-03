from .models import Category
import rest_framework_filters as filters
from django.db.models.constants import LOOKUP_SEP


class CategoryFilter(filters.FilterSet):
    is_root = filters.BooleanFilter(name='parent', method='category_is_root')
    parent = filters.RelatedFilter('auction_api.categories.filters.CategoryFilter', name='parent',
                                   queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'is_active', 'code')

    def category_is_root(self, qs, name, value):
        isnull = not not value
        lookup_expr = LOOKUP_SEP.join([name, 'isnull'])

        return qs.filter(**{lookup_expr: isnull})
