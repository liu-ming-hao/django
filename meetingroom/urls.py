"""
URL configuration for meetingroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.utils.translation import gettext as _

urlpatterns = [
    re_path(r'^',include('jobs.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')), # 注册 http://127.0.0.1:8000/accounts/register/
    path('i18n/', include('django.conf.urls.i18n')), # 多语言设置 http://127.0.0.1:8000/i18n/
]

admin.site.site_header = _('Django科技招聘管理系统')