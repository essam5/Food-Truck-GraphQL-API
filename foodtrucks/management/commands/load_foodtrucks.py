import csv
from django.core.management.base import BaseCommand
from foodtrucks.models import FoodTruck
from django.db import models
from datetime import datetime
import re

pattern = re.compile(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} [APMapm]{2}$')

class Command(BaseCommand):
    help = 'Load food trucks from CSV'

    def handle(self, *args, **kwargs):
        
        # Clear existing data
        FoodTruck.objects.all().delete()

        # Load data from CSV
        file_path ='/home/dell/projects/RAKT-task/foodtruck_project/foodtrucks/management/commands/food-truck-data.csv' 
       
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Create a dictionary to store the field-value pairs
                truck_data = {}
                
                # Loop through columns in the CSV and map them to model fields
                for column_name, value in row.items():
                    # Convert column name to lowercase and replace spaces with underscores
                    field_name = column_name.lower().replace(' ', '_')
                    print(field_name, value)
                    
                    # Check if the field name exists in the model
                    if hasattr(FoodTruck, field_name):
                        # Assign the value to the corresponding field
                        truck_data[field_name] = value

                # Create a new FoodTruck object with the mapped data and save it
                FoodTruck.objects.create(**truck_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded food trucks'))
