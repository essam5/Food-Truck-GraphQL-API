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
   python -m venv venv
4.Activate the virtual environment:
  source venv/bin/activate
5.Install the required dependencies:
   pip install -r requirements.txt
   python manage.py migrate
6.Load the data from the CSV file using the custom Django management command
  python manage.py load_foodtrucks
7.Run the Server
  python manage.py runserver

The API will be available at http://localhost:8000/graphql/.
#Example Query:

    ```bash
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

The API will be available at http://localhost:8000/graphql/.

