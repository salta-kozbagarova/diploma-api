from .models import Category
import rest_framework_filters as filters

class CategoryFilter(filters.FilterSet):
    id = filters.NumberFilter()
    parent = filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'is_active')
