from flask import Flask, url_for, render_template, request, Markup
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


@app.route("/")
def render_main():
    s = get_state_options()
    y = get_year_options()
    return render_template('home.html', state_options = s, year_options = y)

@app.route("/p1")
def render_page1():
    name = request.args["totals"]
    state = request.args["state"]
    data = var_data(name, state)

    bars1 = ""
    if name == "Tax":
        t = 0
        for d in data:
            if d["State"] == state:
                bars1 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Selective sales tax"])+"},"
        bars1=bars1[:-1]
        bars2 = ""
        for d in data:
            if d["State"] == state:
                bars2 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["License tax"])+"},"
        bars2=bars2[:-1]
        bars3 = ""
        for d in data:
            if d["State"] == state:
                bars3 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Other taxes"])+"},"
        bars3=bars3[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName1 = bars1, chart_data_insName2 = bars2, chart_data_insName3 = bars3)

    bars4= ""
    if name == "Revenue":
        t = 0
        for d in data:
            if d["State"] == state:
                bars4 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Revenue"])+"},"
        bars4=bars4[:-1]
        bars5 = ""
        for d in data:
            if d["State"] == state:
                bars5 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["General revenue"])+"},"
                t = t+d["Totals"]["General revenue"]
        bars5=bars5[:-1]
        bars6 = ""
        for d in data:
            if d["State"] == state:
                bars6 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Miscellaneous general revenue"])+"},"
                t = t+d["Details"]["Miscellaneous general revenue"]
        bars6=bars6[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName4 = bars4, chart_data_insName5 = bars5, chart_data_insName6 = bars6)

    bars7= ""
    if name == "Expenditure":
        t = 0
        for d in data:
            if d["State"] == state:
                bars7 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Expenditure"])+"},"
                t = t+d["Totals"]["Expenditure"]
        bars7=bars7[:-1]
        bars8 = ""
        for d in data:
            if d["State"] == state:
                bars8 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["General expenditure"])+"},"
                t = t-d["Totals"]["General expenditure"]
        bars8=bars8[:-1]
        bars9 = ""
        for d in data:
            if d["State"] == state:
                bars9 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Natural Resources"]["Natural Resources Construction"])+"},"
                t = t-d["Details"]["Natural Resources"]["Natural Resources Construction"]
        bars9=bars9[:-1]
        bars10 = ""
        for d in data:
            if d["State"] == state:
                bars10 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Natural Resources"]["Parks"]["Parks Total Expenditure"])+"},"
                t = t-d["Details"]["Natural Resources"]["Parks"]["Parks Total Expenditure"]
        bars10=bars10[:-1]
        bars11 = ""
        for d in data:
            if d["State"] == state:
                bars11 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Welfare"]["Welfare Institution Total Expenditure"])+"},"
                t = t-d["Details"]["Welfare"]["Welfare Institution Total Expenditure"]
        bars11=bars11[:-1]
        bars12 = ""
        for d in data:
            if d["State"] == state:
                bars12 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Transportation"]["Highways"]["Highways Total Expenditure"])+"},"
                t = t-d["Details"]["Transportation"]["Highways"]["Highways Total Expenditure"]
        bars12=bars12[:-1]
        bars13 = ""
        for d in data:
            if d["State"] == state:
                bars13 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Utilities"]["Utilities Current Operation"])+"},"
                t = t-d["Details"]["Utilities"]["Utilities Current Operation"]
        bars13=bars13[:-1]
        bars14=""
        for d in data:
            if d["State"] == state:
                bars14 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Health"]["Health Total Expenditure"])+"},"
                t = t-d["Details"]["Health"]["Health Total Expenditure"]
        bars14=bars14[:-1]
        bars15=""
        for d in data:
            if d["State"] == state:
                bars15 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Education"]["Education Total"])+"},"
                t = t-d["Details"]["Education"]["Education Total"]
        bars15=bars15[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName7 = bars7, chart_data_insName8 = bars8, chart_data_insName9 = bars9, chart_data_insName10 = bars10, chart_data_insName11 = bars11, chart_data_insName12 = bars12, chart_data_insName13 = bars13, chart_data_insName14 = bars14, chart_data_insName15 = bars15)

    bars16= ""
    if name == "Insurance trust revenue":
        t = 0
        for d in data:
            if d["State"] == state:
                bars16 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Insurance trust revenue"])+"},"
                t = t+d["Totals"]["Insurance trust revenue"]
        bars16=bars16[:-1]
        bars17=""
        for d in data:
            if d["State"] == state:
                bars17 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Insurance benefits and repayments"])+"},"
                t = t+d["Details"]["Insurance benefits and repayments"]
        bars17=bars17[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName16 = bars16, chart_data_insName17 = bars17)

    bars18=""
    if name == "Financial Aid":
        t=0
        for d in data:
            if d["State"] == state:
                bars18 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Financial Aid"]["Assistance and Subsidies"])+"},"
                t = t+d["Details"]["Financial Aid"]["Assistance and Subsidies"]
        bars18=bars18[:-1]
        bars19=""
        for d in data:
            if d["State"] == state:
                bars19 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Financial Aid"]["Cash and Securities Total"])+"},"
                t = t+d["Details"]["Financial Aid"]["Cash and Securities Total"]
        bars19=bars19[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName18 = bars18, chart_data_insName19 = bars19)

    bars20= ""
    if name == "Debt at end of fiscal year":
        t = d["Totals"]["Debt at end of fiscal year"]
        for d in data:
            if d["State"] == state:
                bars20 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Debt at end of fiscal year"])+"},"
                t = t-d["Totals"]["Debt at end of fiscal year"]
        bars20=bars20[:-1]
        bars21=""
        for d in data:
            if d["State"] == state:
                bars21 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Interest on debt"])+"},"
                t = t-d["Details"]["Interest on debt"]
        bars21=bars21[:-1]
        bars22=""
        for d in data:
            if d["State"] == state:
                bars22 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Interest on general debt"])+"},"
                t = t-d["Details"]["Interest on general debt"]
        bars22=bars22[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName20 = bars20, chart_data_insName21 = bars21, chart_data_insName22 = bars22)

    bars23= ""
    if name == "Intergovernmental":
        t = 0
        for d in data:
            if d["State"] == state:
                bars23 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Intergovernmental"])+"},"
                t = t+d["Totals"]["Intergovernmental"]
        bars23=bars23[:-1]
        bars24=""
        for d in data:
            if d["State"] == state:
                bars24 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Intergovernmental"]["Intergovernmental Expenditure"])+"},"
                t = t-d["Details"]["Intergovernmental"]["Intergovernmental Expenditure"]
        bars24=bars24[:-1]
        bars25=""
        for d in data:
            if d["State"] == state:
                bars2526 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Intergovernmental"]["Intergovernmental to Combined and Unallocable"])+"},"
                t = t-d["Details"]["Intergovernmental"]["Intergovernmental to Combined and Unallocable"]
        bars25=bars25[:-1]
        bars26=""
        for d in data:
            if d["State"] == state:
                bars26 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Police protection"])+"},"
                t = t-d["Details"]["Police protection"]
        bars26=bars26[:-1]
        bars27=""
        for d in data:
            if d["State"] == state:
                bars27 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Correction"]["Education Total"])+"},"
                t = t-d["Details"]["Correction"]["Correction Total"]
        bars27=bars27[:-1]
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName23 = bars23, chart_data_insName24 = bars24, chart_data_insName25 = bars25, chart_data_insName26 = bars26, chart_data_insName27 = bars27)

            #        { x: new Date(2010,0), y: 28 },
