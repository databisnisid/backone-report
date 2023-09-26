from wagtail.admin.ui.components import Component
from problems.models import Problems
from companies.models import Companies
from customers.models import Customers
from links.models import Links
from reasons.models import Reasons
from resolutions.models import Resolutions


def get_chart_data_problem(model_name):
    chart_data = []
    total_problems = Problems.objects.count()
    objects = model_name.objects.all()

    total_problems_objects = 0
    for obj in objects:
        total_per_object = Problems.objects.filter(
                tags__icontains=obj.tag
                ).count()
        data = {
                'name': obj.name,
                'count': total_per_object
                }
        chart_data.append(data)
        total_problems_objects += total_per_object

    if total_problems_objects < total_problems:
        data = {
                'name': 'unknown',
                'count': total_problems - total_problems_objects
                }
        chart_data.append(data)

    return chart_data



class CheckCompaniesChart(Component):
    order = 10
    template_name = 'dashboard/chart_companies.html'

    def __init__(self):
        self.model_name = Companies
        self.chart_title = 'Problems Per Company'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['chart_data'] = get_chart_data_problem(self.model_name)
        context['chart_title'] = self.chart_title

        return context


class CheckCustomersChart(Component):
    order = 10
    template_name = 'dashboard/chart_customers.html'

    def __init__(self):
        self.model_name = Customers
        self.chart_title = 'Problems Per Customer'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['chart_data'] = get_chart_data_problem(self.model_name)
        context['chart_title'] = self.chart_title

        return context


class CheckLinksChart(Component):
    order = 10
    template_name = 'dashboard/chart_links.html'

    def __init__(self):
        self.model_name = Links
        self.chart_title = 'Problems Per Links'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['chart_data'] = get_chart_data_problem(self.model_name)
        context['chart_title'] = self.chart_title

        return context


class CheckReasonsChart(Component):
    order = 10
    template_name = 'dashboard/chart_reasons.html'

    def __init__(self):
        self.model_name = Reasons
        self.chart_title = 'Problems Per Reason'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['chart_data'] = get_chart_data_problem(self.model_name)
        context['chart_title'] = self.chart_title

        return context


class CheckResolutionsChart(Component):
    order = 10
    template_name = 'dashboard/chart_resolutions.html'

    def __init__(self):
        self.model_name = Reasons
        self.chart_title = 'Problems Per Resolution'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['chart_data'] = get_chart_data_problem(self.model_name)
        context['chart_title'] = self.chart_title

        return context
