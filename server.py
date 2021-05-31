# Web Dev with flask
# Flask automatically converts text to HTML
# Flask uses jinja, which is a templating language
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  # Name of flask app
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# Dynamically adds all pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# function to write data from input form to text file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

# Better way to write out submissions (csv vs text)
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# Get - Send info. Post - Save info.
# This is getting information from the contact form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # get data from HTML request and write to database.txt
            write_to_file(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again.'


