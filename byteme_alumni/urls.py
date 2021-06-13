from django.contrib import admin
from django.urls import path
from users import views as users_view
from base import  views as base_view
from searching import views as search_view
from verification import views as ver_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_view.register,name="register"),
    path('', base_view.NoticeListView.as_view(),name="noticeboard"),
    path('profile/', users_view.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('notice/<int:pk>/', base_view.NoticeDetailView.as_view(), name='notice-detail'),
    path('notice/new/', base_view.NoticeCreateView.as_view(), name='notice-create'),
    path('notice/<int:pk>/update/', base_view.NoticeUpdateView.as_view(), name='notice-update'),
    path('notice/<int:pk>/delete/', base_view.NoticeDeleteView.as_view(), name='notice-delete'),
    path('notice/<int:pk>/delete/', base_view.NoticeDeleteView.as_view(), name='notice-delete'),
    path('verification/<int:pk>/detail', ver_view.detailview, name='user-detail-verify'),
    path('verification/', ver_view.userlist, name="verificationlist"),
    path('verification/<int:pk>/verify', ver_view.verify, name='verify'),
    path('verification/<int:pk>/reject', ver_view.reject, name='reject'),
    path('csearch/', search_view.CollegeSearchView.as_view(), name="csearch"),
    path('dsearch/', search_view.DirectorateSearchView.as_view(), name="dsearch"),
    path('alumni/<int:pk>/', search_view.UserDetailView.as_view(), name='user-detail'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
