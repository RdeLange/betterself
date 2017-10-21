from allauth.account.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView, RedirectView
from rest_framework.authtoken import views

react_home_template = 'react/home.html'
react_signup_template = 'react/signup.html'
react_dashboard_template = 'react/dashboard.html'

favicon_view = RedirectView.as_view(url='/static/images/logos/logojoy/favicon.png', permanent=True)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name=react_home_template), name='home'),

    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User Management
    url(r'^users/', include('betterself.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    #
    url(r'^api/', include('apis.urls')),

    # TODO - switch the regex to just pattern match instead of copy/pasting
    url(r'^dashboard-signup/$', TemplateView.as_view(template_name=react_signup_template), name='react-signup'),
    url(r'^dashboard.*/$', TemplateView.as_view(template_name=react_dashboard_template), name='react-dashboard'),
    url(r'^dashboard-login/$', TemplateView.as_view(template_name=react_dashboard_template), name='react-login'),
    url(r'^dashboard-logout/$', TemplateView.as_view(template_name=react_dashboard_template), name='react-logout'),
    url(r'^demo-signup/$', TemplateView.as_view(template_name=react_dashboard_template), name='react-demo-signup'),
    url(r'^settings/$', TemplateView.as_view(template_name=react_dashboard_template), name='react-settings'),

    url(r'^api-token-auth/$', views.obtain_auth_token, name='api-token-auth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^favicon\.ico$', favicon_view),
]

# might have to double check this, not sure why MEDIA is so oddly pronounced
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
