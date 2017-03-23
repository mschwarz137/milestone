from flask import Flask, render_template, request, redirect
import quandl as qd
from bokeh.plotting import figure,show
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/view_ticker', methods=['GET', 'POST'])
def view_ticker():

    #problem line:
  d = qd.get("WIKI/" + request.form['ticker'] + ".4", rows = 20)

  f = figure(x_axis_type='datetime',title = "Closing Price for " + request.form['ticker'] + " for the Past 30 Days")
  f.line('Date', 'Close', source=d)
  f.xaxis.axis_label = "Date"
  f.yaxis.axis_label = "Price"
  

  html = file_html(f, CDN, "my plot")
  
  return html

if __name__ == '__main__':
  app.run()
