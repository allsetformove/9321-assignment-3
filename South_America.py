from flask import render_template, Flask
app = Flask(__name__)


import csv

filename = './static/csv/kaggle population.csv'
country_names = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela, RB']
filename1 = './static/csv/Forestarea.csv'
filename2 = './static/csv/GDPperperson.csv'
filename3 = './static/csv/inflation.csv'
filename4 = './static/csv/Lifeexpectancyatbirth.csv'
filename5 = './static/csv/Netmigration.csv'

population2009 = []
population2011 = []
population2013 = []
population2015 = []
hospital_beds2006 = []
hospital_beds2008 = []
hospital_beds2010 = []
hospital_beds2012 = []
money_on_per_student2010 = []
money_on_per_student2012 = []
money_on_per_student2014 = []
money_on_per_student2016 = []
pm2_5_2010 = []
pm2_5_2012 = []
pm2_5_2014 = []
pm2_5_2016 = []
deposit_interest2011 = []
deposit_interest2013 = []
deposit_interest2015 = []
deposit_interest2017 = []

forest2009 = []
forest2011 = []
forest2013 = []
forest2015 = []
GDP2009 = []
GDP2011 = []
GDP2013 = []
GDP2015 = []
inflation2009 = []
inflation2011 = []
inflation2013 = []
inflation2015 = []
Life2009 = []
Life2011 = []
Life2013 = []
Life2015 = []
migration1997 = []
migration2002 = []
migration2007 = []
migration2012 = []



with open(filename,  encoding='gbk',errors='ignore') as f:
    reader = csv.reader(f)
    i = 0
    for i in range(4):
        head_row = next(reader)
    i, j  = 0, 0
    reader = csv.reader(f)
    for j in range(12):
        for i,rows in enumerate(reader):
            if rows[0] in country_names:
                population2009.append(rows[-8])
                population2011.append(rows[-6])
                population2013.append(rows[-4])
                population2015.append(rows[-2])
                break

i = 0
for i in range(12):
    population2009[i] = round(float(population2009[i]), 3)
    population2011[i] = round(float(population2011[i]), 3)
    population2013[i] = round(float(population2013[i]), 3)
    population2015[i] = round(float(population2015[i]), 3)

with open('./static/csv/hospital beds.csv', encoding = 'gbk', errors = 'ignore') as f1:
    reader = csv.reader(f1)
    i = 0
    for i in range(4):
        head_row = next(reader)
    i = 0
    reader = csv.DictReader(f1)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2006']
            column2 = row['2008']
            column3 = row['2010']
            column4 = row['2012']
            hospital_beds2006.append(column1)
            hospital_beds2008.append(column2)
            hospital_beds2010.append(column3)
            hospital_beds2012.append(column4)
    a = 0
    for a in range(12):
        if hospital_beds2006[a] != '':
            hospital_beds2006[a] = round(float(hospital_beds2006[a]), 3)
        else:
            hospital_beds2006[a] = 0
        if hospital_beds2008[a] != '':
            hospital_beds2008[a] = round(float(hospital_beds2008[a]), 3)
        else:
            hospital_beds2008[a] = 0
        if hospital_beds2010[a] != '':
            hospital_beds2010[a] = round(float(hospital_beds2010[a]), 3)
        else:
            hospital_beds2010[a] = 0
        if hospital_beds2012[a] != '':
            hospital_beds2012[a] = round(float(hospital_beds2012[a]), 3)
        else:
            hospital_beds2012[a] = 0


with open('./static/csv/money on per stu.csv', encoding = 'gbk', errors = 'ignore') as f2:
    reader = csv.reader(f2)
    i = 0
    for i in range(4):
        head_row = next(reader)
    i = 0
    reader = csv.DictReader(f2)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2010']
            column2 = row['2012']
            column3 = row['2014']
            column4 = row['2016']
            money_on_per_student2010.append(column1)
            money_on_per_student2012.append(column2)
            money_on_per_student2014.append(column3)
            money_on_per_student2016.append(column4)
    a = 0
    for a in range(12):
        if money_on_per_student2010[a] != '':
            money_on_per_student2010[a] = round(float(money_on_per_student2010[a]), 3)
        else:
            money_on_per_student2010[a] = 0
        if money_on_per_student2012[a] != '':
            money_on_per_student2012[a] = round(float(money_on_per_student2012[a]), 3)
        else:
            money_on_per_student2012[a] = 0
        if money_on_per_student2014[a] != '':
            money_on_per_student2014[a] = round(float(money_on_per_student2014[a]), 3)
        else:
            money_on_per_student2014[a] = 0
        if money_on_per_student2016[a] != '':
            money_on_per_student2016[a] = round(float(money_on_per_student2016[a]), 3)
        else:
            money_on_per_student2016[a] = 0

