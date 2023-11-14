import openpyxl


def save_row_to_excel(file_path, data):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    sheet.append(data)
    wb.save(file_path)


# Dữ liệu mẫu
data1 = ["a", "a", "ads", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]

# Lưu dữ liệu từng dòng vào tệp Excel
save_row_to_excel("detail scientist/data.xlsx", data1)
