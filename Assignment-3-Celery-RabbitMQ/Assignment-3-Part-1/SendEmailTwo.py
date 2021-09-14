from celery import Celery
import smtplib

app = Celery(
    "send_email_service",
    broker="amqp://guest:guest@localhost:5672//"
)

app.conf.task_default_exchange = "send_email_service"
app.conf.task_default_routing_key = "send_email_service"
app.conf.task_default_queue = "send_email_service"

@app.task()
def sendMail(sender , receiver , password , message , num1 , operator , num2):
    choice = operator
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login(sender , password)
    if choice == "+":
        message = "Addition of " + str(num1) + " and " + str(num2) + " is " + str(num1+num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "-":
        message = "Subtraction of " + str(num1) + " and " + str(num2) + " is " + str(num1 - num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "*":
        message = "Multiplication of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "/":
        message = "Division of " + str(num1) + " and " + str(num2) + " is " + str(num1 / num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "**":
        message = "Power of " + str(num1) + " to " + str(num2) + " is " + str(num1 ** num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    else:
        return "Please Select correct choice."