from .models import Plan, Fact, Fact_pay
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, NumberInput, NullBooleanSelect, CheckboxInput

class FactPayForm(ModelForm):
    class Meta:
        model = Fact_pay

        fields = ['amount', 'year', 'consignment_note', 'payment_order', 'id_fact']

        widgets = {
            "amount":NumberInput(attrs={
                'class': 'form-control',
            }),
            "year": TextInput(attrs={
                'class': 'form-control',
            }),
            "consignment_note": TextInput(attrs={
                'class': 'form-control',
            }),
            "payment_order": TextInput(attrs={
                'class': 'form-control',
            }),
            "id_fact": Select(attrs={
                'class': 'form-control',
                'placeholder': "Мин. требования"
            }),
        }

class FactForm(ModelForm):
    class Meta:
        model = Fact

        fields = ['kvr', 'name_contract', 'source_finance', 'executor', 'number_contract',
                  'date_contract', 'term_execution', 'add_agreement',
                  'fact_price', 'fact_price1', 'fact_price2', 'fact_price3', 'fact_price4', 'fact_next', 'payment_year1',
                  'payment_year2', 'payment_year3', 'payment_year4', 'payment_next', 'consignment_note',
                  'payment_order']

        widgets = {
            "kvr": Select(attrs={
                'class': 'form-control',
                'placeholder': "КВР",
            }),
            "name_contract": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Предмет договора"
            }),
            "source_finance": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Мин. требования"
            }),
            "executor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "number_contract": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "date_contract": DateTimeInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "term_execution": DateTimeInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "add_agreement": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "fact_price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "fact_price1": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "fact_price2": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "fact_price3": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "fact_price4": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения",
            }),
            "fact_next": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "payment_year1": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "payment_year2": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "payment_year3": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "payment_year4": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "payment_next": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "consignment_note": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "payment_order": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
        }


class PlanForm(ModelForm):
    class Meta:
        model = Plan

        fields = ['kvr', 'okved2', 'okpd2', 'name_contract', 'min_req', 'unit', 'info_quantity', 'region',
                  'info_start_price', 'g2021', 'g2022', 'g2023', 'g2024', 'next', 'date_placing', 'term_execution',
                  'method', 'electronic_form', 'smp', 'source_finance', 'executor_human', 'result', 'executor', 'number_contract']

        widgets = {
            "kvr" : Select(attrs={
                'class': 'form-control',
                'placeholder': "КВР",
            }),
            "okved2": Select(attrs={
                'class': 'form-control',
                'placeholder': "ОКВЕД2",
            }),
            "okpd2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "ОКПД2"
            }),
            "name_contract": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Предмет договора"
            }),
            "min_req": Select(attrs={
                'class': 'form-control',
                'placeholder': "Мин. требования"
            }),
            "unit": Select(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "info_quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "region": Select(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "info_start_price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "g2021": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "g2022": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "g2023": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "g2024": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "next": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "date_placing": DateTimeInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Единица измерения",
            }),
            "term_execution": DateTimeInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "method": Select(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "electronic_form": NullBooleanSelect(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "smp": NullBooleanSelect(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "source_finance": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "executor_human": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "result": Select(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "executor": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
            "number_contract": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Единица измерения"
            }),
        }