from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('list/', views.OwnerList.as_view(), name='ownerlist'),
    path('register/', views.OwnerCreate.as_view(), name='ownercreate'),
    path('<pk>/update/', views.OwnerUpdate.as_view(), name='ownerupdate'),
    path('<pk>/delete/', views.OwnerDelete.as_view(), name='ownerdelete'),
]
