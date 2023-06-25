import xlrd
from ProcessOperation import preparation
from ProcessOperation import reaction
from ProcessOperation import sample
from ProcessOperation import clean


def xls_to_json(file_path, experiment_no, worker_id):
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheets()[0]
    values = worksheet.row_values(experiment_no + 1)
    source_id1 = 'not find'
    volume1 = '0.0'
    for i in range(1, 11):
        if type(values[i]) == float:
            source_id1 = worksheet.row_values(1)[i]
            volume1 = values[i]
            break
    data = {'number of process': 4,
            'experiment_No': experiment_no,
            'process1': preparation(source_id1, volume1, worker_id, {}),
            'process2': reaction(worker_id, values[11], values[12], {}),
            'process3': sample(worker_id, {}),
            'process4': clean(worker_id, {})}
    json_str = str(data)
    json_str = json_str.replace("'", '"')
    return json_str

