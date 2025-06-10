from django.shortcuts import render

from .forms import HousedataForm
from django.shortcuts import render
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor


def home(request):
    if request.method=='POST':
       
        form=HousedataForm(request.POST)
        if form.is_valid():
            MedInc = form.cleaned_data['MedInc']
            HouseAge = form.cleaned_data['HouseAge']
            AveRooms = form.cleaned_data['AveRooms']
            AveBedrms = form.cleaned_data['AveBedrms']
            Population = form.cleaned_data['Population']
            AveOccup = form.cleaned_data['AveOccup']
            Latitude = form.cleaned_data['Latitude']
            Longitude = form.cleaned_data['Longitude']
            df = pd.read_csv('data.csv')
            x = df[['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']]
            y = df['target']
            model = DecisionTreeRegressor()  # <-- Changed here
            model.fit(x, y)


            prediction = model.predict([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]])
            prediction_value = round(prediction[0], 2) 
            #prediction=12345.6
            return render(request, 'result.html', {'prediction': prediction_value})
       
    else:
            form=HousedataForm()
    form=HousedataForm()
    return render(request, 'home.html', {'form': form})



