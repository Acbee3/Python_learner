from openpyxl import load_workbook, Workbook
import os, sys
os.chdir(sys.path[0]) # 相对路径错误 

production_path = './工作002/工人产量日报表.xlsx'
template_path = './工作002/检验记录表模板.xlsx'
plan_path = './工作002/生产计划表.xlsx'
save_path = './工作002/8月25日检验记录表.xlsx'

plan_wb = load_workbook(plan_path)
template_wb = load_workbook(template_path)
production_wb = load_workbook(production_path)

plan_sheet = plan_wb.active
template_sheet = template_wb.active
production_sheet = production_wb.active

production_dict = {}

for row in production_sheet.iter_rows(min_row=3, values_only=True):
    workshop_num = row[0][:2] # 车间号
    if not production_dict.get(workshop_num):
        production_dict[workshop_num] = {row[1]: row[4]}
    else:
        if production_dict[workshop_num].get(row[1]):
            production_dict[workshop_num][row[1]] += row[4]
        else:
            production_dict[workshop_num][row[1]] = row[4]
print(production_dict)

for row in plan_sheet.iter_rows(max_col=4, min_row=3, values_only=True):
    actual_production = production_dict[row[1]][row[2]]
    rate = str(round(actual_production / row[3] * 100, 2)) + '%'
    print(rate)
    template_row = row[:4] + (actual_production, rate)
    template_sheet.append(template_row)
    
template_wb.save(save_path)
