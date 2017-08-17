from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^brands/$', views.BrandList.as_view(),name='brands_list'),
    url(r'^brands/(?P<slug>\w+)/$', views.brandDetail,name='brand_details'),
    url(r'^clothing/$', views.ClothingList.as_view(),name='clothing_list'),
    url(r'clothing/(?P<category>\w+)/$', views.ClothingListWithCategory,name='clothing_list_with_category')
]
