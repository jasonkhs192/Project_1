from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("Test")
root.resizable(False, False)

#파일 추가 버튼 기능
def add_file():
    files = filedialog.askopenfilenames(title="Select File", filetypes=(("PNG File", "*.png"), ("All File", "*.*")), initialdir="C:/")

    for file in files:
        list_file.insert(END, file)

#파일 삭제 버튼 기능
def delete_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#파일 저장 경로 찾기 버튼 기능
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)

def start():
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Select File")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Select Save Path")
        return

    merge_image()

def merge_image():
    images = [Image.open(x) for x in list_file.get(0,END)]
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    max_widths, total_height = max(widths), sum(heights)


    result_img = Image.new("RGB",(max_widths, total_height), (255, 255, 255))
    y_offset = 0
    for img in images:
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

    dest_path = os.path.join(txt_dest_path.get(), "test.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("notice", "complete")



#파일이라는 프레임 설정. 첫번째 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

#파일 추가 버튼
btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File", command=add_file)
btn_add_file.pack(side="left", padx=5, pady=5)
#파일 삭제 버튼
btn_delete_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete File", command=delete_file)
btn_delete_file.pack(side="right", padx=5, pady=5)

#리스트라는 프레임 설정. 두번째 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

#오른쪽 리스트 프레임에 스크롤바 넣기
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y", padx=5, pady=5)

#리스트 박스를 왼쪽 리스트 프레임에 넣고 expand 시켜 넓히기. 스크롤바 mapping 할수있도록 셋트 하기.
list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True, padx=5, pady=5)

#스크롤바 셋트된곳으로 mapping 하기
scrollbar.config(command=list_file.yview)

#경로 프레임이라는 프레임 설정. 세번째 프레임
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack()

#저장 경로를 경로 프레임에 넣기
txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5)

#저장 경로 찾기 버튼
btn_dest_path = Button(path_frame, text="Search", width=18, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

#옵션이라는 라벨 프레임 설정, 네번째 프레임
frame_option = LabelFrame(root, text="Option")
frame_option.pack()

#Width 을 옵션 프레임에 왼쪽에 넣기
lbl_width = Label(frame_option, text="Width", width=5)
lbl_width.pack(side="left")

#Width 옵션을 리스트 형식으로
opt_width = ["Original", "1024", "800", "640"]

#콤보박스를 이용하여 Width 옵션에 있는 리스트들을 볼수있도록
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=15)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

#Label 을 옵션 프레임에 왼쪽으로 넣기
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

#Label 옵션을 리스트 형식으로
opt_space = ["None", "Tight", "Normal", "Wide"]

#콤보박스를 이용하여 Label 옵션에 있는 리스트를 볼수있도록
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space)
cmb_space.pack(side="left", padx=5, pady=5)

#Label Format 을 옵션 프레임에 왼쪽으로 넣기
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

#Label Format 옵션을 리스트 형식으로
opt_format = ["PNG", "JPG", "BMP", "JPEG"]

#콤보박스를 이용하여 Label Format 옵션에 있는 리스트를 볼수있도록
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format)
cmb_format.pack(side="left", padx=5, pady=5)

#Frame Progress 라는 라벨 프레임 설정. 다섯번째 프레임
frame_progress = LabelFrame(root, text="Status")
frame_progress.pack(fill="x", padx=5, pady=5)

#tkk 라이브러리에 있는 Progressbar 사용하여 진행바 보기
p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

#Frame_run 이라는 프레임 설정. 여섯번째 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

#Close 버튼 생성
btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

#Start 버튼 생성
btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()