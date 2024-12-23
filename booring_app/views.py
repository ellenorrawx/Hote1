from rest_framework import viewsets,generics
from tutorial.quickstart.serializers import UserSerializer
from .models import *
from .serializers import *
from .permissions import CheckUserCreate, CheckReview, CheckReviewEDIT


class UserProfileListApiView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer



    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer
    permission_classes = [CheckUserCreate]


    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CountryListAPIView(generics.ListAPIView):
    queryset =Country.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class =CountryDetailSerializer


class HotelListApiView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

class HotelCreateAPIView(generics.ListAPIView):
    serializer_class = HotelSerializers
    permission_classes = [CheckUserCreate]

class HotelLEDITAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    permission_classes = [CheckUserCreate]


class HotelDetailApiView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


class RoomListApiView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

class RoomDetailApiView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class =ReviewSerializers
    permission_classes = [CheckReview,CheckReviewEDIT]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class =BookingSerializer