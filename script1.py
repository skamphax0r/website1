#!/python3
from flask import Flask, render_template
import os

app=Flask(__name__)


@app.route('/')
def home():
    ipaddy=os.getenv('IP')
    return render_template("home.html",ipaddy=ipaddy)

@app.route('/aboot/')
def aboot():
    return render_template("aboot.html")
    

    
if __name__=="__main__":
    app.run(debug=False,host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', '19000')))
    
