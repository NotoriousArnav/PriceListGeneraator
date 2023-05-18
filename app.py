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
    PtR = MRPpc/(constants.RMpercent['value']+1) # Prce to retail
    rmargin = MRPpc-PtR # Retail margin
    PtWS = PtR/(constants.WSpercent['value']+1) # Price to W/S
    wsmargin = PtR-PtWS # W/S Margin
    PtD = PtWS/(constants.DistMargin['value']+1) # Price to Distributor
    distmargin = PtWS-PtD # Distributor Margin
    PtSS = PtD/(constants.SSMargin['value']+1) # Price to SS
    ssmarginn = PtD - PtSS # SS Margin
    netrate = PtSS/(constants.GST['value']+1) # Net Rate
    GST = PtD - netrate # GST
    basic_price = netrate/constants.basic_price['value'] # Basic Price
    importduty = basic_price/(constants.IDpercent['value']+1) # Import Duties
    td = basic_price/(constants.TDpercent+1) # Trade Discount

if __name__ == "__main__":
    constants = Constants('consts.json')
    for var, field in constants.__dict__.items():
        print(f"{var=}\t{field['name']=}\t{field['value']=}")

    print(calculate(50, 200, constants))


