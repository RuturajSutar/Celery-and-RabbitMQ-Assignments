from celery import Celery

app = Celery(
    "Calculator",
    broker="amqp://guest:guest@localhost:5672//"
)

app.conf.task_default_exchange = "Calculator"
app.conf.task_default_routing_key = "Calculator"
app.conf.task_default_queue = "Calculator"

@app.task()
def calculate(a , b):
    print("Select Choice :")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Power")
    choice = input("Enter Your Choice : ")

    if choice == "1":
        return a+b
    elif choice == "2":
        return a-b
    elif choice == "3":
        return a*b
    elif choice == "4":
        return a/b
    elif choice == "5":
        return a**b
    else:
        return "Please Select correct choice."
