from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='carmake model')
    description = models.CharField(max_length=500)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description


# Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    carmaker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    description = models.TextField()
    car_name = models.CharField(null=False, max_length=90, default='Unknown Car Name')
    dealer_id = models.CharField(max_length=100)
    SEDAN = 'Sedan'
    SUV = 'SUV'
    HATCHBACK = 'Hatchback'
    CROSSOVER = 'Crossover'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (HATCHBACK, 'Hatchback'),
        (CROSSOVER, 'Crossover')
    ]
    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    stocked_date = models.DateField(default=now)
    def __str__(self):
        return "Car Title: " + self.car_name + ", " + \
                "Description: " + self.description + ", " \
                "Car Maker: " + self.carmaker + ", " + \
                "Car Type: " + self.car_type + ", " + \
                "Stocked date: " + self.stocked_date

# Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Ddealership
        self.dealership = dealership
        # Reviewer name
        self.name = name
        # Reviewer purchase
        self.purchase = purchase
        # Review id
        self.reviewid = reviewid
        # Purchase Date
        self.purchase_date = purchase_date
        # car_make
        self.car_make = car_make
        # car_model
        self.car_model = car_model
        # car_year
        self.car_year = car_year
        # sentiment
        self.sentiment = sentiment
        # id
        self.id = id
        
    def __str__(self):
        return "Dealer name: " + self.full_name