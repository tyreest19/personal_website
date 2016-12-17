from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import smtplib

app = Flask(__name__,template_folder='template',static_url_path = '/static')

@app.route("/" , methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        sender_email = request.form['user_mail']
        sender_name = request.form['user_name']
        sender_message = request.form['user_message']
        send_email(sender_email,sender_message,sender_name)
        redirect("/",code=200)
    return render_template("index.html")

def send_email(email_recipient,message,sender_name):
    fromaddr  = 'tyreeostevenson@gmail.com'
    toaddrs = fromaddr
    # Credentials (if needed)
    username = fromaddr
    password = 'tyree283'
    message += "\n" + "  sender name is " + sender_name
    message += "\n" + "  sender email is " + email_recipient
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr,email_recipient,"Thanks for the email and I will respond soon as possible.")
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()


if __name__ == "__main__":
    app.run(debug=True)