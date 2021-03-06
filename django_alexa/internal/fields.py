'''These are the only fields supported by the Alexa skills kit'''
from __future__ import absolute_import


class Obj(object):
    def __init__(self, data):
        self.__dict__.update(data)


class AmazonSlots(object):
    '''Base for all amazon slots'''

    def create(self, validated_data):
        return Obj(data=validated_data)


class AmazonField(object):
    '''Base for all amazon fields'''
    amazon_name = None

    def get_slot_name(self):
        return self.amazon_name


class AmazonEvent(AmazonField):
    amazon_name = "AMAZON.EventType"


class AmazonDevice(AmazonField):
    amazon_name = "AMAZON.DeviceType"


class AmazonCustom(AmazonField):
    def get_choices(self):
        return []


class AmazonLiteral(AmazonField):
    amazon_name = "AMAZON.LITERAL"


class AmazonNumber(AmazonField):
    amazon_name = "AMAZON.NUMBER"


class AmazonDate(AmazonField):
    amazon_name = "AMAZON.DATE"


class AmazonTime(AmazonField):
    amazon_name = "AMAZON.TIME"


class AmazonDuration(AmazonField):
    amazon_name = "AMAZON.DURATION"


class AmazonUSCity(AmazonField):
    amazon_name = "AMAZON.US_CITY"


class AmazonFirstName(AmazonField):
    amazon_name = "AMAZON.US_FIRST_NAME"


class AmazonUSState(AmazonField):
    amazon_name = "AMAZON.US_STATE"


class AmazonFourDigitNumber(AmazonField):
    amazon_name = "AMAZON.FOUR_DIGIT_NUMBER"
