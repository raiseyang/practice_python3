"""
写入excel文件

序号	唯一ID	                    状态	生产批次	艾拉比注册码
1	051M1186020000191000100001	TRUE
2	051M1186020000191000100002	TRUE
3	051M1186020000191000100003	TRUE
4	051M1186020000191000100004	TRUE
5	051M1186020000191000100005	TRUE
6	051M1186020000191000100006	TRUE

"""
import os
import xlrd
import xlutils.copy as xcopy

from python_excel_ import excel_read_


def write(file_name, active_code_list):
    """
    没有直接提供修改excel的方法，先复制，再写入
    :param active_code_list:
    :return:
    """
    # 打开修改前的文档
    src = xlrd.open_workbook(file_name)
    wb = xcopy.copy(src)
    sheet = wb.get_sheet(0)
    # prn_obj(sheet)
    code_col = excel_read_.find_col(file_name, "注册码")
    if code_col != -1:
        # 开始写
        for i in range(len(active_code_list)):
            print("i={},len={},col={}".format(i, len(active_code_list), code_col))
            sheet.write(i + 1, code_col, active_code_list[i])

        print("所有激活码写入完成")
        wb.save(os.path.join(os.path.dirname(file_name), os.path.basename(file_name) + ".active"))

    return os.path.join(os.path.dirname(file_name), os.path.basename(file_name) + ".active")


def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


if __name__ == '__main__':
    write("./file_excel/ids_2019.10.25_out.xls",
          ['61623031DFDAC35D0', '61623031DFDAC35D1', '61623031DFDAC35D2'])