#change
@app.route("/p2")
def render_page2():
    return render_template('page2.html')


def get_state_options():
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('finance.json') as demographics_data:
        counties = json.load(demographics_data)
    states=[]
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
    options=""
    for s in states:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

def get_year_options():
        """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
        with open('finance.json') as demographics_data:
            counties = json.load(demographics_data)
        options= Markup("<option value=Capital outlay>Capital outlay </option>" + "<option value=Revenue>Revenue </option>" + "<option value=Expenditure>Expenditure </option>" + "<option value=General expenditure>General expenditure </option>" + "<option value=General revenue>General revenue </option>" + "<option value=Insurance trust revenue>Insurance trust revenue </option>" + "<option value=Intergovernmental>Intergovernmental </option>" + "<option value=Tax>Tax </option>" + "<option value=Debt at end of fiscal year>Debt at end of fiscal year </option>" + "<option value=Correction Correction Total>Correction Total </option>" + "<option value=Education Total>Education Total </option>" + "<option value=Financial Aid>Financial Aid </option>" + "<option value=Health Total Expenditure>Health Total Expenditure </option>" + "<option value=Natural Resources>Natural Resources </option>" + "<option value=Utilities Current Operation>Utilities Current Operation </option>" + "<option value=Welfare Institution Total Expenditure>Welfare Institution Total Expenditure </option>" + "<option value=Transportation>Transportation </option>" + "<option value=Interest on debt>Interest on debt </option>" + "<option value=Tax>Tax </option>" + "<option value=Tax>Tax </option>" + "<option value=Tax>Tax </option>" + "<option value=Tax>Tax </option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
        return options

def var_data(name, state):
    with open('finance.json') as demographics_data:
        counties = json.load(demographics_data)
    #    cpOut = 0
    #    rev = 0
    #    exp = 0
    #    genExp = 0
    #    genRev = 0
    #    insTRev = 0
    #    intgov = 0
    #    licT = 0
    #    slcSlT = 0
    #    t = 0
    #    dbtFisY = 0



    if type == "Revenue":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Revenue"]
        else:
            totals[c["Year"]] = c["Totals"]["Revenue"]

    if type == "Expenditure":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Expenditure"]
        else:
            totals[c["Year"]] = c["Totals"]["Expenditure"]

    if type == "General expenditure":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["General expenditure"]
        else:
            totals[c["Year"]] = c["Totals"]["General expenditure"]

    if type == "General revenue":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["General revenue"]
        else:
            totals[c["Year"]] = c["Totals"]["General revenue"]

    if type == "Insurance trust revenue":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Insurance trust revenue"]
        else:
            totals[c["Year"]] = c["Totals"]["Insurance trust revenue"]

    if type == "Intergovernmental":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Intergovernmental"]
        else:
            totals[c["Year"]] = c["Totals"]["Intergovernmental"]

    if type == "License tax":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["License tax"]
        else:
            totals[c["Year"]] = c["Totals"]["License tax"]

    if type == "Selective sales tax":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Selective sales tax"]
        else:
            totals[c["Year"]] = c["Totals"]["Selective sales tax"]

    if type == "Tax":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Tax"]
        else:
            totals[c["Year"]] = c["Totals"]["Tax"]

    if type == "Debt at end of fiscal year":
        if c["Year"] in totals.keys():
            totals[c["Year"]] += c["Totals"]["Debt at end of fiscal year"]
        else:
            totals[c["Year"]] = c["Totals"]["Debt at end of fiscal year"]
    #print (totals)
    #data = ""
    #for a in totals:
    #    data += Markup("{ x: new Date(" + a + ", x:/" + a.value() + "},")
    return counties











if __name__=="__main__":
    app.run(debug=True)
