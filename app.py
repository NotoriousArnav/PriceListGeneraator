import json
from pprint import pprint

class Constants:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.__dict__ = json.load(f)

        self.basic_price = {
            "name": "Basic Price",
            "value": self.IDpercent['value'] + self.TDpercent['value'] + 1
        }
def calculate(MRPpu, qty, constants):
    results = {}
    results['MRPpc'] = round(MRPpu * qty, 3) # MRP per Case
    results['PtR'] = round(results['MRPpc'] / (constants.RMpercent['value'] + 1), 3) # Price to retail
    results['rmargin'] = round(results['MRPpc'] - results['PtR'], 3) # Retail margin
    results['PtWS'] = round(results['PtR'] / (constants.WSPercent['value'] + 1), 3) # Price to W/S
    results['wsmargin'] = round(results['PtR'] - results['PtWS'], 3) # W/S Margin
    results['PtD'] = round(results['PtWS'] / (constants.DistMargin['value'] + 1), 3) # Price to Distributor
    results['distmargin'] = round(results['PtWS'] - results['PtD'], 3) # Distributor Margin
    results['PtSS'] = round(results['PtD'] / (constants.SSMargin['value'] + 1), 3) # Price to SS
    results['ssmarginn'] = round(results['PtD'] - results['PtSS'], 3) # SS Margin
    results['netrate'] = round(results['PtSS'] / (constants.GST['value'] + 1), 3) # Net Rate
    results['GST'] = round(results['PtD'] - results['netrate'], 3) # GST
    results['basic_price'] = round(results['netrate'] / constants.basic_price['value'], 3) # Basic Price
    results['importduty'] = round(results['basic_price'] / (constants.IDpercent['value'] + 1), 3) # Import Duties
    results['td'] = round(results['basic_price'] / (constants.TDpercent['value'] + 1), 3) # Trade Discount
    return results

"""
def calculate(MRPpu, qty, constants):
    results = {}
    results['MRPpc'] = MRPpu*qty # MRP per Case
    results['PtR'] = results['MRPpc']/(constants.RMpercent['value']+1) # Prce to retail
    results['rmargin'] = results['MRPpc']-results['PtR'] # Retail margin
    results['PtWS'] = results['PtR']/(constants.WSPercent['value']+1) # Price to W/S
    results['wsmargin'] = results['PtR']-results['PtWS'] # W/S Margin
    results['PtD'] = results['PtWS']/(constants.DistMargin['value']+1) # Price to Distributor
    results['distmargin'] = results['PtWS']-results['PtD'] # Distributor Margin
    results['PtSS'] = results['PtD']/(constants.SSMargin['value']+1) # Price to SS
    results['ssmarginn'] = results['PtD'] - results['PtSS'] # SS Margin
    results['netrate'] = results['PtSS']/(constants.GST['value']+1) # Net Rate
    results['GST'] = results['PtD'] - results['netrate'] # GST
    results['basic_price'] = results['netrate']/constants.basic_price['value'] # Basic Price
    results['importduty'] = results['basic_price']/(constants.IDpercent['value']+1) # Import Duties
    results['td'] = results['basic_price']/(constants.TDpercent['value']+1) # Trade Discount
    return results
"""

if __name__ == "__main__":
    constants = Constants('consts.json')
    print("This is just a proof of Concept.")
    for var, field in constants.__dict__.items():
        print(f"{var=}\t{field['name']=}\t{field['value']=}")
    input("Product Name: ")
    pprint(calculate(float(input("MRP per Unit: ")), float(input("Case Size: ")), constants))


