from .models import Bargain
from auction_api.categories.models import Category
import rest_framework_filters as filters
from django.db.models.constants import LOOKUP_SEP
from auction_api.categories.filters import CategoryFilter

def categories(request):
    category_code = request.query_params.get('category__code')
    category = Category.objects.get(code=category_code)
    return Category.objects.filter(id__in=category.all_children_id)

class BargainFilter(filters.FilterSet):
    has_image = filters.BooleanFilter(name='image', method='bargain_has_image')
    category = filters.CharFilter(name='category', method='bargain_in_category')

    class Meta:
        model = Bargain
        fields = ('id', 'bargain_type', 'start_price', 'current_price', 'name', 'category', 'is_active')

    def bargain_has_image(self, qs, name, value):
        isnull = not not value
        lookup_expr = LOOKUP_SEP.join([name, 'isnull'])

        return qs.filter(**{lookup_expr: isnull})

    def bargain_in_category(self, qs, name, value):
        # TODO: if category doesn't exist catch the exception
        category = Category.objects.get(code=value)
        cat_ids = category.all_children_id
        lookup_expr = LOOKUP_SEP.join([name, 'in'])

        return qs.filter(**{lookup_expr: cat_ids})
