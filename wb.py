import wbdata
import datetime
data_date = (datetime.datetime(2014, 1, 1), datetime.datetime(2014, 1, 1))
wbdata.get_data("NY.GDP.MKTP.CD", country='USA', data_date=data_date)
wbdata.get_data("SP.POP.TOTL", country='USA', data_date=data_date)
wbdata.get_data("AG.LND.FRST.K2", country='USA', data_date=data_date)
wbdata.get_data("EG.USE.ELEC.KH.PC", country='USA', data_date=data_date)
wbdata.get_data("SL.TLF.TOTL.IN", country='USA', data_date=data_date)
wbdata.get_data("EN.ATM.CO2E.PC", country='USA', data_date=data_date)
wbdata.get_data("BN.CAB.XOKA.CD", country='USA', data_date=data_date)
wbdata.get_data("AG.LND.TOTL.K2", country='USA', data_date=data_date)
wbdata.get_data("IS.RRS.TOTL.KM", country='USA', data_date=data_date)
wbdata.get_data("IC.TAX.TOTL.CP.ZS", country='USA', data_date=data_date)
country = {'Argentina':'ARG',
           'Bolivia':'BOL',
           'Brazil':'BRA',
           'Chile':'CHL',
           'Colombia':'COL',
           'Ecuador':'ECU',
           'Guyana':'GUY',
           'Paraguay':'PRY',
           'Peru':'PER',
           'Suriname':'SUR',
           'Uruguay':'URY',
           'Venezuela':'VEN'}

wbdata.get_data("NY.GDP.MKTP.CD", country='PER', data_date=data_date)

resultgdp = [wbdata.get_data("NY.GDP.MKTP.CD", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("SP.POP.TOTL", country='PER', data_date=data_date)

resultpop = [wbdata.get_data("SP.POP.TOTL", country=i, data_date=data_date) for i in country.values() ]


wbdata.get_data("AG.LND.FRST.K2", country='PER', data_date=data_date)

resultfor = [wbdata.get_data("AG.LND.FRST.K2", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("EG.USE.ELEC.KH.PC", country='PER', data_date=data_date)

resultepc = [wbdata.get_data("EG.USE.ELEC.KH.PC", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("SL.TLF.TOTL.IN", country='PER', data_date=data_date)

resultlf = [wbdata.get_data("SL.TLF.TOTL.IN", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("EN.ATM.CO2E.PC", country='PER', data_date=data_date)

resultco2 = [wbdata.get_data("EN.ATM.CO2E.PC", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("BN.CAB.XOKA.CD", country='PER', data_date=data_date)

resultbop = [wbdata.get_data("BN.CAB.XOKA.CD", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("AG.LND.TOTL.K2", country='PER', data_date=data_date)

resultland = [wbdata.get_data("AG.LND.TOTL.K2", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("IS.RRS.TOTL.KM", country='PER', data_date=data_date)

resultrail = [wbdata.get_data("IS.RRS.TOTL.KM", country=i, data_date=data_date) for i in country.values() ]

wbdata.get_data("IC.TAX.TOTL.CP.ZS", country='PER', data_date=data_date)

resulttax = [wbdata.get_data("IC.TAX.TOTL.CP.ZS", country=i, data_date=data_date) for i in country.values() ]



country.values()

GDP = [i[0]['value'] for i in resultgdp]

print(GDP)

Population = [i[0]['value'] for i in resultpop]

print(Population)




forest = [i[0]['value'] for i in resultfor]

print(forest)



epc = [i[0]['value'] for i in resultepc]

print(epc)




LF = [i[0]['value'] for i in resultlf]

print(LF)




CO2 = [i[0]['value'] for i in resultco2]

print(CO2)

bop = [i[0]['value'] for i in resultbop]

print(bop)




land = [i[0]['value'] for i in resultland]

print(land)




railway = [i[0]['value'] for i in resultrail]

print(railway)





tax = [i[0]['value'] for i in resulttax]

print(tax)
