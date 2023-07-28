from django.urls import path
from .views import AllCreateUserView,AllUserField,DetailUpdateDeleteUserView,UserBronViews,TimeFieldView

urlpatterns = [
    path("user/",AllCreateUserView.as_view()),
    path("bron/",UserBronViews.as_view()),
    path("seefield/",AllUserField.as_view()),
    path("user/<pk>/",DetailUpdateDeleteUserView.as_view()),
    path("notbron/<pk>/",TimeFieldView.as_view()),
]