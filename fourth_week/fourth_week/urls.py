"""fourth_week URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import CompanyCardView
from app.views import custom_handler404
from app.views import custom_handler500
from app.views import HomeView
from app.views import MyCompanyVacanciesView
from app.views import MyCompanyView
from app.views import MyLoginView
from app.views import OneVacanciesView
from app.views import SentView
from app.views import SpecialVacanciesView
from app.views import UserCreateView
from app.views import VacanciesView
from app.views import VacancyView
from django.contrib.auth.views import LogoutView


handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:specialty_title_str>/', SpecialVacanciesView.as_view()),
    path('companies/<int:company_id>/', CompanyCardView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view()),
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('mycompany/', MyCompanyView.as_view(), name='company'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:vacancy_id>/', OneVacanciesView.as_view()),
    path('vacancies/<int:vacancy_id>/send/', SentView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
