#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask, render_template


#from . import app, db
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)


app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 450


@app.route('/')
def index():
    return render_template('pages/home.html')


# Default port:
if __name__ == '__main__':
    app.run(port=5052, debug=True)
