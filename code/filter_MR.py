import pandas as pd
import numpy as np

source_data = pd.read_csv("../source/MR_report.csv")

source_data = source_data.drop(columns=['report_html', 'report_image', 'uploaded', 'history', 'finish_date',
                                        'finish_time', 'upload_text', 'his2wkl_assign', 'PROC_FLAG', 'assign', 'CHECK1', 'VER1'])

source_data['report_uid'] = source_data['report_uid'].str[21:33]

source_data['ICD'] = ""

# for index, row in source_data.iterrows():
#     if 'I61' in row['report_text']:
#         source_data["ICD"][index] = 'I61'
#     elif 'I62' in row['report_text']:
#         source_data["ICD"][index] = 'I62'
#     elif 'I63' in row['report_text']:
#         source_data["ICD"][index] = 'I63'
#     elif 'I64' in row['report_text']:
#         source_data["ICD"][index] = 'I64'
#     elif 'I65' in row['report_text']:
#         source_data["ICD"][index] = 'I65'
#     elif 'I66' in row['report_text']:
#         source_data["ICD"][index] = 'I66'
#     elif 'I67' in row['report_text']:
#         source_data["ICD"][index] = 'I67'
#     elif 'I68' in row['report_text']:
#         source_data["ICD"][index] = 'I68'
#     elif 'I69' in row['report_text']:
#         source_data["ICD"][index] = 'I69'
#     elif 'S06' in row['report_text']:
#         source_data["ICD"][index] = 'S06'
#     elif 'No image evidence of acute infarct, intracranial hemorrhage' in row['report_text']:
#         source_data["ICD"][index] = 'normal'
#     elif 'No image evidence of cerebral infarct, intracranial hemorrhage' in row['report_text']:
#         source_data["ICD"][index] = 'normal'
#     elif 'No evident space-occupying lesion, infarction and hemorrhage' in row['report_text']:
#         source_data["ICD"][index] = 'normal'
#     elif 'No obvious intracranial hemorrhage' in row['report_text']:
#         source_data["ICD"][index] = 'normal'
#     else:
#         source_data["ICD"][index] = 'other'

for index, row in source_data.iterrows():
    if 'No image evidence of acute infarct, intracranial hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'normal'
    elif 'No image evidence of cerebral infarct, intracranial hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'normal'
    elif 'No evident space-occupying lesion, infarction and hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'normal'
    elif 'No obvious intracranial hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'normal'
    elif 'No intracranial hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'normal'
    elif 'Intracranial hemorrhage: None' in row['report_text']:
        source_data["ICD"][index] = 'normal'
    elif 'no evidence of acute intracranial hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'normal'

    elif 'I61' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'I62' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'I63' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'S06' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'Intracranial hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'ICH' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'Subarachnoid hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'SAH' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'Subdural hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'SDH' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'Epidural hemorrhage' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'EDH' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'lacunar infarcts' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'hypoplasia' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'ischemic infarcts' in row['report_text']:
        source_data["ICD"][index] = 'stroke'
    elif 'segmental stenosis' in row['report_text']:
        source_data["ICD"][index] = 'stroke'

    else:
        source_data["ICD"][index] = 'other'

source_data.to_csv('../output/output_MR_report.csv', index=False)

source_data = source_data.drop(columns=['report_text'])
source_data.to_csv('../output/output_MR.csv', index=False)

print(source_data)