with open('./static/csv/pm2.5.csv', encoding = 'gbk', errors = 'ignore') as f3:
    reader = csv.reader(f3)
    i = 0
    for i in range(4):
        head_row = next(reader)
    i, j  = 0, 0
    reader = csv.reader(f3)
    for j in range(12):
        for i,rows in enumerate(reader):
            if rows[0] in country_names:
                if rows[-9] != '':
                    pm2_5_2010.append(rows[-9])
                else:
                    pm2_5_2010.append(0)
                if rows[-7] != '':
                    pm2_5_2012.append(rows[-7])
                else:
                    pm2_5_2012.append(0)
                if rows[-5] != '':
                    pm2_5_2014.append(rows[-5])
                else:
                    pm2_5_2014.append(0)
                if rows[-3] != '':
                    pm2_5_2016.append(rows[-3])
                else:
                    pm2_5_2016.append(0)
                break
    i = 0
    for i in range(12):
        pm2_5_2010[i] = round(float(pm2_5_2010[i]), 3)
        pm2_5_2012[i] = round(float(pm2_5_2012[i]), 3)
        pm2_5_2014[i] = round(float(pm2_5_2014[i]), 3)
        pm2_5_2016[i] = round(float(pm2_5_2016[i]), 3)

with open('./static/csv/deposit interest.csv', encoding = 'gbk', errors = 'ignore') as f4:
    reader = csv.reader(f4)
    i = 0
    for i in range(4):
        head_row = next(reader)
    i, j  = 0, 0
    reader = csv.DictReader(f4)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2011']
            column2 = row['2013']
            column3 = row['2015']
            column4 = row['2017']
            deposit_interest2011.append(column1)
            deposit_interest2013.append(column2)
            deposit_interest2015.append(column3)
            deposit_interest2017.append(column4)
    a = 0
    for a in range(12):
        if deposit_interest2011[a] != '':
            deposit_interest2011[a] = round(float(deposit_interest2011[a]), 3)
        else:
            deposit_interest2011[a] = 0
        if deposit_interest2013[a] != '':
            deposit_interest2013[a] = round(float(deposit_interest2013[a]), 3)
        else:
            deposit_interest2013[a] = 0
        if deposit_interest2015[a] != '':
            deposit_interest2015[a] = round(float(deposit_interest2015[a]), 3)
        else:
            deposit_interest2015[a] = 0
        if deposit_interest2017[a] != '':
            deposit_interest2017[a] = round(float(deposit_interest2017[a]), 3)
        else:
            deposit_interest2017[a] = 0

with open(filename1, encoding='gbk',errors='ignore') as f:
    reader = csv.reader(f)
    i = 0
    for i in range(4):
        head_row = next(reader)

    reader = csv.DictReader(f)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2009']
            column2 = row['2011']
            column3 = row['2013']
            column4 = row['2015']
            forest2009.append(column1)
            forest2011.append(column2)
            forest2013.append(column3)
            forest2015.append(column4)

with open(filename2, encoding='gbk',errors='ignore') as f:
    reader = csv.reader(f)
    i = 0
    for i in range(4):
        head_row = next(reader)

    reader = csv.DictReader(f)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2009']
            column2 = row['2011']
            column3 = row['2013']
            column4 = row['2015']
            GDP2009.append(column1)
            GDP2011.append(column2)
            GDP2013.append(column3)
            GDP2015.append(column4)

with open(filename3, encoding='gbk',errors='ignore') as f:
    reader = csv.reader(f)
    i = 0
    for i in range(4):
        head_row = next(reader)

    reader = csv.DictReader(f)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2009']
            column2 = row['2011']
            column3 = row['2013']
            column4 = row['2015']
            inflation2009.append(column1)
            inflation2011.append(column2)
            inflation2013.append(column3)
            inflation2015.append(column4)

