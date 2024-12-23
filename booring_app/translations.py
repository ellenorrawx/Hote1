from .models import Country, Hotel, Room
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name')

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('Hotel_name','hotel_description','city','address')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_descriptioncd')