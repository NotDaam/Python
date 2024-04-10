from flask import Flask, request
app = Flask (__name__)

@app.route("/saludar")
def saludar():
    return("<p>Hola holaa</p>")

@app.route("/hora")
def hora():
    return("La hora es: ")

@app.route("/factorial")
def factorial():
    fact = 1
    num = int(request.args.get('nro'))
    for x in range(1,num+1):
        fact *= x   
    return str(fact)