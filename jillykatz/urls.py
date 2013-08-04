from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

# Cachebuster
from django.template.loader import add_to_builtins
add_to_builtins('cachebuster.templatetags.cachebuster')

from jillykatz.widgy_site import site as widgy_site

admin.autodiscover()

urlpatterns = patterns(
    '',
    url('^robots.txt$', TemplateView.as_view(content_type='text/plain', template_name='robots.txt')),
    #url('^sitemap.xml$', TemplateView.as_view(content_type='application/xml', template_name='sitemap.xml')),

    # Home Page
    #url(r'^$', 'jillykatz.views.index', name='site_index'),
    url(r'^$', 'mezzanine.pages.views.page', {'slug': '/'}, name='home'),

    # Admin Site
    url(r'^admin/', include(admin.site.urls)),

    # widgy admin
    url(r'^admin/widgy/', include(widgy_site.urls)),

    # widgy frontend
    url(r'^widgy/', include('widgy.contrib.widgy_mezzanine.urls')),
    url(r'^', include('mezzanine.urls')),
)

# Auth Urls
urlpatterns += patterns(
    'authtools.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout_then_login', name='logout'),
    url(r'^reset/$', 'password_reset'),
    url(r'^reset-done/$', 'password_reset_done'),
    url(r'^reset-confirm/(?P<uidb36>\w+)/(?P<token>[-a-zA-Z0-9]+)/$', 'password_reset_confirm_and_login'),
    url(r'^reset-complete/$', 'password_reset_complete'),
)

urlpatterns += patterns(
    '',
    # Accounts Urls
    #url(r'^account/', include('accounts.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
