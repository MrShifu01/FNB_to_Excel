from components.data_preprocessing import preprocess_dataframe
from components.excel_styling import stylize_excel
from components.data_validation import apply_data_validations
from components.excel_utils import (create_excel_from_csv,
                                    add_dataframe_to_excel, 
                                    convert_range_to_table,
                                    deduplicate_rows)

# Path to your CSV and Excel files
csv_file_path = './CSV/63032560921B.csv'
excel_file_path = './EXCEL/output_excel_file.xlsx'
destination_file_path = "C:/Users/ChristianStander/Documents/Personal/Finances/PersonalFinances2.xlsx"

wb = create_excel_from_csv(csv_file_path, excel_file_path)

df = preprocess_dataframe(excel_file_path)

wb, ws = add_dataframe_to_excel(destination_file_path, df)

ws = stylize_excel(ws)

ws = deduplicate_rows(ws)

ws = apply_data_validations(ws)

ws = convert_range_to_table(ws)
# Save the workbook
wb.save(destination_file_path)
