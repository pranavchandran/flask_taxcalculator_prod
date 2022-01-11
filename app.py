from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json

app = Flask(__name__)


# 2022 tax rate finder
def tax_payable(income):
    if income <= 5000_00:
        tax = income * 0.025
    elif income <= 75_000_00:
        tax = 500000 * 0.025 + (income - 500000) * 0.1
    elif income <= 100_000_0:
        tax = 500000 * 0.025 + 250000 * 0.1 + (income - 750000) * 0.15
    return tax


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def tax_calculator():
    if request.method == 'POST':
        # Get the form data
        name = request.form['person']
        income = float(request.form['salary'])
        tax_amount = tax_payable(income)
        # create a json file
        data = {
            'name': name,
            'income': income,
            'tax_amount': tax_amount
        }
        # save it to a json file and append it to the existing file
        with open('data.json', 'a') as f:
            json.dump(data, f)
            f.write(', \n')

        return render_template(
            'index.html',
            name=name,
            income=income,
            tax=tax_amount
        )


if __name__ == '__main__':
    app.run(debug=True)
