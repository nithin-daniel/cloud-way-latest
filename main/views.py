from django.shortcuts import render
from random import shuffle
from main.models import CeoMessage,AboutCard,Moments,ServicingCountries,University,Service,CourseProvide,Accreditations,Testimonials
from main.forms import ContactForm

# Create your views here.
def index(request):
    servicing_countries = ServicingCountries.objects.all()
    accreditations = Accreditations.objects.all()
    service = Service.objects.all()
    testimonials = Testimonials.objects.all()

    context = {
        "accreditations":accreditations,
        "servicing_countries":servicing_countries,
        "service":service,
        "testimonials":testimonials
    }
    return render(request,'home.html',context)
def about(request):
    ceo_message_obj = CeoMessage.objects.all()
    ceo_about_objs = AboutCard.objects.all()

    context = {
        "ceo_name":ceo_message_obj,
        "ceo_about_objs":ceo_about_objs,
    }
    return render(request,'main/about.html',context)

def moments(request):
    moments = Moments.objects.all()
    context = {
        "moments":moments,
    }
    return render(request,'main/moments.html',context)

def service_details(request,id):
    obj = ServicingCountries.objects.get(id=id)
    title = obj.title
    university = University.objects.filter(university=id)
    servicing_countries = ServicingCountries.objects.all()
    my_list = list(servicing_countries)
    shuffle(my_list)
    context = {
        "obj":obj,
        "servicing_countries":my_list,
        "university":university
    }
    return render(request,'main/service-detail.html',context)

def university_detail_page(request,id):
    try:
        university = University.objects.get(university=id)
    except University.DoesNotExist:
        university=None
    context = {
        "university":university,
    }
    return render(request,'main/Univercity.html',context)

def service(request):
    service = Service.objects.all()
    context = {
        "service":service
    }
    return render(request,'main/service.html',context)

def contact(request):
    countries = ServicingCountries.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "countries":countries,
    }
    return render(request,'main/contact.html',context)

def all_courses(request):
    course = CourseProvide.objects.all()
    context = {
        "courses":course
    }
    return render(request,'main/courses.html',context)

def load_univeristies(request):
    country_id = request.GET.get('country')
    univesity_objs = University.objects.filter(university_id=country_id).order_by('university_name')
    return render(request, 'dropdown_options.html', {'objs':univesity_objs,"title":"Select preferred University*" })


def load_courses(request):
    university_id = request.GET.get('university')
    courses_objs = CourseProvide.objects.filter(university_id=university_id)
    return render(request, 'dropdown_options.html', {'objs':courses_objs,"title":"Select preferred Course*" })