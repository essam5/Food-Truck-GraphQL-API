import graphene
from graphene_django.types import DjangoObjectType
from .models import FoodTruck
from .enums import StatusEnum, FacilityTypeEnum

class FoodTruckType(DjangoObjectType):
    class Meta:
        model = FoodTruck

class FoodTruckFilter(graphene.InputObjectType):
    status = StatusEnum()
    facility_type = FacilityTypeEnum()