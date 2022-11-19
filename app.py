import random
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dev = "ENV"

if dev == "ENV":
    app.debug = True


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jamesbond@localhost/feedbackk'


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# class Feedback(db.Model):
#     __tablename__ = 'message'

#     id = db.Column(db.Integer, primary_key=True)
#     Roll_Number = db.Column(db.Integer)
#     name = db.Column(db.String(40))
#     email = db.Column(db.String(40))
#     rating = db.Column(db.Integer)
#     message = db.Column(db.String)
#     course = db.Column(db.String)

#     def __int__(self, name, Roll_Number, email, rating, message, course):
#         self.name = name
#         self.email = email
#         self.rating = rating
#         self.message = message
#         self.course = course
#         self.Roll_Number = Roll_Number


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        Roll_Number = request.form['roll_no']
        emaill = request.form['email']
        course = request.form['service']
        rating = request.form['rating']
        message = request.form['message']
        if name == '' or Roll_Number == '' or emaill == '' or course == 'Select Course' or rating == 'Select Rating' or message == '':
            return render_template('index.html', mess=" Please Enter all required Fields ")
        else:

            # if db.session.query(Feedback).filter(Feedback.Roll_Number == Roll_Number).count() == 0:
            #      data = Feedback(name, Roll_Number, email, rating, message, course)
            #      db.session.add(data)
            #      db.session.commit()
            het = str(Roll_Number) + ".txt"
            #  path = "A:\gama\database" + het
            path = f"A:\gama\{het}"
            print(path)
            isFile = os.path.isfile(path)
            if isFile:
                return render_template("already_submitted.html")
            else:
                # completeName = het
                # with open(os.path.join("A:\gama\database", completeName), "w") as file1:
                # toFile = input(str(message))
                # file1.write(toFile)
                info = "Name : " + str(name) + "\nRoll Number : " + str(Roll_Number) + "\nEmail : " + str(
                    emaill) + "\nRating : " + str(rating) + "\nFeedback : " + str(message)
                thanking="<b> \n\n\nThanks For Your Feedback </b>"
                with open(het, "w") as file1:
                    file1.write(info)

                email = EmailMessage()
                email['from'] = 'James Bond'
                email['to'] = emaill
                email['subject'] = "Feedback"

                #email.set_content(f"Your feedback is appreciated {name},we will contact you soon\n\n Your rating for "
                #                  f"Nitra Technical Campus is: \t{rating}\n\n Feedback: \t{message}")
                email.set_content(info+thanking)
                with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login("kakagems26@gmail.com", "jhljvkxkvzcuaanx")
                    smtp.send_message(email)

                return render_template('godlike.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
    )
