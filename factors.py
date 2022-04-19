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
    if name == "Tax":
        for d in data:
            if d["State"] == state:
                "{ x: new Date("+d["Year"]+",0), y:"+ d["Totals"]["Selective sales tax"]}
    return render_template('page1.html', chart_data_intergovExp = name, chart_data_insName3 = data)

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
        totals = {}
        for c in counties:
            if c["Year"] in totals.keys():
                if state == c["State"]:
                    if type == "Capital outlay":
                            totals[c["Year"]] += c["Totals"]["Capital outlay"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Capital outlay"]


                    if type == "Revenue":
                            totals[c["Year"]] += c["Totals"]["Revenue"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Revenue"]

                    if type == "Expenditure":
                            totals[c["Year"]] += c["Totals"]["Expenditure"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Expenditure"]

                    if type == "General expenditure":
                                totals[c["Year"]] += c["Totals"]["General expenditure"]
                            else:
                                totals[c["Year"]] = c["Totals"]["General expenditure"]

                    if type == "General revenue":
                            totals[c["Year"]] += c["Totals"]["General revenue"]
                        else:
                            totals[c["Year"]] = c["Totals"]["General revenue"]

                    if type == "Insurance trust revenue":
                            totals[c["Year"]] += c["Totals"]["Insurance trust revenue"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Insurance trust revenue"]

                    if type == "Intergovernmental":
                            totals[c["Year"]] += c["Totals"]["Intergovernmental"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Intergovernmental"]

                    if type == "License tax":
                            totals[c["Year"]] += c["Totals"]["License tax"]
                        else:
                            totals[c["Year"]] = c["Totals"]["License tax"]

                    if type == "Selective sales tax":
                            totals[c["Year"]] += c["Totals"]["Selective sales tax"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Selective sales tax"]

                    if type == "Tax":
                            totals[c["Year"]] += c["Totals"]["Tax"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Tax"]

                    if type == "Debt at end of fiscal year":
                            totals[c["Year"]] += c["Totals"]["Debt at end of fiscal year"]
                        else:
                            totals[c["Year"]] = c["Totals"]["Debt at end of fiscal year"]
    print (totals)
    data = ""
    for a in totals:
        data += Markup("{ x: new Date(" + a + ", x:/" + a.value() + "},")
    return data











if __name__=="__main__":
    app.run(debug=True)
