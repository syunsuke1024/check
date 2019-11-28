from django.urls import path
from . import views

app_name = "boxlinks"

urlpatterns = [
    path('',views.LinksListView.as_view(),name='boxlinks_list'),
    path('boxlinks_create/',views.LinksCreateView.as_view(),name="boxlinks_create"),
    path('boxlinks_update/<int:pk>',views.LinksUpdateView.as_view(),name="boxlinks_update"),
    path('boxlinks_delete/<int:pk>',views.LinksDeleteView.as_view(),name="boxlinks_delete"),
]