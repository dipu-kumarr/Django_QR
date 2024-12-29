# myapp/urls.py
from django.urls import path
from .views import GetUserView, CreateQRUserLinkView, GetUserByQRIDView,SearchUserView

urlpatterns = [
    path('users', GetUserView.as_view(), name='get_user'),
    path('qr-users-link', CreateQRUserLinkView.as_view(), name='create_qr_user_link'),
    path('qr/<str:qr_unique_id>', GetUserByQRIDView.as_view(), name='get_user_by_qr_id'),
    path('search', SearchUserView.as_view(), name='search_user'),

]
