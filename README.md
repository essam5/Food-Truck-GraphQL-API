# Food-Truck-GraphQL-API

This API provides information about food trucks based on geographical coordinates to get
at least 5 food trucks to choose from a particular latitude and longitude
and allows filtering by status (APPROVED,REQUESTED,SUSPEND,EXPIRED) and facility type (Push Cart, Truck).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/food-truck-graphql-api.git
2. cd food-truck-graphql-api
3. Create a virtual environment:
   ```bash
   python -m venv venv

5. Activate the virtual environment:
   ```bash
   source venv/bin/activate

7. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   python manage.py migrate

8. Load the data from the CSV file using the custom Django management command
    ```bash
    python manage.py load_foodtrucks

10. Run the Server
   ```bash
   python manage.py runserver
```
The API will be available at http://localhost:8000/graphql/.

#Example Query:

    
    query foodTrucks{
      foodTrucks(lat:37.712302604744416, 
        lon:-122.43164419037294
        filters:{
          status:REQUESTED
          facilityType: TRUCK
        }
      )
      {
        locationid
        latitude
        longitude
        location
        facilitytype
        status    
        address
      }
      
    }

### New Feature 
Haversine Distance Calculation:

The distance_to method in the FoodTruck model calculates the distance between a given latitude and longitude using the Haversine formula. This method enhances the API's ability to filter food trucks based on geographical proximity.

reference: https://en.wikipedia.org/wiki/Haversine_formula , https://docs.djangoproject.com/en/3.2/ref/models/expressions/#func-expressions 

