import graphene
from .models import FoodTruck
from django.db import models
from . import types



class Query(graphene.ObjectType):
    food_trucks = graphene.List(types.FoodTruckType, 
                                lat=graphene.Float(),
                                lon=graphene.Float(),
                                filters=graphene.Argument(types.FoodTruckFilter))

    def resolve_food_trucks(self, info, lat=None, lon=None,filters=None):
        queryset = FoodTruck.objects.all()
        
        # Apply filters based on status or facility type, if provided
        if filters:
            if filters.status:
                queryset = queryset.filter(status=filters.status.value)
            if filters.facility_type:
                queryset = queryset.filter(facilitytype=filters.facility_type.value)


        if lat is not None and lon is not None:
            queryset = queryset.annotate(
                distance=models.ExpressionWrapper(
                    FoodTruck.distance_to(lat, lon),
                    output_field=models.FloatField()
                )
            ).order_by('distance')[:5]

        return queryset


schema = graphene.Schema(query=Query)
