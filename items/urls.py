from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from items import views

urlpatterns =format_suffix_patterns( [

    path('<int:id>/items/all',views.item_list,name='item-list'),
    path('item/<int:pk2>',views.item_detail,name='item'),
    path('login/',views.login),
    path('signup',views.signup),
 
])
