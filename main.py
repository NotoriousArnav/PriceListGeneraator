from flask import Flask, render_template, request, jsonify
from app import calculate, Constants

app = Flask(__name__)
constants = Constants('consts.json')

@app.route('/api/calculate', methods=['GET'])
def calculate_api():
    MRPpu = float(request.args.get('MRPpu'))
    qty = float(request.args.get('qty'))
    results = calculate(MRPpu, qty, constants)

    formatted_results = {
        '14MRPpc': {'name': 'MRP per Case', 'value': results['MRPpc']},
        '12PtR': {'name': 'Price to Retail', 'value': results['PtR']},
        '13rmargin': {'name': 'Retail margin', 'value': results['rmargin']},
        '10PtWS': {'name': 'Price to W/S', 'value': results['PtWS']},
        '11wsmargin': {'name': 'W/S Margin', 'value': results['wsmargin']},
        '08PtD': {'name': 'Price to Distributor', 'value': results['PtD']},
        '09distmargin9': {'name': 'Distributor Margin', 'value': results['distmargin']},
        '06PtSS': {'name': 'Price to SS', 'value': results['PtSS']},
        '07ssmarginn': {'name': 'SS Margin', 'value': results['ssmarginn']},
        '04netrate': {'name': 'Net Rate', 'value': results['netrate']},
        '05GST': {'name': 'GST', 'value': results['GST']},
        '01basic_price': {'name': 'Basic Price', 'value': results['basic_price']},
        '03importduty': {'name': 'Import Duties', 'value': results['importduty']},
        '02td': {'name': 'Trade Discount', 'value': results['td']}
    }

    return jsonify(formatted_results)

@app.route('/')
def calculate_form():
    return render_template('index.html')

"""
@app.route('/', methods=['GET', 'POST'])
def calculate_form():
    if request.method == 'POST':
        MRPpu = float(request.form['MRPpu'])
        qty = float(request.form['qty'])
        results = calculate(MRPpu, qty, constants)
        return render_template('result.html', results=results)
    return render_template('form.html')
"""
if __name__ == '__main__':
    app.run(debug=True)

