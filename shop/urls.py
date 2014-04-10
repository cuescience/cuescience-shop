from shop.views.cart_views import CheckoutWizard
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', "shop.views.shop_views.index_view",
                           name="index"),
                       url(r'^cart/$', "shop.views.cart_views.index_view",
                           name="cart_index"),
                       url(r'^cart/add/(?P<product_id>\d+)/$', "shop.views.cart_views.add_view",
                           name="cart_add"),
                       url(r'^cart/remove/(?P<product_id>\d+)/$', "shop.views.cart_views.remove_view",
                           name="cart_remove"),
                       url(r'^cart/update/$', "shop.views.cart_views.update_view",
                           name="cart_update"),
                       url(r'^cart/checkout/$', CheckoutWizard.as_view(),
                           name="cart_checkout"),

)
