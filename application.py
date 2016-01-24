from flask import Flask, render_template
import jinja2

app = Flask(__name__)


@app.route("/application-form")
def form_page():
    """this is the form page"""
    print "error"
    return render_template("application-form.html")



@app.route("/application", methods="POST")
def index_page():
    

    first_name = request.form.get(fname)
    last_name = request.form.get(lname)
    salary = request.form.get(salary)
    position = request.form.get(position)


    return """

    <!doctype html>
    <html>
        <head>
            <title>Thank you!</title>
        </head>
        <body>
            <div "Thank you %s %s, for applying to be a %s. Your minimum salary requirement is $%s dollars." 
            </div> 
        </body>
    </html>""" %(first_name,last,position,salary)

    
#     # Alternately, we could make this a Jinja template in `templates/`
#     # and return that result of rendering this, like:
#     #
#     # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
