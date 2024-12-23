from collections import namedtuple
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns =[
    path('urls/', include(router.urls)),
    path('', HotelListApiView.as_view(), name='hotels_list'),
    path('<int:pk>/', HotelDetailApiView.as_view(), name='Hotels_detail'),
    path('rooms/', RoomListApiView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailApiView.as_view(), name='room_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_List'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('user/', UserProfileListApiView.as_view(), name='user_List'),
    path('user/<int:pk>/', UserProfileDetailApiView.as_view(), name='user_detail'),
    path('hotel/create/',HotelDetailApiView.as_view(),name = 'hotel_create'),
    path('hotel/<int:pk>/',HotelLEDITAPIVIEW.as_view(),name = 'hotel_edit')

]
