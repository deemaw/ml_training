from flask import Flask, render_template, request
from facebookconnect import facebookconnect

app = Flask(__name__)
#POST - to receive data
# GET used to send data back only 
@app.route('/')
def main():
   
    return render_template('index.html')

@app.route('/facebook')
def facebook():

    return render_template('facebook.html')


@app.route('/facebook/facebook_get', methods=['POST'])

def facebook_get():

    post_url = request.form['post_url']
    facebookconnect(post_url)
    print(post_url)
    return render_template('facebook.html')


if __name__ == '__main__':

    app.run(debug=True)


facebook_get()