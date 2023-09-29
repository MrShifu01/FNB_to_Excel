from openpyxl.worksheet.datavalidation import DataValidation

def apply_data_validations(ws):
    # Assuming you've already set the primary dropdown for column 6
    # Create data validation object
    dv = DataValidation(type="list", formula1='=Category', allow_blank=False)

    # Add validation to cell range
    # Column 6 which corresponds to "F" in Excel. Adjust range if needed.
    dv.add('F2:F1048576')
    ws.add_data_validation(dv)

    # For the dependent dropdown in column 7
    dv_dependent = DataValidation(
        type="list", formula1='INDIRECT($F2)', allow_blank=False)
    dv_dependent.add('G2:G1048576')  # Corresponds to column 7
    ws.add_data_validation(dv_dependent)
    return ws
