import xlrd
import xlwt
import os


CUR_PATH = os.getcwd()
OUTPUT_FILE = "summary.xls"
INPUT_DIR = "在线销售跟踪表"


def merge():
    """
    批量将相同格式的表合并至一个sheet
    """
    files = os.listdir(os.path.join(CUR_PATH, INPUT_DIR))
    # 按序号排序
    files.sort(key=lambda item: item.split(".")[0][-1])

    summary_workbook = xlwt.Workbook()
    summary_sheet = summary_workbook.add_sheet("合并后的sheet")

    row_index = 0
    total_income = 0  # 总收入
    total_return = 0  # 总退货
    total_earning = 0  # 总收益
    for file in files:
        if file.endswith((".xlsx", ".xls")):
            print("正在写入{}".format(file))
            workbook = xlrd.open_workbook(os.path.join(CUR_PATH, INPUT_DIR, file))
            sheet = workbook.sheets()[0]
            rows, cols = sheet.nrows, sheet.ncols  # 行数和列数
            if row_index == 0:
                # 写入第一行的表头
                for i in range(cols):
                    summary_sheet.write(row_index, i, sheet.cell_value(row_index, i))
                row_index += 1

            for i in range(rows)[1:-1]:
                # 去掉第一行表头和最后一行总计
                total_income += sheet.cell_value(i, 5)
                total_return += sheet.cell_value(i, 9)
                total_earning += sheet.cell_value(i, 10)
                for j in range(cols):
                    summary_sheet.write(row_index, j, sheet.cell_value(i, j))
                row_index += 1
        # 每个表格数据之间空一行
        row_index += 1

    # 最后一行写入总计， 分别是1，5，9，10列
    summary_sheet.write(row_index, 1, "总计")
    summary_sheet.write(row_index, 5, total_income)
    summary_sheet.write(row_index, 9, total_return)
    summary_sheet.write(row_index, 10, total_earning)

    summary_workbook.save(os.path.join(CUR_PATH, OUTPUT_FILE))


if __name__ == '__main__':
    merge()