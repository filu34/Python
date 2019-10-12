print("Hello World!")

matt = "Matt Damon"

mango = False

if mango:
	print("True")
else:
	print("False")

print(matt)

count = 0
while (count < 9):
	print("Number: "), count
	count += 1

print ("good bye!")

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
	name = request.args.get("name", "World")
	return f'Hello, {escape(name)}!'