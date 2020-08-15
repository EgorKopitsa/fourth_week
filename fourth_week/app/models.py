from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR')
    description = models.CharField(max_length=200)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} {self.location} {self.description} {self.employee_count}'


class Specialty(models.Model):
    title = models.CharField(max_length=15)
    code = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR')
    name = models.CharField(max_length=15, default='')

    def __str__(self) -> str:
        return f'{self.code} {self.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=10)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.title} {self.specialty} {self.company} {self.skills} {self.description} {self.salary_max}' \
               f' {self.salary_min} {self.published_at}'


class Application(models.Model):
    written_username = models.CharField(max_length=10)
    written_phone = models.CharField(max_length=11)
    written_cover_letter = models.CharField(max_length=1000)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")


class Image(models.Model):
    image = models.ImageField(upload_to='MEDIA_PICTURE_IMAGE_DIR')
