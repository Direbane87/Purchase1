from django.urls import path

from . import views

urlpatterns = [
    path('plan/', views.PlansView.as_view(), name='plan'),
    path('fact/', views.FactsView.as_view(), name='fact'),

    path('kvr/', views.Spr1View.as_view(), name='spr1'),
    path('spr2/', views.Spr2View.as_view(), name='spr2'),
    path('spr3/', views.Spr3View.as_view(), name='spr3'),
    path('spr4/', views.Spr4View.as_view(), name='spr4'),
    path('spr5/', views.Spr5View.as_view(), name='spr5'),
    path('spr6/', views.Spr6View.as_view(), name='spr6'),
    path('spr7/', views.Spr7View.as_view(), name='spr7'),
    path('spr8/', views.Spr8View.as_view(), name='spr8'),

    path('pay/', views.FactPayView.as_view(), name='pay'),
    path('pay/add/', views.AddFactPay, name='pay_add'),
    path('pay/<int:pk>', views.FactPayDetailView.as_view(), name='pay_detail'),
    path('pay/<int:pk>/update', views.FactPayUpdateView.as_view(), name='pay_update'),
    path('pay/<int:pk>/delete', views.FactPayDeleteView.as_view(), name='pay_delete'),
    path('pay/filter/', views.FilterPayView.as_view(), name='pay_filter'),
    path('pay/export/', views.export, name='export'),

    path('plan/add/', views.AddPlan, name='plan_add'),
    path('plan/<int:pk>', views.PlanDetailView.as_view(), name='plan_detail'),
    path('plan/<int:pk>/update', views.PlanUpdateView.as_view(), name='plan_update'),
    path('plan/<int:pk>/delete', views.PlanDeleteView.as_view(), name='plan_delete'),
    path('plan/filter/', views.FilterPlanView.as_view(), name='plan_filter'),

    path('fact/add/', views.AddFact, name='fact_add'),
    path('fact/<int:pk>', views.FactDetailView.as_view(), name='fact_detail'),
    path('fact/<int:pk>/update', views.FactUpdateView.as_view(), name='fact_update'),
    path('fact/<int:pk>/delete', views.FactDeleteView.as_view(), name='fact_delete'),
    path('fact/filter/', views.FilterFactView.as_view(), name='fact_filter'),
]