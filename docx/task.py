from openpyxl import load_workbook, Workbook
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
import os, sys
os.chdir(sys.path[0]) # 相对路径错误 

excel_path = './工作001/封号名单.xlsx'
docTemplate_path = './工作001/法务函模板.docx'
user_path = './工作001/法务函文件/法务函-{}.doc'

wb = load_workbook(excel_path)
ws = wb.active
list = []
# 获取封号dict
for p in ws.iter_rows(min_row=2, values_only=True):
    dict = {}
    dict['name'] = p[0]
    dict['wx_code'] = p[1]
    list.append(dict)

# 打开doc模板
doc = Document(docTemplate_path)

for user in list:
    doc = Document(docTemplate_path)
    para = doc.paragraphs[5]
    run_1 = para.add_run(user['name'])
    run_1.font.size = Pt(14)
    run_1.font.underline = True
    run_1.font.bold = True
    run_2 = para.add_run(f" 同学（WeChat ID: {user['wx_code']}）")
    run_2.font.size = Pt(14)
    doc.save(user_path.format(user['name']))
