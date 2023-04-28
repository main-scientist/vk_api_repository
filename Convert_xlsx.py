import xlsxwriter as xlsx


class Convert_xlsx:

    @staticmethod
    def create_xlsx_by_list(array: list[str]):
        workbook = xlsx.Workbook('data/Data.xlsx')
        worksheet = workbook.add_worksheet()
        cell_format_for_text = workbook.add_format({
            'text_wrap': True,
            'valign': 'vcenter',
            'border': 1
        })
        border_format = workbook.add_format({'border': 1})
        column_width = 70
        worksheet.set_column('A:A', column_width)

        row, col = 0, 0
        for item in array:
            try:
                worksheet.write(row, col, item, cell_format_for_text)
            except Exception:
                print(item)
            worksheet.write_blank(row, col+1, None, border_format)
            row += 1

        workbook.close()
