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
        for d in data:
            if d["State"] == state:
                bars1 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Selective sales tax"])+"},"
        bars1=bars1[:-1]
        bars2 = ""
        for d in data:
            if d["State"] == state:
                bars2 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["Tax"])+"},"
        bars2=bars2[:-1]
        bars3 = ""
        for d in data:
            if d["State"] == state:
                bars3 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Totals"]["License tax"])+"},"
        bars3=bars3[:-1]
        bars4 = ""
        for d in data:
            if d["State"] == state:
                bars4 += "{ x: new Date("+str(d["Year"])+",0), y:"+ str(d["Details"]["Other taxes"])+"},"
        bars4=bars4[:-1]




    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName3 = bars1, chart_data_insName4 = bars2, chart_data_insName5 = bars3, chart_data_insName6 = bars4, chart_data_insName7 = bars5, chart_data_insName8 = bars6, chart_data_insName9 = bars7, chart_data_insName10 = bars8)

            #        { x: new Date(2010,0), y: 28 },

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
