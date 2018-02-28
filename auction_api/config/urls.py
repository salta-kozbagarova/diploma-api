from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from django.conf.urls.i18n import i18n_patterns
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = i18n_patterns(
    *(
        url(r'^api/bargains/', include('auction_api.bargains.urls')),
        url(r'^api/users/', include('auction_api.users.urls')),
        url(r'^api/categories/', include('auction_api.categories.urls')),
        url(r'^api/products/', include('auction_api.products.urls')),
        url(r'^api/transports/', include('auction_api.transports.urls')),
        url(r'^api/arts/', include('auction_api.arts.urls')),
        url(r'^api/clothes/', include('auction_api.clothes.urls')),
        url(r'^api/electronics/', include('auction_api.electronics.urls')),
        url(r'^api/other/', include('auction_api.other.urls')),
        url(r'^api/real-estates/', include('auction_api.real_estates.urls')),
        url(r'^api/administrative-divisions/', include('auction_api.administrative_division.urls')),
        url(r'^api/ad-banners/', include('auction_api.ad_banners.urls')),
        url(r'^api/search-radiuses/', include('auction_api.search_radius.urls')),
        url(r'^schema/$', schema_view),
        # Django Admin, use {% url 'admin:index' %}
        url(settings.ADMIN_URL, admin.site.urls),
        url(r'^api-token-auth/', obtain_jwt_token),
        url(r'^api-token-refresh/', refresh_jwt_token),
        url(r'^api-token-verify/', verify_jwt_token),
    ),
    **{"prefix_default_language" : False}
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
