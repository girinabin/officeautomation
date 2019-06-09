from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name="home"),
    path('addrequest/',views.add_requestView.as_view(),name="addrequest"),
    path('leaverequest/',views.leave_requestView.as_view(),name="leaverequest"),
    path('booking/',views.BookingView.as_view(),name="booking"),
    path('snacks/',views.SnacksView.as_view(),name="snacks"),
]
