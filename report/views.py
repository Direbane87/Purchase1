from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.http import HttpResponse

from .models import Plan, Fact, Fact_pay, Spr1_kvr, Spr2_okved2, Spr3_okpd2, Spr4_requirements, Spr5_unit, Spr6_region, Spr7_method, Spr8_result
from .forms import PlanForm, FactForm, FactPayForm
from .resources import FactPayResource

def export(request):
    factpay_resource = FactPayResource()
    dataset = factpay_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content_Disposition'] = 'attachment; filename="factpay.xls"'
    return response

class Filter:
    def get_kvr(self):
        return Spr1_kvr.objects.all()

    def get_method(self):
        return Spr7_method.objects.all()

    def get_pay(self):
        return Fact_pay.objects.all()

    def get_fact(self):
        return Fact.objects.all()

class Spr1View(Filter, View):
    def get(self, request):
        spr1 = Spr1_kvr.objects.all()
        return render(request, "report/spr1_list.html", {"spr1_list": spr1})

class Spr2View(View):
    def get(self, request):
        spr2 = Spr2_okved2.objects.all()
        return render(request, "report/spr2_list.html", {"spr2_list": spr2})

class Spr3View(View):
    def get(self, request):
        spr3 = Spr3_okpd2.objects.all()
        return render(request, "report/spr3_list.html", {"spr3_list": spr3})

class Spr4View(View):
    def get(self, request):
        spr4 = Spr4_requirements.objects.all()
        return render(request, "report/spr4_list.html", {"spr4_list": spr4})

class Spr5View(View):
    def get(self, request):
        spr5 = Spr5_unit.objects.all()
        return render(request, "report/spr5_list.html", {"spr5_list": spr5})

class Spr6View(View):
    def get(self, request):
        spr6 = Spr6_region.objects.all()
        return render(request, "report/spr6_list.html", {"spr6_list": spr6})

class Spr7View(Filter, View):
    def get(self, request):
        spr7 = Spr7_method.objects.all()
        return render(request, "report/spr7_list.html", {"spr7_list": spr7})

class Spr8View(View):
    def get(self, request):
        spr8 = Spr8_result.objects.all()
        return render(request, "report/spr8_list.html", {"spr8_list": spr8})

"""Оплата"""
class FactPayView(Filter, ListView):
    model = Fact_pay
    queryset = Fact_pay.objects.all()
    template_name = "report/fact_pay_list.html"

def AddFactPay(request):
    error = ''
    if request.method == 'POST':
        form = FactPayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pay')
        else:
            error = 'Форма введена неправильно'

    form = FactPayForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'report/fact_pay_add.html', data)

class FactPayDetailView(DetailView):
    model = Fact_pay
    template_name = 'report/fact_pay_detail.html'
    context_object_name = 'pay'

class FactPayUpdateView(UpdateView):
    model = Fact_pay
    template_name = 'report/fact_pay_add.html'
    form_class = FactPayForm

class FactPayDeleteView(DeleteView):
    model = Fact_pay
    success_url = '/pay'
    template_name = 'report/fact_pay_delete.html'

class FilterPayView(Filter, ListView):
    def get_queryset(self):
        year = self.request.GET.getlist("year")[0]
        fact = self.request.GET.getlist("fact_id")

        if (fact == ['0']):
            for f in Filter.get_fact(self):
                fact.append(str(f.id))

        queryset = Fact_pay.objects.filter(
            Q(year__icontains=year) &
            Q(id_fact__in=fact)
        )

        return queryset

"""План"""
class PlansView(Filter, ListView):
    model = Plan
    queryset = Plan.objects.all()
    template_name = "report/plan_list.html"

def AddPlan(request):
    error = ''
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            if (request.POST.get('result') == '1'):
                fact = Fact()
                fact.kvr = Spr1_kvr.objects.get(id=request.POST.get('kvr'))
                fact.name_contract = request.POST.get('name_contract')
                fact.source_finance = request.POST.get('source_finance')
                fact.executor = request.POST.get('executor')
                fact.number_contract = request.POST.get('number_contract')
                fact.save()
            form.save()
            return redirect('plan')
        else:
            error = 'Форма введена неправильно'

    form = PlanForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'report/plan_add.html', data)

