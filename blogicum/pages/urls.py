from django.urls import path
# from django.views.generic import TemplateView

from pages import views

app_name = 'pages'

urlpatterns = [
    # Автотесты не пропускают решение :(
    # path('about/', TemplateView.as_view(template_name="pages/about.html")),
    # path('rules/', TemplateView.as_view(template_name="pages/rules.html")),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
