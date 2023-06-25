import xlrd
from xlutils import copy


def write_no_status(file_path, vial_no, experiment_no):
    workbook = xlrd.open_workbook(file_path)
    workbook_new = copy.copy(workbook)
    worksheet = workbook_new.get_sheet(0)
    worksheet.write(experiment_no+1, 14, vial_no)
    worksheet.write(experiment_no+1, 13, 1)
    workbook_new.save(file_path)
