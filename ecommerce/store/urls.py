from django.urls import path
from . import views
from . views import CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("login/",CustomLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page='login'),name="logout"),
    path("register/",RegisterPage.as_view(),name="register"),



    path("",views.store,name="store"),
    path("cart/",views.cart,name="cart"),
    path("checkout/",views.checkout,name="checkout"),
    path("update_item/",views.updateItem,name="update_item"),
    path("process_order/",views.processOrder,name="process_order"),
]