with open(filename4, encoding='gbk',errors='ignore') as f:
    reader = csv.reader(f)
    i = 0
    for i in range(4):
        head_row = next(reader)

    reader = csv.DictReader(f)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['2009']
            column2 = row['2011']
            column3 = row['2013']
            column4 = row['2015']
            Life2009.append(column1)
            Life2011.append(column2)
            Life2013.append(column3)
            Life2015.append(column4)

with open(filename5, encoding='gbk',errors='ignore') as f:
    reader = csv.reader(f)
    i = 0
    for i in range(4):
        head_row = next(reader)

    reader = csv.DictReader(f)
    for row in reader:
        if row['Country Name'] in country_names:
            #dataset.append(row)
            column1 = row['1997']
            column2 = row['2002']
            column3 = row['2007']
            column4 = row['2012']
            migration1997.append(column1)
            migration2002.append(column2)
            migration2007.append(column3)
            migration2012.append(column4)

a = 0
for a in range(12):
    if forest2009[a] != '':
        forest2009[a] = round(float(forest2009[a]), 3)
    else:
        forest2009[a] = 0
    if forest2011[a] != '':
        forest2011[a] = round(float(forest2011[a]), 3)
    else:
        forest2011[a] = 0
    if forest2013[a] != '':
        forest2013[a] = round(float(forest2013[a]), 3)
    else:
        forest2013[a] = 0
    if forest2015[a] != '':
        forest2015[a] = round(float(forest2015[a]), 3)
    else:
        forest2015[a] = 0

b = 0
for b in range(12):
    if GDP2009[b] != '':
        GDP2009[b] = round(float(GDP2009[b]), 3)
    else:
        GDP2009[b] = 0
    if GDP2011[b] != '':
        GDP2011[b] = round(float(GDP2011[b]), 3)
    else:
        GDP2011[b] = 0
    if GDP2013[b] != '':
        GDP2013[b] = round(float(GDP2013[b]), 3)
    else:
        GDP2013[b] = 0
    if GDP2015[b] != '':
        GDP2015[b] = round(float(GDP2015[b]), 3)
    else:
        GDP2015[b] = 0

c = 0
for c in range(12):
    if inflation2009[c] != '':
        inflation2009[c] = round(float(inflation2009[c]), 3)
    else:
        inflation2009[c] = 0
    if inflation2011[c] != '':
        inflation2011[c] = round(float(inflation2011[c]), 3)
    else:
        inflation2011[c] = 0
    if inflation2013[c] != '':
        inflation2013[c] = round(float(inflation2013[c]), 3)
    else:
        inflation2013[c] = 0
    if inflation2015[c] != '':
        inflation2015[c] = round(float(inflation2015[c]), 3)
    else:
        inflation2015[c] = 0

d = 0
for d in range(12):
    if Life2009[d] != '':
        Life2009[d] = round(float(Life2009[d]), 3)
    else:
        Life2009[d] = 0
    if Life2011[d] != '':
        Life2011[d] = round(float(Life2011[d]), 3)
    else:
        Life2011[d] = 0
    if Life2013[d] != '':
        Life2013[d] = round(float(Life2013[d]), 3)
    else:
        Life2013[d] = 0
    if Life2015[d] != '':
        Life2015[d] = round(float(Life2015[d]), 3)
    else:
        Life2015[d] = 0

e = 0
for e in range(12):
    if migration1997[e] != '':
        migration1997[e] = round(float(migration1997[e]), 3)
    else:
        migration1997[e] = 0
    if migration2002[e] != '':
        migration2002[e] = round(float(migration2002[e]), 3)
    else:
        migration2002[e] = 0
    if migration2007[e] != '':
        migration2007[e] = round(float(migration2007[e]), 3)
    else:
        migration2007[e] = 0
    if migration2012[e] != '':
        migration2012[e] = round(float(migration2012[e]), 3)
    else:
        migration2012[e] = 0



r1 = 8.02 * 0.01
r2 = 20.99 * 0.01
r3 = 17.68 * 0.01
r4 = 4.97 * 0.01
r5 = 16.57 * 0.01
r6 = 13.81 * 0.01
r7 = 6.91 * 0.01
r8 = 11.05 * 0.01
hospital_s = []
student_s = []
pm2_5_s = []
deposit_s = []
forest_s = []
GDP_s = []
inflation_s = []
life_s = []
score = []

