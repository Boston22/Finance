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
    years=[]
    for c in counties:
        if c["Year"] not in years:
            years.append(c["Year"])
    options=""
    for y in years:
        options += Markup("<option value=\"" + str(y) + "\">" + str(y) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options







if __name__=="__main__":
    app.run(debug=True)
