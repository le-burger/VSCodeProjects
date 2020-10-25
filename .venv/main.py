import pandas as pd

BezoekersAantallen = ('df1')
Horeca_en_Winkel_omzet = ('df2')

df1 = pd.read_excel (r"/Users/ebosma/Documents/E + E /Studie/HvA/Programming - Opdrachten/PandasTest/Museum gegevens 2019.xlsx","Bezoekers aantallen")
df2 = pd.read_excel (r"/Users/ebosma/Documents/E + E /Studie/HvA/Programming - Opdrachten/PandasTest/Museum gegevens 2019.xlsx","Horeca en Winkelomzet")

# Om wat ruimte te creeren tussen de diverse overzichten
def layout():
    print('= = = = = = = = = = = = = = = = = = = = =')
def layout2():
    print('                                          ')

pivot = df1.groupby(['Museumtype']).mean()
OverzichtAantalBezoekers = pivot.loc[:,"Museumjaarkaart":"Totaal"]
layout()
layout2()

print ('Overzicht van de diverse musea en hun bezoers in 2019')
print (OverzichtAantalBezoekers)


#Percentage Museumjaarkaart per museum tov het Totaal]
layout()
layout2()
BezoekersPercentage_per_Museum1 = (df1 ['Museumjaarkaart'].values / df1 ['Totaal'].values).round(3) * 100
print ('Percentage Museumjaarkaart bezoekers per museum')

print (df1 ['Museumtype'].values.tolist()

print (BezoekersPercentage_per_Museum1)

layout()
layout2()

% Touristen per museumtype

TouristenPercentage_per_Museum2 = (df1 ['Waarvan Touristen'].values / df1 ['Totaal'].values).round(3) * 100

print ('Percentage Touristen per museum')
print (df1 ['Museumtype'].values.tolist())
print (TouristenPercentage_per_Museum2)

layout()
layout2()

pivot = df2.groupby(['Museumtype']).mean()
OmzetHorecaenWinkel = pivot.loc[:,"Winkel":"Totaal"]
layout()
layout2()

print ('Overzicht van de diverse musea en hun Horeca en Winkel omzet in 2019')
print (OmzetHorecaenWinkel)




