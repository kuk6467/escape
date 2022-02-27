from openpyxl import Workbook

wb = Workbook()
# wb.active
ws = wb.create_sheet("mySheet")  # Sheet  이름 변경
ws1 = wb.create_sheet("yourSheet")  # 주어진 이름으로 생성
ws3 = wb.create_sheet("NewSheet", 2)  # 2번째 index에 sheet 생성


ws.sheet_properties.tabColor = 'ff66ff'  # RGB 형태로 값을 넣어주면 탭 색상 변경


print(wb.sheetnames)  # 모든 시트 이름을 확인

# sheet  복사
new_ws = wb['NewSheet']  # Dict 형태로 sheet에 접근
new_ws['A1'] = "Test"  # NewSheet의 A1 부분에 Test 입력
taget = wb.copy_worksheet(new_ws)  # Sheet 복사
taget.title = "Copied Sheet"  # 주어진 탭명으로 변경경

wb.save("C:\sparta\escape\Sanghyun\python_example\openpyxl\sample.xlsx")
wb.close()
