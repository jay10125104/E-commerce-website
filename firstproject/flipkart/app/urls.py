from .forms import LoginFrom,Mypasswordchange,MyPasswordResetForm
from django.urls import path
from app import views
from django.views import View
# for images
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('logout/', views.logoutuser, name='logout'),
    path('passwordchanged/', views.passwordchaged, name='passwordchanged'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=Mypasswordchange , success_url='/passwordchanged/'),name='passwordchange'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('laptop/', views.laptop, name='laptop'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form = LoginFrom ),name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uid64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'),name='password_reset_confirm'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# setting up this static files.
