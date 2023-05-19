# API Documentation

## Calculate API

Calculates the results based on the provided inputs and constant values.

### Endpoint

```
GET /api/calculate
```

### Parameters

- `MRPpu` (float): The MRP per unit.
- `qty` (float): The quantity or case size.

### Query Parameters

- `new_const` (optional): Set this parameter to `true` to use new constant values.

If `new_const` parameter is included, the following query parameters are required:

- `dist_margin` (float): The distributor margin.
- `gst` (float): The GST percentage.
- `id_percent` (float): The import duty percentage.
- `rm_percent` (float): The retail margin percentage.
- `ss_margin` (float): The SS margin percentage.
- `td_percent` (float): The trade discount percentage.
- `ws_percent` (float): The wholesale margin percentage.
- `basic_price` (float): The basic price value.

### Response

A JSON object containing the calculated results.

Example response:

```json
{
  "MRPpc": 150.0,
  "PtR": 120.0,
  "rmargin": 30.0,
  "PtWS": 100.0,
  "wsmargin": 20.0,
  "PtD": 90.0,
  "distmargin": 10.0,
  "PtSS": 80.0,
  "ssmarginn": 10.0,
  "netrate": 72.0,
  "GST": 18.0,
  "basic_price": 60.0,
  "importduty": 54.54545454545454,
  "td": 54.54545454545454
}
```

## Constants API

Retrieves the default or custom constant values used in the calculations.

### Endpoint

```
GET /api/constants
```

### Response

A JSON object containing the constant values.

Example response:

```json
{
  "DistMargin": {
    "name": "Distributor Margin",
    "value": 0.1
  },
  "GST": {
    "name": "GST",
    "value": 0.12
  },
  "IDpercent": {
    "name": "Import Duty",
    "value": 0.1
  },
  "RMpercent": {
    "name": "Retail Margin",
    "value": 0.4
  },
  "SSMargin": {
    "name": "SS Margin",
    "value": 0.05
  },
  "TDpercent": {
    "name": "Trade Discount",
    "value": 0.05
  },
  "WSPercent": {
    "name": "W/S Margin",
    "value": 0.11
  },
  "basic_price": {
    "name": "Basic Price",
    "value": 1.15
  }
}
```
