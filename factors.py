from flask import Flask, url_for, render_template, request, Markup
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


@app.route("/")
def render_main():
    # type = request.args["year"]
    s = get_state_options()
    y = get_year_options()
    d = var_data(type)
    return render_template('home.html', state_options = s, year_options = y)

@app.route("/p1")
def render_page1():

    return render_template('page1.html')

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
        options= Markup("<option value=Capital outlay>Capital outlay </option>" + "<option value=Revenue>Revenue </option>" + "<option value=Expenditure>Expenditure </option>" + "<option value=General expenditure>General expenditure </option>" + "<option value=General revenue>General revenue </option>" + "<option value=Insurance trust revenue>Insurance trust revenue </option>" + "<option value=Intergovernmental>Intergovernmental </option>" + "<option value=License tax>License tax </option>" + "<option value=Selective sales tax>Selective sales tax </option>" + "<option value=Tax>Tax </option>" + "<option value=Debt at end of fiscal year>Debt at end of fiscal year </option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
        return options

def var_data(type):
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
        for c in counties:
            if type == "Capital outlay":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Capital outlay"]
                else:
                    totals[c["year"]] = c["totals"]["Capital outlay"]

            if type == "Revenue":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Revenue"]
                else:
                    totals[c["year"]] = c["totals"]["Revenue"]

            if type == "Expenditure":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Expenditure"]
                else:
                    totals[c["year"]] = c["totals"]["Expenditure"]

            if type == "General expenditure":
                    totals = {}
                    if c["year"] in totals.keys():
                        totals[c["year"]] += c["totals"]["General expenditure"]
                    else:
                        totals[c["year"]] = c["totals"]["General expenditure"]

            if type == "General revenue":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["General revenue"]
                else:
                    totals[c["year"]] = c["totals"]["General revenue"]

            if type == "Insurance trust revenue":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Insurance trust revenue"]
                else:
                    totals[c["year"]] = c["totals"]["Insurance trust revenue"]

            if type == "Intergovernmental":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Intergovernmental"]
                else:
                    totals[c["year"]] = c["totals"]["Intergovernmental"]

            if type == "License tax":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["License tax"]
                else:
                    totals[c["year"]] = c["totals"]["License tax"]

            if type == "Selective sales tax":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Selective sales tax"]
                else:
                    totals[c["year"]] = c["totals"]["Selective sales tax"]

            if type == "Tax":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Tax"]
                else:
                    totals[c["year"]] = c["totals"]["Tax"]

            if type == "Debt at end of fiscal year":
                totals = {}
                if c["year"] in totals.keys():
                    totals[c["year"]] += c["totals"]["Debt at end of fiscal year"]
                else:
                    totals[c["year"]] = c["totals"]["Debt at end of fiscal year"]


    # data = ""
    # for a in totals:
    #     data += Markup("")
    # return data









if __name__=="__main__":
    app.run(debug=True)
