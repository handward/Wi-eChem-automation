import xlrd


def experiment_no(file_path):
    # return the first experiment_no according to the user.xls
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheets()[0]
    values = worksheet.col_values(13)
    No = 21
    for i in range(2, len(values)):
        if values[i] == 0:
            No = i - 1
            break
    k = [No, len(values)]
    return k
# print(experiment_no(r'C:\Users\15239\Desktop\labview multichannel v314\user.xls'))
