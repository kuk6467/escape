from openpyxl import Workbook

wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 현재 활성화된 SHEET 를 가져옴
ws.title = 'NadoSheet'  # 워크시트의 이름을 변경경
wb.save("C:\sparta\escape\Sanghyun\python_example\openpyxl\sample.xlsx")
wb.close()
