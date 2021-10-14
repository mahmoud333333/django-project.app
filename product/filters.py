import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class TASKSFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	Descreption = CharFilter(field_name='Descreption', lookup_expr='icontains')
    


	class Meta:
		model = TASKS
		fields = '__all__'
		exclude = ['date_created','pic','my_file','Whse_Mangament','status']
class FULFILLEDFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')


    class Meta:
        model = TASKS
        fields = '__all__'
        exclude = ['date_created','pic','my_file']	