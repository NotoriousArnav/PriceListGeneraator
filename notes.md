# Price List App

## Inputs
1. MRP per unit (MRPpu)
2. Case Size (QTY)

## Constants Used (Decimal/Percentage) 
1. Retail Margin (RMpercent)
2. W/S Margin  (WSMpercent)
3. Ditributor Margin (DistMpercent)
4. SS Margin (SSMpercent)
5. GST (GSTpercent)
6. Import Duty (IDpercent)
7. Trade Discount (TDpercent)
8. Basic Price = IDpercent+TDpercent+1 = basic\_price


## Variables Dependent 
- MRP per Case (MRPpc)
MRPpu\*QTY

- Price to Retail (PtR)
MRPpc/(RMpercent+1)

- Retail Margin (rmargin)
MRPpc-PtR

- Price to W/s (PtWS)
PtR/(WSMpercent+1)

- WS Margin (wsmargin)
PtR-PtWS

- Price to Distributor (PtD)
PtWS/(DistMpercent+1)

- Ditributor Margin (distmargin)
PtWS-PtD

- Price to SS (PtSS)
PtD/(SSMpercent+1)

- SS Margin (SSmargin)
PtD-PtSS

- Net Rate (netrate)
PtSS/(GSTpercent+1)

- GST
PtD-netrate

- Basic Price (basicprice)
netrate/basic\_price

- Import Duty (importduty)
basicprice/(IDpercent+1)

- Trade Discount (td)
basicprice/(TDpercent+1)
