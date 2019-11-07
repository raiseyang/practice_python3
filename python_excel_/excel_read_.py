"""
读取excel文件

序号	唯一ID	                    状态	生产批次	艾拉比注册码
1	051M1186020000191000100001	TRUE
2	051M1186020000191000100002	TRUE
3	051M1186020000191000100003	TRUE
4	051M1186020000191000100004	TRUE
5	051M1186020000191000100005	TRUE
6	051M1186020000191000100006	TRUE

"""
import xlrd


def read(file_name):
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

    # 找出有id的那一列
    id_col = -1
    id_list = []

    for i in range(sheet.ncols):
        print("第一行列名称：", sheet.cell(rowx=0, colx=i))
        if 'ID' in sheet.cell(rowx=0, colx=i).value:
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
        id = sheet.cell(rowx=i, colx=id_col).value
        result_ids.append(id)
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
    read("./file_excel/ids_2019.10.25_out.xls")
