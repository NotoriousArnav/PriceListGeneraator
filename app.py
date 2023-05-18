import json

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

if __name__ == "__main__":
    constants = Constants('consts.json')
    for var, field in constants.__dict__.items():
        print(f"{var=}\t{field['name']=}\t{field['value']=}")

    print(calculate(50, 200, constants))


