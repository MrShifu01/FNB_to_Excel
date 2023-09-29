from openpyxl.styles import Font, Alignment

def stylize_excel(ws):
    font = Font(name='Arial', size=11)
    alignment = Alignment(horizontal="center", vertical="center")

    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, str):  # Check if the cell value is a string
                cell.value = cell.value.strip()  # Remove leading and trailing whitespace
            cell.font = font
            cell.alignment = alignment
    return ws