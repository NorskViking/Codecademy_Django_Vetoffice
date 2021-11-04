from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('owner/list/', views.OwnerList.as_view(), name='ownerlist'),
    path('owner/register/', views.OwnerCreate.as_view(), name='ownercreate'),
    path('owner/<pk>/update/', views.OwnerUpdate.as_view(), name='ownerupdate'),
    path('owner/<pk>/delete/', views.OwnerDelete.as_view(), name='ownerdelete'),
]
