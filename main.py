from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

# Within encrypt, store the values of these request parameters in local variables, 
# converting data types as necessary. Then, encrypt the value of the text 
# parameter using rotate_string. Return the encrypted string wrapped in <h1> tags,
# to be rendered in the browser.

   
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method='POST'>
        <label>Rotate By:
            <input name="rot" type="text" value="0" />
        </label>

        <br>


        <label>
            <textarea name="text"></textarea>
        </label>

        <br>

        <input type="submit" />

        </form>

    </body>
</html>
    
    """

@app.route("/")
def display_form_inputs():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']  
    rot = int(request.form['rot'])
    return form.format(rotate_string(text,rot))
    
app.run()