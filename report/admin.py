from django.contrib import admin

from .models import Fact_pay, Fact, Spr1_kvr, Spr2_okved2, Spr3_okpd2, Spr4_requirements, Spr5_unit, Spr6_region, Spr7_method, Spr8_result, Plan

admin.site.register(Spr1_kvr)
admin.site.register(Spr2_okved2)
admin.site.register(Spr3_okpd2)
admin.site.register(Spr4_requirements)
admin.site.register(Spr5_unit)
admin.site.register(Spr6_region)
admin.site.register(Spr7_method)
admin.site.register(Spr8_result)
admin.site.register(Plan)
admin.site.register(Fact)
admin.site.register(Fact_pay)

