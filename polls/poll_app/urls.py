# from django.urls import path
# from . import views
#
# app_name = 'poll_app' # This is namespacing  url for this particular app.This allows django to be able to identify this better when there are plenty apps.
#
# urlpatterns = [
#     # path('', views.index_1, name='index_1'),
#     path('', views.index, name='index'),
#     path('specifics/<int:question_id>/',views.detail, name='detail'),
#     # path('<int:question_id>/',views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


# Amended URLconf: using generic view

from django.urls import path
from . import views

app_name = 'poll_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]