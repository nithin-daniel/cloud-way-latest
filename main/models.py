from django.db import models

# Create your models here.
class CeoMessage(models.Model):
    content = models.TextField()
    ceo_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Ceo Message'

    def __str__(self):
        return self.ceo_name
    

class AboutCard(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = 'About Card'

    def __str__(self):
        return self.title
    

class Moments(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Moments/')
    
    class Meta:
        verbose_name_plural = 'Moments'

    def __str__(self):
        return self.title
    
    
class ServicingCountries(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='servicing_countries')
    description = models.CharField(max_length=500)
    banner = models.ImageField(upload_to='servicing_countries_banner')
    details = models.TextField()
    feature_1 = models.CharField(max_length=200)
    feature_2 = models.CharField(max_length=200)
    feature_3 = models.CharField(max_length=200)
    benefits_of_cloud_way = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Servicing Countries'

    def __str__(self):
        return self.title

class University(models.Model):
    university_image = models.ImageField( upload_to='university_image')
    university_name = models.CharField(max_length=100)
    desciption = models.CharField(max_length=100)
    university = models.ForeignKey(ServicingCountries, on_delete=models.CASCADE)
    university_details = models.TextField()
    university_specialities_1 = models.CharField(max_length=100)
    university_specialities_1_icon = models.ImageField( upload_to='university_detail_icons')
    university_specialities_2 = models.CharField(max_length=100)
    university_specialities_2_icon = models.ImageField( upload_to='university_detail_icons')
    university_specialities_3 = models.CharField(max_length=100)
    university_specialities_3_icon = models.ImageField( upload_to='university_detail_icons')
    university_specialities_4 = models.CharField(max_length=100)
    university_specialities_4_icon = models.ImageField( upload_to='university_detail_icons')
    university_specialities_5 = models.CharField(max_length=100)
    university_specialities_5_icon = models.ImageField( upload_to='university_detail_icons')

    class Meta:
        verbose_name_plural = 'University'
    
    def __str__(self):
        return f'{self.university_name} + {self.university}'


    @property
    def title(self):
        return self.university_name

class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    icon_class_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.title

class CourseProvide(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    university = models.ForeignKey(University,on_delete=models.CASCADE,related_name='courses')

    class Meta:
        verbose_name_plural = 'Course Provide'

    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField()
    country = models.ForeignKey(ServicingCountries,on_delete=models.CASCADE)
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    course = models.ForeignKey(CourseProvide,on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return f'{self.first_name} + {self.course}'

class Accreditations(models.Model):
    image = models.ImageField(upload_to='Accreditations/')

    class Meta:
        verbose_name_plural = 'Accreditations'

class Testimonials(models.Model):
    student_name = models.CharField(max_length=50)
    course_name_and_university = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    student_image = models.ImageField(upload_to='testimonials_student_image')

    class Meta:
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.student_name
    
    