# Power BI rebuild notes

The source article describes an Excel-to-Power BI workflow using Power Query for data preparation and month ordering, plus DAX measures for revenue, recorded profit, units sold, average selling price, and margin.

## Suggested measures

```DAX
Revenue = SUM(Sales[Revenue])
Recorded Profit = SUM(Sales[Profit])
Units Sold = SUM(Sales[Units Sold])
Average Selling Price = DIVIDE([Revenue], [Units Sold])
Recorded Profit Margin = DIVIDE([Recorded Profit], [Revenue])
```

## Suggested report pages

1. **Executive overview:** revenue, recorded profit, units sold, average selling price, and margin.
2. **Category performance:** revenue and units sold by category, with a revenue-versus-demand comparison.
3. **Regional growth:** regional revenue, volume, and benchmark analysis.
4. **Brand and customer trends:** brand comparison and customer satisfaction filters where available.
5. **Monthly exploration:** correctly ordered month slicers and trend visuals.

The article does not publish the original Excel workbook or complete row-level tables, so this repository does not invent missing brand, monthly, regional, or satisfaction values.
