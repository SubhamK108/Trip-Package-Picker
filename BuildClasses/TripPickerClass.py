import random
import os
import json


class TripPicker:
    def __init__(self, destination, budget):
        self.Destination = destination
        self.Budget = budget
    
    def GetHotel(self):
        raw_data = open(r'AppDatabase/HotelDatabase.json', 'r')
        data = json.load(raw_data)
        for obj in data:
            if self.Destination.lower() == obj['Name']:
                Hotel = obj
                break
        try:
            random.seed(os.urandom(1024))
            SelectedHotel = random.choice(Hotel[str(self.Budget)])
        except:
            print('Sorry! {0} is currently not present in our database.'.format(self.Destination))
            print('System is shutting down...\n')
            exit()
        return SelectedHotel

    def GetPrice(self):
        raw_data = open(r'AppDatabase/PriceDatabase.json', 'r')
        data = json.load(raw_data)
        for obj in data:
            if self.Destination.lower() == obj['Name']:
                Price = obj
                break
        SelectedPrice = Price[str(self.Budget)]
        return SelectedPrice
    
    def GetPlaces(self):
        raw_data = open(r'AppDatabase/PlacesDatabase.json', 'r')
        data = json.load(raw_data)
        for obj in data:
            if self.Destination.lower() == obj['Name']:
                Places = obj
                break
        SelectedPlacess = ''
        for _places in Places[str(self.Budget)]:
            SelectedPlacess += _places + '\n'
        return SelectedPlacess
