from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from Expense_App import views as app_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='user_register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('',include('Expense_App.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('add/',app_views.add,name='add_expenses'),
    path('expenses/',app_views.expenses,name='expenses'),
    path('delete/<int:id_value>',app_views.delete_expenses,name='delete_expenses'),
    path('filter/',app_views.filter_expenses,name='filter_expenses'),
    path('view/<int:value>',app_views.view_expenses,name='view_expense'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)