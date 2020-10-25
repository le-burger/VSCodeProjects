import pandas as pd

BezoekersAantallen = ('df1')
Horeca_en_Winkel_omzet = ('df2')

df1 = pd.read_excel (r"Museum gegevens 2019.xlsx","Bezoekers aantallen")
df2 = pd.read_excel (r"Museum gegevens 2019.xlsx","Horeca en Winkelomzet")

#Colums in Excel_file Bezoekersaantallen
Kolom0 = df1 ['Museumtype']
Kolom1 = df1 ['Museumjaarkaart']
Kolom2 = df1 ['Losse Tickets']
Kolom3 = df1 ['Waarvan Touristen']
Kolom4 = df1 ['Scholieren']
Kolom5 = df1 ['Totaal']

pivot = df1.groupby(['Museumtype']).mean()
GemiddeldAantalBezoekers = pivot.loc[:,"Museumjaarkaart":"Totaal"]
print ('= = = = = = = = = = = = = =')
print ('-                          -')
print ('Overzicht van de diverse musea en hun bezoers in 2019')
print (GemiddeldAantalBezoekers)


#Percentage Museumjaarkaart per museum tov het Totaal]
print ('= = = = = = = = = = = = = =')
print ('-                          -')
BezoekersPercentage_per_Museum1 = (df1 ['Museumjaarkaart'].values / df1 ['Totaal'].values).round(3) * 100
print ('Percentage Museumjaarkaart bezoekers per museum')

print (df1 ['Museumtype'].values.tolist())

print (BezoekersPercentage_per_Museum1)

print ('= = = = = = = = = = = = = =')
print ('-                          -')
#print (df1.columns)

# % Touristen per museumtype

BezoekersPercentage_per_Museum2 = (df1 ['Waarvan Touristen'].values / df1 ['Totaal'].values).round(3) * 100

print ('Percentage Touristen per museum')
print (df1 ['Museumtype'].values.tolist())
print (BezoekersPercentage_per_Museum2)

print ('= = = = = = = = = = = = = =')
print ('-                          -')

pivot = df2.groupby(['Museumtype']).mean()
OmzetHorecaenWinkel = pivot.loc[:,"Winkel":"Totaal"]
print ('= = = = = = = = = = = = = =')
print ('-                          -')
print ('Overzicht van de diverse musea en hun Horeca en Winkel omzet in 2019')
print (OmzetHorecaenWinkel)




