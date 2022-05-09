import xlrd

"""
根据excel表，自动替换strings.xml内容
"""

def read(file_name, top_col_name):
    """
    打开excel文件
    :param file_name: excel文件的绝对路径
    :return:
    """
    book = xlrd.open_workbook(filename=file_name)

    print("表单数量:", book.nsheets)
    print("表单名称:", book.sheet_names())
    # 获取第一个表单
    sheet = book.sheet_by_index(0)
    print("表单 {} 共 {} 行 {} 列".format(sheet.name, sheet.nrows, sheet.ncols))

    # 找出有 [中文]  的那一列
    id_col = -1
    id_list = []

    for i in range(sheet.ncols):
        print("第一行列名称：", sheet.cell(rowx=0, colx=i))
        if top_col_name in sheet.cell(rowx=0, colx=i).value:
            id_col = i
            break
    if id_col != -1:
        id_list = list_all_id(sheet, id_col)
    print("ids={}".format(id_list))

    return id_list


def list_all_id(sheet, id_col):
    result_ids = []
    # sheet所有列
    rows = sheet.nrows
    # 扫描ID对应的所有列
    for i in range(1, rows):
        # 获得ID值
        desc = sheet.cell(rowx=i, colx=id_col).value
        result_ids.append(desc)
    return result_ids


def find_col(file_name, key):
    """
    找到第一行包含key的某一列
    :return:
    """
    book = xlrd.open_workbook(filename=file_name)

    # 获取第一个表单
    sheet = book.sheet_by_index(0)

    # 找出有id的那一列
    col = -1
    for i in range(sheet.ncols):
        print("第一行列名称：", sheet.cell(rowx=0, colx=i))
        if key in sheet.cell(rowx=0, colx=i).value:
            col = i
            break
    return col


if __name__ == "__main__":
    list_cn = read("./file_excel/1.xlsx", "中文")
    # list_en = read("./file_excel/1.xlsx", "英文")
    # list_fr = read("./file_excel/1.xlsx", "法语")
    list_de = read("./file_excel/1.xlsx", "德语")

    content_text = ""

    with open('./file_excel/strings.xml', 'r', encoding="utf8") as file:  # with 语法读取file
        content_text = file.read()

    for i in range(len(list_cn)):
        content_text = content_text.replace(">{}<".format(list_cn[i]),">{}<".format(list_de[i]), 1)
    print("content_en:\n" + content_text)
