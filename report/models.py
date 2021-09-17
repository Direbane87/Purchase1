from django.db import models
from datetime import date

class Spr1_kvr(models.Model):
    """КВР"""
    kvr = models.PositiveSmallIntegerField("КВР")
    analytical_code = models.CharField("Анал.код", max_length=10)
    name = models.CharField("Наименование", max_length=150)

    def __str__(self):
        return str(self.kvr) + ' ' + self.analytical_code + ' ' + self.name

    class Meta:
        verbose_name = "Справочник 1 (КВР)"
        verbose_name_plural = "Справочник 1 (КВР)"

class Spr2_okved2(models.Model):
    """"ОКВЕД2"""
    section = models.CharField("Раздел", max_length=20)
    description = models.TextField("Наименование")
    parent = models.CharField("Родитель", max_length=20)

    def __str__(self):
        return self.section + ' ' + self.description

    class Meta:
        verbose_name = "Справочник 2 (ОКВЕД2)"
        verbose_name_plural = "Справочник 2 (ОКВЕД2)"

class Spr3_okpd2(models.Model):
    """"ОКПД2"""
    section = models.CharField("Раздел", max_length=20)
    description = models.TextField("Наименование")
    parent = models.CharField("Родитель", max_length=20)

    def __str__(self):
        return self.section + ' ' + self.description

    class Meta:
        verbose_name = "Справочник 3 (ОКПД2)"
        verbose_name_plural = "Справочник 3 (ОКПД2)"

class Spr4_requirements(models.Model):
    """"Мин. требования"""
    name = models.CharField("Наименование", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Справочник 4 (требования)"
        verbose_name_plural = "Справочник 4 (требования)"

class Spr5_unit(models.Model):
    """Единица измерения"""
    code = models.PositiveSmallIntegerField("Код")
    name = models.CharField("Наименование", max_length=25)

    def __str__(self):
        return str(self.code) + '-' + self.name

    class Meta:
        verbose_name = "Справочник 5 (единица измерения)"
        verbose_name_plural = "Справочник 5 (единица измерения)"

class Spr6_region(models.Model):
    """"Регион поставки"""
    code = models.CharField("Код региона", max_length=15)
    name = models.CharField("Наименование", max_length=25)

    def __str__(self):
        return self.code + '-' + self.name

    class Meta:
        verbose_name = "Справочник 6 (Регион поставки)"
        verbose_name_plural = "Справочник 6 (Регион поставки)"

class Spr7_method(models.Model):
    method = models.CharField("Способ", max_length=150)
    point = models.CharField("Пункт", max_length=15)

    def __str__(self):
        return self.method + '-' + self.point

    class Meta:
        verbose_name = "Справочник 7 (способ закупки)"
        verbose_name_plural = "Справочник 7 (способ закупки)"

class Spr8_result(models.Model):
    name = models.CharField("Результат", max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Справочник 8 (результат)"
        verbose_name_plural = "Справочник 8 (результат)"

class Plan(models.Model):
    kvr = models.ForeignKey(Spr1_kvr, verbose_name="КВР", on_delete=models.SET_NULL, null=True)
    okved2 = models.ForeignKey(Spr2_okved2, verbose_name="ОКВЕД2", on_delete=models.SET_NULL, null=True)
    okpd2 = models.ForeignKey(Spr3_okpd2, verbose_name="ОКПД2", on_delete=models.SET_NULL, null=True)
    name_contract = models.TextField("Предмет договора")
    min_req = models.ForeignKey(Spr4_requirements, verbose_name="Мин. требования", on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Spr5_unit, verbose_name="Единица измерения", on_delete=models.SET_NULL, null=True)
    info_quantity = models.PositiveIntegerField("Сведения о количестве", default=0)
    region = models.ForeignKey(Spr6_region, verbose_name="Регион", on_delete=models.SET_NULL, null=True)
    info_start_price = models.PositiveIntegerField("Начальная цена",default=0)
    g2021 = models.PositiveIntegerField("2021", default=0)
    g2022 = models.PositiveIntegerField("2022", default=0)
    g2023 = models.PositiveIntegerField("2023", default=0)
    g2024 = models.PositiveIntegerField("2024", default=0)
    next = models.PositiveIntegerField("Последующие", default=0)
    date_placing = models.DateField("Дата размещения", default=date.today)
    term_execution = models.DateField("Срок размещения", default=date.today)
    method = models.ForeignKey(Spr7_method, verbose_name="Способ", on_delete=models.SET_NULL, null=True)
    electronic_form = models.BooleanField(default=False)
    smp = models.BooleanField(default=False)
    source_finance = models.CharField("Источник финансирования", max_length=40)
    executor_human = models.CharField("Отв. исполнитель", max_length=150)
    result = models.ForeignKey(Spr8_result, verbose_name="Результат", on_delete=models.SET_NULL, null=True)
    executor = models.CharField("Испольнитель", max_length=255)
    number_contract = models.CharField("Номер договора", max_length=100)

    def __str__(self):
        return str(self.kvr)

    def get_absolute_url(self):
        return f'/plan/'

    class Meta:
        verbose_name = "План"
        verbose_name_plural = "План"

class Fact(models.Model):
    kvr = models.ForeignKey(Spr1_kvr, verbose_name="КВР", on_delete=models.SET_NULL, null=True)
    name_contract = models.TextField("Предмет договора", null=True)
    source_finance = models.CharField("Источник финансирования", max_length=40, null=True)
    executor = models.CharField("Испольнитель", max_length=255, null=True)
    number_contract = models.CharField("Номер договора", max_length=100, null=True)
    date_contract = models.DateField("Дата договора", default=date.today)
    term_execution = models.DateField("Срок исполнения", default=date.today)
    add_agreement = models.CharField("Дополнительное соглашение", max_length=255, null=True)
    fact_price = models.PositiveIntegerField("Фактическая сумма", default=0)
    fact_price1 = models.PositiveIntegerField("Фактическая сумма 1 год", default=0)
    fact_price2 = models.PositiveIntegerField("Фактическая сумма 2 год", default=0)
    fact_price3 = models.PositiveIntegerField("Фактическая сумма 3 год", default=0)
    fact_price4 = models.PositiveIntegerField("Фактическая сумма 4 год", default=0)
    fact_next = models.PositiveIntegerField("Фактическая сумма последующие года", default=0)
    payment_year1 = models.PositiveIntegerField("Оплата 1 год", default=0)
    payment_year2 = models.PositiveIntegerField("Оплата 2 год", default=0)
    payment_year3 = models.PositiveIntegerField("Оплата 3 год", default=0)
    payment_year4 = models.PositiveIntegerField("Оплата 4 год", default=0)
    payment_next = models.PositiveIntegerField("Оплата последующие года", default=0)
    consignment_note = models.CharField("Товарная накладная", max_length=255, null=True)
    payment_order = models.CharField("Платежное поручение", max_length=255, null=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return f'/fact/'

    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факт"

class Fact_pay(models.Model):
    amount = models.PositiveIntegerField("Сумма", default=0)
    year = models.CharField("Год", max_length=25)
    consignment_note = models.CharField("Товарная накладная", max_length=255, null=True)
    payment_order = models.CharField("Платежное поручение", max_length=255, null=True)
    id_fact = models.ForeignKey(Fact, verbose_name="Факт", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.amount) + ' ' + self.consignment_note + ' ' + self.payment_order

    def get_absolute_url(self):
        return f'/pay/'

    class Meta:
        verbose_name = "Оплата по годам"
        verbose_name_plural = "Оплата по годам"