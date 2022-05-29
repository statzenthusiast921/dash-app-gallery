from dash import Dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc 
from datetime import datetime, date
app = Dash(__name__)

# main app code
app.layout = html.Div(
    [        
        dcc.Markdown("""
        #### Birthday !! 
        here we are asking user to enter birthdate with datepicker and showing success message when user selects date.
        we will be using duration to make sure alert will last for certain duration
        """), 
        dmc.DatePicker(
            id="age-alert-x-date-pick",
            label="Birthday!",
            description="please pick your birthdate!",
            minDate=date(1900, 8, 5),
            maxDate=date(2022, 9, 19),
            value=date(2002, 9, 19),
        ),
        html.Div(id = "age-alert-x-show-succ"),
        html.Div(id= "age-alert-x-show-age"),
        dcc.Markdown('''
            ### Using Simple alert
            You can use this for simple application for showing success, failure, etc. Note that this will stay on screen till it's rendering since we are `not giving any duration`.
            '''), 
        dbc.Alert("this is a simple alert", color= "warning"),
        dcc.Markdown("One with the `different color`"), 
        dbc.Alert("one with another color" , color = "danger"),
        dcc.Markdown("""
            alert on click
            """),
        dbc.Button(
            "Toggle alert", id="age-alert-x-toggle-fade", n_clicks=0
        ),
        html.Div(id="age-alert-x-fade")
    ]
)

# app callback using datepicker and updating alert and div according to date provided
@callback(
    Output("age-alert-x-show-succ", "children"),
    Output("age-alert-x-show-age", "children"),
    Input("age-alert-x-date-pick", "value")
)
def update_output(d): 
    todays_date = datetime.now().date().year
    if todays_date- int(d[:4]) > 18 : 
        text = """
        # 
            You are 18+ 🎁! """  
    else: 
        text = """
        # 
            Happy childhood! 🎉 """  
    alert_text = f"thanks for selecting date {d}"
    duration = 3000
    if  d == "2002-09-19":
        duration = 1 
        alert_text = ""
        text = ""
    
    return [
    dbc.Alert(alert_text , duration = duration , color = 'success'),
    dcc.Markdown(text)
    ]

# app callback for toggling alert with button
@app.callback(
    Output("age-alert-x-fade", "children"),
    [Input("age-alert-x-toggle-fade", "n_clicks")],
)
def toggle_alert(n):
    return dbc.Alert("Hello! I am an alert",dismissable=True,duration = 900)

if __name__ == "__main__":
    app.run_server(debug=True)
