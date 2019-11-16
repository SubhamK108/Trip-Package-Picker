import random
import os
import json


class TripManager:
    def __init__(self, destination, budget):
        self.Destination = destination
        self.Budget = budget

    def GetHotel(self):
        for dictionary in THD.TripHotel:
            if self.Destination.lower() == dictionary['Name']:
                Hotel = dictionary
                break
        try:
            random.seed(os.urandom(1024))
            SelectedHotel = random.choice(Hotel[self.Budget])
        except:
            print('Sorry! {0} is currently not present in our database.'.format(self.Destination))
            print('System is shutting down...\n')
            exit()
        return SelectedHotel
    
    def GetPrice(self):
        for dictionary in TPD.TripPrice:
            if self.Destination.lower() == dictionary['Name']:
                Price = dictionary
                break
        SelectedPrice = Price[self.Budget]
        return SelectedPrice

    def GetPlaces(self):
        for dictionary in TPCSD.TripPlaces:
            if self.Destination.lower() == dictionary['Name']:
                Places = dictionary
                break
        SelectedPlacess = ''
        for _places in Places[self.Budget]:
            SelectedPlacess += _places + '\n'
        return SelectedPlacess
