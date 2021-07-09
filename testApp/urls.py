from django.urls import path,include
from . import views
from .views import TopView,SnsCreateView,SnsDeleteView,MySnsShowView,SnsCommentView,SnsCommentIndex

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('snscreate/', SnsCreateView.as_view(), name='snscreate'),
    path('snsdelete/<int:num>/', SnsDeleteView.as_view(), name='snsdelete'),
    path('mysnsshow/', MySnsShowView.as_view(), name='mysnsshow'),
    path('snscommentcreate/<int:num>/', SnsCommentView.as_view(), name='snscommentcreate'),
    path('snscommentindex/<int:num>/', SnsCommentIndex.as_view(), name='snscommentindex'),
]