from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.db.models import Avg, Sum

from .models import Sites, SiteName

# Create your views here.

def index(request):
    return render(request, 'index.html',{'sites': SiteName.objects.all()})

def detail(request, site_id):
    site_name = SiteName.objects.get(id=site_id)
    site_details = Sites.objects.filter(site_name__id=site_id)
    return render(request, 'detail.html', context={'site_details': site_details, 'site_name': site_name})

def summary(request):
    method_type = request.GET.get('type')
    final_list = []
    all_site_names = SiteName.objects.all()
    if method_type == 'django':
        for site_name in all_site_names:
            dict_value = Sites.objects.filter(site_name=site_name).aggregate(Sum('a_value'), Sum('b_value'))
            dict_value.update({'site_name': site_name.name})
            final_list.append(dict_value)
            print (final_list)

    else:
        # using python functions
        for site_name in all_site_names:
            query = Sites.objects.filter(site_name=site_name)
            a_value_avg = sum(query.values_list('a_value', flat=True))
            b_value_avg = sum(query.values_list('b_value', flat=True))
            final_list.append({'site_name': site_name.name,
                               'a_value__sum': a_value_avg,
                               'b_value__sum': b_value_avg})
    print (final_list)
    return render(request, 'summary.html', context={'site_details': final_list})

def summary_avarage(request):
    # using django api over raw sql
    method_type = request.GET.get('type')
    final_list = []
    all_site_names = SiteName.objects.all()
    if method_type == 'django':
        for site_name in all_site_names:
            dict_value = Sites.objects.filter(site_name=site_name).aggregate(Avg('a_value'), Avg('b_value'))
            dict_value.update({'site_name': site_name.name})
            final_list.append(dict_value)
    else:
        # using python functions
        for site_name in all_site_names:
            query = Sites.objects.filter(site_name=site_name)
            a_value_avg = sum(query.values_list('a_value', flat=True))/query.count()
            b_value_avg = sum(query.values_list('b_value', flat=True))/query.count()
            final_list.append({'site_name': site_name.name,
                               'a_value__avg': a_value_avg,
                               'b_value__avg': b_value_avg})
    return render(request, 'summary-avg.html', context={'site_details': final_list})