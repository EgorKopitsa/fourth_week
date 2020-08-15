from django.views.generic import CreateView
from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from fourth_week.forms import ApplicationForm
from app.models import Application
from app.models import Company
from app.models import Image
from app.models import Specialty
from app.models import Vacancy


# Create your views here.


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка на нашей стороне')


class HomeView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()
        user = request.user

        context = {
            'specialties': specialties,
            'companies': companies,
            'user': user,
        }
        return render(request, 'app/index.html', context=context)


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies
        }
        return render(request, 'app/all_vacancies.html', context=context)


class SpecialVacanciesView(View):
    def get(self, request, specialty_title_str):
        specialty_title = Specialty.objects.filter(code=specialty_title_str).first()
        if not specialty_title:
            raise Http404
        special_vacancies = Vacancy.objects.filter(skills=specialty_title_str)
        context = {
            'specialty_title': specialty_title,
            'special_vacancies': special_vacancies
        }
        return render(request, 'app/special_vacancies.html', context=context)


class CompanyCardView(View):
    def get(self, request, company_id):
        company = Company.objects.filter(id=company_id).first()
        vacancies = company.vacancies.all()
        if not company:
            raise Http404

        context = {
            'company': company,
            'vacancies': vacancies
        }

        return render(request, 'app/company.html', context=context)


class VacancyView(View):
    def get(self, request, vacancy_id):
        vacancy_sought = Vacancy.objects.filter(id=vacancy_id).first()
        if not vacancy_sought:
            raise Http404

        application_form = ApplicationForm()

        context = {
            'vacancy': vacancy_sought,
            'application_form': application_form,
        }
        return render(request, 'app/vacancy.html', context=context)

    def post(self, request, vacancy_id):
        vacancy_sought = Vacancy.objects.filter(id=vacancy_id).first()
        application_form = ApplicationForm(request.POST)
        if request.method == 'POST':
            if application_form.is_valid():
                Application.objects.create(
                    written_username=application_form.cleaned_data['written_username'],
                    written_phone=application_form.cleaned_data['written_phone'],
                    written_cover_letter=application_form.cleaned_data['written_cover_letter'],
                    user=User.objects.filter(id=request.user.id).first(),
                    vacancy=Vacancy.objects.filter(id=vacancy_id).first(),
                )
                return redirect('send/')

        context = {
            'vacancy': vacancy_sought,
            'application_form': application_form
        }
        return render(request, 'app/vacancy.html', context=context)


class SentView(View):
    def get(self, request, vacancy_id):
        image = Image.objects.all().first()
        context = {
            'vacancy': vacancy_id,
            'image': image
        }
        return render(request, 'app/sent.html', context=context)


class MyCompanyView(View):
    def get(self, request):
        return render(request, 'app/company-create.html')


class CompanyEdit(View):
    def get(self, request):
        return render(request, 'app/company-edit.html')


class MyCompanyVacanciesView(View):
    def get(self, request):
        return render(request, 'app/vacancy-list.html')


class OneVacanciesView(View):
    def get(self, request, vacancy_id):
        return render(request, 'app/vacancy-edit.html')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'app/login.html'


class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'app/register.html'
