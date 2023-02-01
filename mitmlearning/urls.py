from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('scenario', views.scenario, name='scenario'),
    path('feedback', views.feedback, name='feedback'),
    path('term', views.term_view, name='list-term'),
    path('term/<int:pk>/detail/', views.DetailTermView.as_view(), name='detail-term'),
    path('term/create/', views.CreateTermView.as_view(), name='create-term'),
    path('term/<int:pk>/delete/', views.DeleteTermView.as_view(), name='delete-term'),
    path('term/<int:pk>/update/', views.UpdateTermView.as_view(), name='update-term'),
    path('term/<str:category>/', views.CategoryView.as_view(), name='category'),
    # 画面なし 機能だけ
    path('sslstrip', views.sslstrip, name='sslstrip'),
    path('dnsspoof', views.dns_spoof, name='dnsspoof'),
    path('stop_attack', views.stop_attack, name='stop_attack'),
    path('password', views.scenario_download_password, name='scenario_download_password'),
    path('credential', views.scenario_download_credential, name='scenario_download_credential'),
    path('feedback/send_impersonation_email', views.send_impersonation_email, name='send_impersonation_email'),
    path('term/send_countermeasure_email', views.send_countermeasure_email, name='send_countermeasure_email'),
    # path('auto_login', views.auto_login, name='auto_login'),
    # path('example_auto_login', views.example_auto_login, name='example_auto_login'),
]