from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore
import re
import logging

# create a instance for the Flask class
app = Flask(__name__) # app configure routes,handles requests and run the application
app.secret_key = 'your_secret_key'# generates 32-hexadecimal string to encrypt for session management
# CSRF protection,flash messages

# Set up logging
logging.basicConfig(level=logging.DEBUG)# it has debug, info,warning,error,critical mode
logger = logging.getLogger(__name__)

# List of countries
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
    "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar",
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
    "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

def sanitize_input(input_data):
    return re.sub(r'[<>]', '', input_data) # Protect against XSS

def validate_email(email):
    return re.match(r'[^@]+@[^@]+\.[^@]+', email)# regular expression.(pattern,string)

@app.route('/', methods=['GET', 'POST'])# decorators
def contact():
    if request.method == 'POST':
        first_name = sanitize_input(request.form['first_name'])
        last_name = sanitize_input(request.form['last_name'])
        email = sanitize_input(request.form['email'])
        country = sanitize_input(request.form['country'])
        message = sanitize_input(request.form['message'])
        gender = sanitize_input(request.form['gender'])
        subject = request.form.getlist('subject')
        honeypot = request.form['honeypot']

        logger.debug(f"Form submitted with: {first_name=}, {last_name=}, {email=}, {country=}, {message=}, {gender=}, {subject=}, {honeypot=}")

        # Check honeypot field
        if honeypot:
            flash('Spam detected!', 'danger')
            logger.warning("Spam detected due to honeypot field.")
            return redirect(url_for('contact'))

        # Validate email
        if not validate_email(email):
            flash('Invalid email address!', 'danger')
            logger.warning("Invalid email address.")
            return redirect(url_for('contact'))

        # Check mandatory fields
        if not (first_name and last_name and email and country and message and gender):
            flash('All fields are required!', 'danger')
            logger.warning("Missing mandatory fields.")
            return redirect(url_for('contact'))

        # Check that at least one checkbox is selected
        if not subject:
            flash('Please select at least one subject!', 'danger')
            logger.warning("No subject selected.")
            return redirect(url_for('contact'))

        # If validation passes, redirect to thank you page
        logger.info("Form submission successful.")
        return redirect(url_for('thank_you'))

    return render_template('contact.html', countries=countries)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# run the application directly .checks if the script is being run directly.
if __name__ == '__main__':
    app.run(debug=True)


