from django.contrib import admin

from .models import Company
from .models import Specialty
from .models import Vacancy
from .models import Image

# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Image, ImageAdmin)