#specific data adjustment
inflation2015[0] = 10.6
hospital_beds2012[3], hospital_beds2012[5], hospital_beds2012[6], hospital_beds2012[8], hospital_beds2012[9], hospital_beds2012[11] = 2.1, 1.6, 2, 1.5, 3.1, 0.9
money_on_per_student2016[0], money_on_per_student2016[1], money_on_per_student2016[2], money_on_per_student2016[3], money_on_per_student2016[6] = 15.977, 23.482, 19.589, 15.099, 7.75
money_on_per_student2016[8], money_on_per_student2016[10], money_on_per_student2016[11] = 11.775, 8.565, 0.018
deposit_interest2017[3], deposit_interest2017[7], deposit_interest2017[8], deposit_interest2017[9], deposit_interest2017[10], deposit_interest2017[11] = 3.81, 2.48, 3.85, 8.07, 5.56, 15.0
i = 0
for i in range(12):
    hospital_s.append(round(hospital_beds2012[i] / max(hospital_beds2012) * 100 * r1, 3))
i = 0
for i in range(12):
    student_s.append(round(money_on_per_student2016[i] / max(money_on_per_student2016) * 100 * r2, 3))
i = 0
for i in range(12):
    pm2_5_s.append(round(pm2_5_2016[i] / max(pm2_5_2016) * 100 * r3, 3))
i = 0
for i in range(12):
    deposit_s.append(round(deposit_interest2017[i] / max(deposit_interest2017) * 100 * r4, 3))
i = 0
for i in range(12):
    forest_s.append(round(forest2015[i] / max(forest2015) * 100 * r5, 3))
i = 0
for i in range(12):
    GDP_s.append(round(GDP2015[i] / max(GDP2015) * 100 * r6, 3))
i = 0
temp = 0
for i in range(12):
    temp = (max(inflation2015) - inflation2015[i]) / max(inflation2015)
    inflation_s.append(round(temp * 100 * r7, 3))
i = 0
for i in range(12):
    life_s.append(round(Life2015[i] / max(Life2015) * 100 * r8, 3))
i = 0
for i in range(12):
    score.append(hospital_s[i] + student_s[i] + pm2_5_s[i] + deposit_s[i] + forest_s[i] + GDP_s[i] + inflation_s[i] + life_s[i])
    score[i] = round(score[i], 3)
final_score1 = dict(zip(country_names, score))

#change dict to list
aaa = sorted(final_score1.items(),key = lambda x:x[1],reverse = True)
final_score = []
for i in range(len(aaa)):
    final_score.append(list(aaa[i]))
final_score[10][0] = 'Venezuela'








@app.route('/')
def index():
    return render_template("main.html",final_score = final_score)

@app.route("/<countryname>")
def countrydata(countryname):
    country_list = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana',
                    'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

    if countryname == 'dataanalysis' or  countryname == 'dataanalysis.html':
        return render_template("dataanalysis.html")
    if countryname == 'main' or  countryname == 'main.html':
        return render_template("main.html",final_score = final_score)
    if countryname.split('.')[0] not in country_list:
        return render_template("inputwrong.html")

    number = country_list.index(countryname.split('.')[0])

    country_population = {'population': population2015[number]}
    country_hospital_beds = {'hospital_beds': hospital_beds2012[number]}
    country_money_on_per_student = {'money_on_per_student': money_on_per_student2016[number]}
    country_pm2_5 = {'pm2_5': pm2_5_2016[number]}
    country_deposit_interest = {'deposit_interest': deposit_interest2017[number]}
    country_forest = {'forest': forest2015[number]}
    country_GDP = {'GDP': GDP2015[number]}
    country_inflation = {'inflation': inflation2015[number]}
    country_Life = {'Life': Life2015[number]}
    country_migration = {'migration': migration2012[number]}

    return render_template(countryname, population = country_population, hospital_beds = country_hospital_beds, money_on_per_student = country_money_on_per_student
                                           , pm2_5 = country_pm2_5, deposit_interest = country_deposit_interest, forest = country_forest, GDP = country_GDP
                                           , inflation = country_inflation, Life = country_Life, migration = country_migration)

@app.route("/dataanalysis.html")
def data():
    return render_template("dataanalysis.html",score = score)


if __name__ == "__main__":
    app.run(debug="true")


