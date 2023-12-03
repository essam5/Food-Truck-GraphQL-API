from django.db import models
from django.db.models import F, Func

# note: Am not sticking with the naming convention to just the model fields be compatible with csv 

    
class FoodTruck(models.Model):
    STATUS = (
    ("APPROVED", "APPROVED"),
    ("REQUESTED", "REQUESTED"),
    ("SUSPEND", "SUSPEND"),
    ("EXPIRED", "EXPIRED"),  
    )
    
    FACILITY_TYPE = (
    ("Push Cart", "Push Cart"),
    ("Truck", "Truck"), 
    )
    
    locationid = models.IntegerField()
    applicant = models.CharField(max_length=255)
    facilitytype = models.CharField(max_length=9,choices=FACILITY_TYPE,default="Truck",blank=True, null=True)
    cnn = models.IntegerField()
    locationdescription = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    blocklot = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    permit = models.CharField(max_length=255)
    status = models.CharField(max_length=9,choices=STATUS,default="REQUESTED")
    fooditems = models.CharField(max_length=255)
    x = models.CharField(max_length=255,blank=True, null=True)
    y = models.CharField(max_length=255,blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    schedule = models.URLField(blank=True, null=True)
    dayshours = models.CharField(max_length=255, blank=True, null=True)
    noisent = models.CharField(max_length=255,blank=True, null=True)
    approved = models.CharField(max_length=255,blank=True, null=True)
    received = models.CharField(max_length=255,blank=True, null=True)
    priorpermit = models.CharField(max_length=255, blank=True, null=True)
    expirationdate = models.CharField(max_length=255,blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    fire_prevention_districts = models.CharField(max_length=255,blank=True, null=True)  
    police_districts = models.CharField(max_length=255,blank=True, null=True)
    supervisor_districts = models.CharField(max_length=255,blank=True, null=True)
    zip_codes = models.CharField(max_length=255,blank=True, null=True)  
    neighborhoods_old = models.CharField(max_length=255,blank=True, null=True) 
    

    def __str__(self):
        return f"{self.locationid} - {self.applicant}"
    
    @staticmethod
    def haversine_distance(lat_diff, lon_diff):
        
        # Haversine formula
        haversine_formula = (
            Func(lat_diff / 2, function='SIN') ** 2 +
            Func((F('longitude') - lon_diff) / 2, function='SIN') *
            Func(F('latitude'), function='COS') * Func(F('latitude'), function='COS') *
            Func(lon_diff / 2, function='SIN') ** 2
        )

        haversine_distance = 2 * 6371 * (
            haversine_formula ** 0.5
        )        
        
        return haversine_distance

    @staticmethod
    def distance_to(lat, lon):
        lat_diff = F('latitude') - lat
        lon_diff = F('longitude') - lon

        distance_expr = FoodTruck.haversine_distance(lat_diff, lon_diff)

        return distance_expr