class PlanDetailView(DetailView):
    model = Plan
    template_name = 'report/plan_detail.html'
    context_object_name = 'plan'

class PlanUpdateView(UpdateView):
    model = Plan
    template_name = 'report/plan_add.html'
    form_class = PlanForm

class PlanDeleteView(DeleteView):
    model = Plan
    success_url = '/plan'
    template_name = 'report/plan_delete.html'

class FilterPlanView(Filter, ListView):
    def get_queryset(self):
        date1_placing = self.request.GET.getlist("date1_placing")[0]
        date2_placing = self.request.GET.getlist("date2_placing")[0]
        date1_term = self.request.GET.getlist("date1_term")[0]
        date2_term = self.request.GET.getlist("date2_term")[0]

        source_finance = self.request.GET.getlist("source_filter")[0]

        kvr_itog = self.request.GET.getlist("kvr")
        if (kvr_itog == []):
            for kvr in Filter.get_kvr(self):
                kvr_itog.append(str(kvr.id))
        method_itog = self.request.GET.getlist("method")

        if (method_itog == []):
            for method in Filter.get_kvr(self):
                method_itog.append(str(method.id))

        if (date1_placing == ''):
            date1_placing = "1000-01-01"
        if (date2_placing == ''):
            date2_placing = "3000-01-01"

        if (date1_term == ''):
            date1_term = "1000-01-01"
        if (date2_term == ''):
            date2_term = "3000-01-01"

        queryset = Plan.objects.filter(
            Q(kvr__in=kvr_itog) &
            Q(method__in=method_itog) &
            Q(date_placing__range=[date1_placing,date2_placing]) &
            Q(term_execution__range=[date1_term,date2_term]) &
            Q(source_finance__icontains=source_finance)
        )
        return queryset

"""Факт"""
class FactsView(Filter, ListView):
    model = Fact
    queryset = Fact.objects.all()
    template_name = "report/fact_list.html"

def AddFact(request):
    error = ''
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid() & form.is_valid():
            form.save()
            return redirect('fact')
        else:
            error = 'Форма введена неправильно'

    form = FactForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'report/fact_add.html', data)

class FactDetailView(Filter, DetailView):
    model = Fact
    template_name = 'report/fact_detail.html'
    context_object_name = 'fact'

class FactUpdateView(UpdateView):
    model = Fact
    template_name = 'report/fact_add.html'
    form_class = FactForm

class FactDeleteView(DeleteView):
    model = Fact
    success_url = '/fact'
    template_name = 'report/fact_delete.html'

class FilterFactView(Filter, ListView):
    def get_queryset(self):
        date1_placing = self.request.GET.getlist("date1_placing")[0]
        date2_placing = self.request.GET.getlist("date2_placing")[0]
        date1_term = self.request.GET.getlist("date1_term")[0]
        date2_term = self.request.GET.getlist("date2_term")[0]
        source_finance = self.request.GET.getlist("source_filter")[0]

        kvr_itog = self.request.GET.getlist("kvr")
        if (kvr_itog == []):
            for kvr in Filter.get_kvr(self):
                kvr_itog.append(str(kvr.id))

        if (date1_placing == ''):
            date1_placing = "1000-01-01"
        if (date2_placing == ''):
            date2_placing = "3000-01-01"

        if (date1_term == ''):
            date1_term = "1000-01-01"
        if (date2_term == ''):
            date2_term = "3000-01-01"

        queryset = Fact.objects.filter(
            Q(kvr__in=kvr_itog) &
            Q(date_contract__range=[date1_placing,date2_placing]) &
            Q(term_execution__range=[date1_term,date2_term]) &
            Q(source_finance__icontains=source_finance)
        )
        return queryset


