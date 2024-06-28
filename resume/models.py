from django.db import models

class Experience(models.Model):
    duration_of_activity = models.CharField(max_length=20,verbose_name="Duration of Activity")
    employment_status= models.CharField(max_length=50,verbose_name="Employment Status")
    workplace = models.CharField(max_length=100,verbose_name="Workplace")
    description = models.TextField(verbose_name="description")
    status = models.BooleanField(default=True,verbose_name="status")
    date = models.DateTimeField(auto_now=True,verbose_name="Date created model")
    def __str__(self):
        return self.workplace

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Experience"


class Education(models.Model):
    year_of_education = models.CharField(max_length=20,verbose_name="Year of education")
    name_of_school= models.CharField(max_length=20,verbose_name="Name of school")
    education_place= models.CharField(max_length=50,verbose_name="Education Place")
    field_of_Study = models.CharField(max_length=50,verbose_name="Field of Study")
    description = models.TextField(verbose_name="description")
    status = models.BooleanField(default=True, verbose_name="status")
    date = models.DateTimeField(auto_now=True, verbose_name="Date created model")
    def __str__(self):
        return self.field_of_Study

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Education"