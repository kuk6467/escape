from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Sanghyun Sheet"

# worksheet 에 값을 입력
ws["A1"] = 1
ws["A2"] = 2
ws["A3"] = 3

# 소문자로 해도 들어갑니다.
ws["b1"] = 4
ws["b2"] = 5
ws["b3"] = 6

print(ws["A1"])  # a1의 셀 정보를 출력  <Cell 'Sanghyun Sheet'.A1>
print(ws["A1"].value)  # 1
print(ws["A10"].value)  # 값이 없을 때 "None" 을 출력


# row = 1,2,3,4 ... 렬
# column = a(1),b(2),c(3)... 행
print(ws.cell(row=1, column=1).value)  # ws["A1"].value
print(ws.cell(row=1, column=2).value)  # ws["B1"].value

c = ws.cell(column=3, row=1, value=10)  # ws["C1"].value =10
print(c.value)

wb.save("C:\sparta\escape\Sanghyun\python_example\openpyxl\sample.xlsx")
wb.close()
