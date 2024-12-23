from rest_framework import serializers
from .models import *



class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumberField
        fields = ['hotels_image']



class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields =['room_image']

class ReviewSerializers(serializers.ModelSerializer):
    user_name = UserProfileSimpleSerializers
    class Meta:
        model = Review
        fields =['text','stars','user_name','hotel','parent']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many = True,read_only = True )
    class Meta:
        model = Room
        fields =['id','room_number','room_type','room_images','room_status','room_price']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many = True,read_only = True )

    class Meta:
        model = Room
        fields =['id','room_number','room_type','room_status','room_price',
                 'all_inclusive','room_description']


class HotelListSerializer(serializers.ModelSerializer):
    hotel = HotelImageSerializers(many = True, read_only = True)
    class Meta:
        model = Hotel
        fields =['id','hotel_name', 'hotel', 'address','stars']


class CountryDetailSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many = True, read_only = True)
    class Meta:
        model = Country
        fields = ['id','country_name','hotels']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel = HotelImageSerializers(many = True, read_only = True)
    country = CountryListSerializer
    owner = UserProfileSimpleSerializers()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    rooms =RoomListSerializer(many=True,read_only=True)
    reviews = ReviewSerializers(many=True,read_only=True)
    class Meta:
        model = Hotel
        fields =['hotel_name','description','country', 'stars',
                 'city','address','hotel','hotel_video','created_date','owner','rooms', 'reviews','hotels']

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = []