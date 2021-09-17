from import_export import resources
from .models import Fact_pay

class FactPayResource(resources.ModelResource):
    class Meta:
        model = Fact_pay