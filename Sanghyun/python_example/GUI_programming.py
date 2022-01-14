# tkinter 라이브러리 import
from tkinter import *
from tkinter import messagebox

# tk 객체 인스턴스 생성하기
root = Tk()
root.title("SiSO")
root.geometry("500x500+100+100")
root.resizable(False, False)

count = 0
items = ['국어', '영어', '수학', '과학']


def delete():
    global items
    selection = listbox.curselection()
    if(len(selection) == 0):
        return

    value = listbox.get(selection[0])
    ind = items.index(value)
    del items[ind]
    listbox.delete(selection[0])
    print(items)


def add(event):
    global items
    items.append(entry.get())
    listbox.insert(END, entry.get())
    entry.delete(0, 'end')


def countplus():
    global count
    count += 1
    label.config(text=str(count))


def countminus():
    global count
    count -= 1
    label.config(text=str(count))


def calc(event):
    label.config(text="계산결과: " + str(eval(entry.get())))


def show():
    print("item1: %d,\nitem2: %d,\nitem3: %d\n" %
          (variety1.get(), variety2.get(), variety3.get()))
    messagebox.showinfo("Button Clicked", "item1: {0},\nitem2: {1},\nitem3: {2}\n".format(
        variety1.get(), variety2.get(), variety3.get()))


def selectall():
    bt1.select()
    bt2.select()
    bt3.select()


def deselectall():
    bt1.deselect()
    bt2.deselect()
    bt3.deselect()


# 레이블 생성
label = Label(root, text="0", width=100, height=50,
              bitmap="info", compound="top", relief="solid")
# 레이블을 화면에 배치
label.pack()

# plus 버튼 생성
button1 = Button(root, width=10, text="plus",
                 overrelief="solid", command=countplus)
button1.pack()

# minus 버튼 생성
button2 = Button(root, width=10, text="minus",
                 overrelief="solid", command=countminus)
button2.pack()

# Entry 생성 calc
entry = Entry(root, width=30)
entry.bind("<Return>", calc)
entry.pack()

# listbox 생성
listbox = Listbox(root, height=0, selectmode="extended")

# 리스트 박스에 데이터 추가
for i in range(len(items)):
    # 끝에 삽입,listbox.insert(len(listbox), items[i])
    listbox.insert(END, items[i])
listbox.pack()

# 선택항목 삭제 버튼
buttonDel = Button(root, width=10, text="선택항목 삭제",
                   overrelief="solid", command=delete)
buttonDel.pack()


# Entry 생성 add
entry = Entry(root, width=30)
entry.bind("<Return>", add)
entry.pack()

variety1 = IntVar()
variety2 = IntVar()
variety3 = IntVar()

bt1 = Checkbutton(root, text="item1", variable=variety1)
bt2 = Checkbutton(root, text="item2", variable=variety2)
bt3 = Checkbutton(root, text="item3", variable=variety3)

bt1.pack()
bt2.pack()
bt3.pack()

button = Button(root, width=10, text="Show", overrelief="solid", command=show)
button.pack()
buttonSelectAll = Button(root, width=10, text="전체선택",
                         overrelief="solid", command=selectall)
buttonSelectAll.pack()

buttonDeSelectAll = Button(root, width=10, text="전체취소",
                           overrelief="solid", command=deselectall)
buttonDeSelectAll.pack()


label.mainloop()
