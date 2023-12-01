from django.urls import path
from . import views
app_name = 'snsapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.CreateSnsappView.as_view(), name='post'),
    path('post_done/',views.PostSuccessView.as_view(), name='post_done'),
    path('snsapp/<int:category>',views.CategoryView.as_view(), name='post_cat'),
    path('user-list/<int:user>',views.UserView.as_view(), name='user_list'),
    path('post-detail/<int:pk>',views.DetailView.as_view(), name='post_detail'),
    path('mypage/',views.MypageView.as_view(), name='mypage'),
    path('snsapp/<int:pk>/delete/',views.SnsappDeleteView.as_view(), name='post_delete'),
    path('contact/',views.ContactView.as_view(),name='contact'),
]