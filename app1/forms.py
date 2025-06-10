from django import forms 
from .models import Housedata
class HousedataForm(forms.ModelForm):
    class Meta:
        model=Housedata
        fields=('MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude')
        labels = {
            'MedInc': '	Median Income ',
            'HouseAge': 'House Age (in years)',
            'AveRooms': 'Average Number of Rooms',
            'AveBedrms': 'Average Number of Bedrooms',
            'Population':'Population',
            'AveOccup':'Average Occupancy per Household',
            'Latitude':'Latitude (Geographic)',
            'Longitude':'Longitude (Geographic)'
        }
      
           