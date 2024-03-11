# 2602348: Program Design (Python)
---
* github: https://github.com/prasertcbs/348_2566
* author: [Prasert Kanawattanachai](mailto:prasert.k@chula.ac.th)
* Chulalongkorn Business School
* YouTube: https://youtube.com/prasertcbs
---
# Week 1: 8-Jan-2024
## book
* ประเสริฐ คณาวัฒนไชย (2566), Python ใคร ๆ ก็เขียนโปรแกรมได้: https://www.chulabook.com/computer/189875 
- [ ] [week 1 clips](./week1_clips.md)
## [how to ask question](https://stackoverflow.com/help/how-to-ask)
## Why coding?
- [ ] [Steve Jobs](https://www.youtube.com/watch?v=BRTOlPdyPYU)
- [ ] [Tim Cook: Apple CEO](https://www.businessinsider.com/apple-ceo-tim-cook-coding-should-be-taught-elementary-school-2022-10)
## Why Python
- [ ] [Why Python?](https://realpython.com/world-class-companies-using-python/)
- [ ] [History](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [ ] [Popularity](https://en.wikipedia.org/wiki/Python_(programming_language)#Popularity)
- [ ] [Stack Overflow survey 2023](https://survey.stackoverflow.co/2023/)
## Basic Python
- [ ] Install Python
  - [ ] [Windows](https://youtu.be/NxIwWGKuSco)
    - [ ] `where.exe python`
  - [ ] macOS (preinstalled with macOS)
    - [ ] `python3` instead of `python`
      - [ ] `which python3`
      - [ ] `which python`
    - [ ] `pip3` instead of `pip`
- [ ] IDE (Integrated development environment)
  - [ ] Visual Studio Code
    - [ ] [Download and Install](https://www.youtube.com/playlist?list=PLoTScYm9O0GEo8pnhJb-m-MGVGDvGb4bB)
    - [ ] [Visual Studio Code for Python](https://www.youtube.com/watch?v=D2Q_P5BcgpU&list=PLoTScYm9O0GE-HoYQYU2lsIQblP430ypV)
  - [ ] Jupyter Lab (Python Notebook)
    - [ ] [Installation](https://www.youtube.com/watch?v=TAZluNvUgds&list=PLoTScYm9O0GEour5CiwfSnoutg3RyA76O&index=2)
    - [ ] [Learn](https://www.youtube.com/watch?v=3PkMNsUCAM0&list=PLoTScYm9O0GEour5CiwfSnoutg3RyA76O)
- [ ] [Cheat sheet](https://cheatography.com/sschaub/cheat-sheets/essential-python/)
## Basic Command line
### [Windows command line](https://www.youtube.com/watch?v=C5fCLAA7Mmc&list=PLoTScYm9O0GGpQRdTu3Y8sGA8MsBuojhV)
- [ ] `dir`: list files
- [ ] `md`: make directory
- [ ] `cd`: change directory
- [ ] `copy`: copy file
- [ ] `move`: move file
- [ ] `del`: delete file
### [macOS Terminal command line](https://www.youtube.com/watch?v=-5SI3xFM_3E&list=PLoTScYm9O0GGWXd_4sYsADmM4og6vU1Zh)
- [ ] `ls`: list files
- [ ] `mkdir`: make directory
- [ ] `cd`: change directory
- [ ] `cp`: copy file
- [ ] `mv`: move file
- [ ] `rm`: delete file
- [ ] `man`: command manual
## ตำรา
- บทที่ 1-2 Python ใคร ๆ ก็เขียนโปรแกรมได้
### 1. ทำไมต้องเขียนโค้ด
1.1	โปรแกรมคอมพิวเตอร์คืออะไร
1.2	ทำไมถึงควรเรียนรู้การเขียนโปรแกรม
1.3	ภาษาคอมพิวเตอร์คืออะไร
1.4	Interpreter กับ Compiler
1.5	ตัวอย่างภาษาคอมพิวเตอร์
1.6	ขั้นตอนการทำงานของโปรแกรมคอมพิวเตอร์
1.7	โค้ดที่ดีเป็นอย่างไร
1.8	สรุป
### 2. รู้จักภาษาไพทอน Python
2.1	ภาษาไพทอน
2.2	รูปแบบของภาษาไพทอน
2.3	ฟังก์ชัน print()
2.4	คำอธิบายโค้ด (comment)
2.5	คำสงวน (reserved keywords) ของภาษาไพทอน
2.6	การควบคุมทิศทางการทำงานของโปรแกรม
2.7	สรุป
## First program: Hello World
- [ ] New, Edit, Save, Run Python file
## [Programming concepts](https://www.youtube.com/watch?v=bu6kwrpOqFM&list=PLoTScYm9O0GH4YQs9t4tf2RIYolHt_YwW)
- [ ] IPO (Input-Process-Output)
  - [ ] rock-paper-scissors
- [ ] sample programs:
  - [ ] [come x pay y](https://youtu.be/qqk0iTdmeTA)
  - [ ] [get historical stock prices](https://www.youtube.com/watch?v=U2YMOfGcsvg)
  - [ ] [generate QR Code](https://youtu.be/zjGXl3iLCs8)
  - [ ] [lucky phone number](https://youtu.be/OK5lP47wd3k)
  - [ ] [NATO phonetic](https://youtu.be/3sofYly_vxA)
## Class materials
- [ ] [Python playlist](https://www.youtube.com/playlist?list=PLoTScYm9O0GH4YQs9t4tf2RIYolHt_YwW)
- [ ] [book](https://www.eng.chula.ac.th/th/20535)
- [ ] [tutorial](https://www.tutorialspoint.com/python3/python_overview.htm)
## Clone class materials
- [ ] [install git](https://www.git-scm.com/)
  - [ ] [how to use github](https://www.youtube.com/watch?v=hSQgAA8bj6I&list=PLoTScYm9O0GGsV1ZAyP4m_iyAbflQrKrX)
- [ ] clone git repo to local machine
  - [ ] Windows (`cmd`)
    - [ ] clone repository
      ```bat
      cd %userprofile%
      git clone https://github.com/prasertcbs/348_2566.git lego
      ```
    - [ ] pull latest files from git repo
      ```bat
      cd %userprofile%\lego
      git pull
      ```
  - [ ] Windows (`powershell`)
    - [ ] clone repository
      ```bat
      cd ~
      git clone https://github.com/prasertcbs/348_2566.git lego
      ```
    - [ ] pull latest files from git repo
      ```bat
      cd ~\lego
      git pull
      ```  
  - [ ] mac
    - [ ] clone repository
      ```sh
      cd ~
      git clone https://github.com/prasertcbs/348_2566.git lego
      ```
    - [ ] pull latest files from git repo
      ```sh
      cd ~/lego
      git pull
      ```
## Class exercises
- [ ] find a simple real-world application (e.g., come x pay y, buy 1 get 1 free)
---
# Week 2 (15-Jan-2024)
- [ ] บทที่ 3-4 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] [week 2 clips](week2_clips.md)
## class registration issues
## [how to ask question](https://stackoverflow.com/help/how-to-ask)
## ตำรา 
- บทที่ 3-4 Python ใคร ๆ ก็เขียนโปรแกรมได้
### 3. ตัวแปร (variable)
3.1	ตัวแปร (variable) คืออะไร  
3.2	ประเภทของตัวแปร (variable types)  
3.3	การใช้งานตัวแปร  
3.4	วิธีการตั้งชื่อตัวแปร  
3.5	Static typing กับ Dynamic typing คืออะไร  
3.6	Type hints  
3.7	ขอบเขตของตัวแปร (variable scope)  
3.8	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  
3.9	สรุป  
### 4. ตัวดำเนินการ (operator)
4.1	รู้จักตัวดำเนินการ (operator)  
4.2	ตัวดำเนินการทางคณิตศาสตร์ (Arithmetic operators)  
4.3	ตัวดำเนินการที่ใช้ในการเปรียบเทียบค่า (Comparison operators)  
4.4	ตัวดำเนินการทางตรรกศาสตร์ (Logical operators)  
4.5	ตัวดำเนินการตรวจสอบการเป็นสมาชิก (Membership operators)  
4.6	ตัวดำเนินการเกี่ยวกับสตริง (String operators)  
4.7	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  
4.8	สรุป  

## Extra:
- [ ] Customize your `terminal`
  - [ ] `Windows` (PowerShell)
    - [ ] Install Windows Terminal
    - [ ] [Install PowerShell 7](https://www.youtube.com/watch?v=FFLrObUKgwg)
    - [ ] [Install Oh-my-posh](https://www.youtube.com/watch?v=Soiqw0ooFRM)
    - [ ] [Customize Windows Terminal](https://www.youtube.com/watch?v=hgx1JnU5B4k)
  - [ ] `macOS`
    - [ ] [Install homebrew](https://www.youtube.com/watch?v=48oicKQ2qgQ)
    - [ ] Install iterm2
    - [ ] [Install Oh-my-zsh](https://www.youtube.com/watch?v=-5SI3xFM_3E)
---
# Week 3 (22-Jan-2024)
- [ ] บทที่ 5-6 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] [week 3 clips](week3_clips.md)
- [ ] Pop Quiz 10 points (เนื้อหาในตำราบทที่ 1-6)
## ตำรา 
- บทที่ 5-6 Python ใคร ๆ ก็เขียนโปรแกรมได้
### 5. สตริง (string)
5.1	การกำหนดค่า  
5.2	การใช้งานสตริง  
5.3	การใช้ f-string  
5.4	escape sequences  
5.5	การใช้ raw string  
5.6	การดึงส่วนของสตริงด้วย slicing  
5.7	รู้จักกับรหัส ASCII  
5.8	รู้จักกับรหัส Unicode  
5.9	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  
5.10	สรุป  
### 6. การตรวจสอบเงื่อนไขด้วย if
6.1	ไวยากรณ์  
6.2	การใช้งาน  
6.3	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  
6.4	สรุป  

---
# Week 4 (29-Jan-2024)
- [ ] บทที่ 7 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] [week 4 clips](week4_clips.md)
- [ ] 19-Feb-2024: quiz 40 points
- [ ] 22-Apr-2024: quiz xx points
## ตำรา 
- บทที่ 7 Python ใคร ๆ ก็เขียนโปรแกรมได้
7. การวนซ้ำแบบลูป while  
7.1	ไวยากรณ์  
7.2	การใช้งานลูป while  
7.3	การใช้งานลูป do...while  
7.4	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  
7.5	สรุป  

## How to debug your code
  - [ ] [Python Preview](https://youtu.be/4r4Qb1a1rD4)
  - [ ] [Visual Studio Code Debugger](https://youtu.be/89Ch7ON2Tqg) 


---
# Week 5 (5-Feb-2024)
- [ ] ❗final warning: register google classroom with @student.chula.ac.th account only
- [ ] บทที่ 8 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] [week 5 clips](week5_clips.md)
- [ ] 📢 19-Feb-2024: quiz 40 points
- [ ] 📢 22-Apr-2024: quiz xx points
## ตำรา 
- บทที่ 8 Python ใคร ๆ ก็เขียนโปรแกรมได้
8. การวนซ้ำแบบลูป for  
8.1	ไวยากรณ์  
8.2	การใช้ range()  
8.3	iterable คืออะไร  
8.4	ลูปซ้อนลูป (nested loop)  
8.5	break และ continue  
8.6	เปรียบเทียบลูปแบบ for และ while  
8.7	การใช้ enumerate()  
8.8	การใช้ zip()  
8.9	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  
8.10	สรุป


## Packages/Libraries
- [ ] math
- [ ] random
  - dice
  - coin flip

---
# Week 6 (12-Feb-2024)
- [ ] บทที่ 1-8 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] 📢 19-Feb-2024: quiz 40 points
- [ ] 📢 22-Apr-2024: quiz xx points
## install packages/modules/libraries
- [how to use packages](https://www.youtube.com/watch?v=iNmrsrwjzvE)
  - pip install requests pillow seaborn matplotlib
- [how to import package](https://www.youtube.com/watch?v=tglWu0KGa_M)
  - import random
  - import seaborn as sns
  - from PIL import Image
  - import matplotlib.pyplot as plt
## comprehensive case study (เนื้อหาบทที่ 1-8)
- blindbox
  - list
    - store image URLs
  - random
    - randint
    - randrange
  - [requests image from URL](https://www.youtube.com/watch?app=desktop&v=EUHT7pFaywU)
  - image
    - read
      - local
      - URL
    - display
    - save
    - resize
---
# Week 7 (19-Feb-2024)
- [ ] 📢 19-Feb-2024: quiz 40 points สอบบทที่ 1-8 Python ใคร ๆ ก็เขียนโปรแกรมได้
---
# Week 8 (26-Feb-2024)
- [ ] 📢 วันหยุดราชการ
---
# Week 10 (4-Mar-2024)
- [ ] 📢 ช่วงสอบกลางภาค
---
# Week 11 (11-Mar-2024)
- [ ] บทที่ 13 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] [week 11 clips](week11_clips.md)

## ตำรา 
- บทที่ 13 Python ใคร ๆ ก็เขียนโปรแกรมได้
13. ฟังก์ชัน (function)  
13.1	การใช้งาน  
13.2	ฟังก์ชันที่ดีเป็นอย่างไร  
13.3	ประเภทของฟังก์ชัน  
13.4	เทคนิคการผ่านพารามิเตอร์ให้ฟังก์ชัน  
13.5	ทำไมต้องแยกเขียนส่วนต่าง ๆ ออกเป็นฟังก์ชัน  
13.6	ทำไมต้องเขียนเป็นฟังก์ชัน  
13.7	ตัวอย่างการออกแบบและเขียนฟังก์ชัน  
13.8	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  

## Principles of programming
- [ ] Single Responsibility: Do one thing, do it best
  - [ ] get image
  - [ ] save image
  - [ ] area
    - [ ] rectangle
    - [ ] square
    - [ ] triangle
    - [ ] circle
    - [ ] cylinder
  - [ ] body mass index

---
# Week 12 (18-Mar-2024)
- [ ] บทที่ 13 Python ใคร ๆ ก็เขียนโปรแกรมได้
- [ ] [week 12 clips](week11_clips.md)

## ตำรา 
- บทที่ 13 Python ใคร ๆ ก็เขียนโปรแกรมได้
13. ฟังก์ชัน (function)  
13.1	การใช้งาน  
13.2	ฟังก์ชันที่ดีเป็นอย่างไร  
13.3	ประเภทของฟังก์ชัน  
13.4	เทคนิคการผ่านพารามิเตอร์ให้ฟังก์ชัน  
13.5	ทำไมต้องแยกเขียนส่วนต่าง ๆ ออกเป็นฟังก์ชัน  
13.6	ทำไมต้องเขียนเป็นฟังก์ชัน  
13.7	ตัวอย่างการออกแบบและเขียนฟังก์ชัน  
13.8	ข้อผิดพลาดที่มักพบและวิธีการแก้ไข  