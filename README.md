# 2602348: Program Design (Python)
---
* github: https://github.com/prasertcbs/348_2566
* author: [Prasert Kanawattanachai](mailto:prasert.k@chula.ac.th)
* Chulalongkorn Business School
* YouTube: https://youtube.com/prasertcbs
* clipboard: https://collabedit.com/bpnu5
---
# Week 1: 9-Jan-2023
* [ ] [week 1 clips](./week1_clips.md)
## [how to ask question](https://stackoverflow.com/help/how-to-ask)
## Why coding?
* [ ] [Steve Jobs](https://www.youtube.com/watch?v=BRTOlPdyPYU)
* [ ] [Tim Cook: Apple CEO](https://www.businessinsider.com/apple-ceo-tim-cook-coding-should-be-taught-elementary-school-2022-10)
## Why Python
* [ ] [Why Python?](https://realpython.com/world-class-companies-using-python/)
* [ ] [History](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [ ] [Popularity](https://en.wikipedia.org/wiki/Python_(programming_language)#Popularity)
* [ ] [Stack Overflow survey 2022](https://survey.stackoverflow.co/2022/#technology-most-popular-technologies)
## Basic Python
* [ ] Install Python
  * [ ] [Windows](https://youtu.be/NxIwWGKuSco)
    * [ ] `where.exe python`
  * [ ] macOS (preinstalled with macOS)
    * [ ] `python3` instead of `python`
      * [ ] `which python3`
      * [ ] `which python`
    * [ ] `pip3` instead of `pip`
* [ ] IDE (Integrated development environment)
  * [ ] Visual Studio Code
    * [ ] [Download and Install](https://www.youtube.com/playlist?list=PLoTScYm9O0GEo8pnhJb-m-MGVGDvGb4bB)
    * [ ] [Visual Studio Code for Python](https://www.youtube.com/watch?v=D2Q_P5BcgpU&list=PLoTScYm9O0GE-HoYQYU2lsIQblP430ypV)
  * [ ] Jupyter Lab (Python Notebook)
    * [ ] [Installation](https://www.youtube.com/watch?v=TAZluNvUgds&list=PLoTScYm9O0GEour5CiwfSnoutg3RyA76O&index=2)
    * [ ] [Learn](https://www.youtube.com/watch?v=3PkMNsUCAM0&list=PLoTScYm9O0GEour5CiwfSnoutg3RyA76O)
* [ ] [Cheat sheet](https://cheatography.com/sschaub/cheat-sheets/essential-python/)
## Basic Command line
### [Windows command line](https://www.youtube.com/watch?v=C5fCLAA7Mmc&list=PLoTScYm9O0GGpQRdTu3Y8sGA8MsBuojhV)
* [ ] `dir`: list files
* [ ] `md`: make directory
* [ ] `cd`: change directory
* [ ] `copy`: copy file
* [ ] `move`: move file
* [ ] `del`: delete file
### [macOS Terminal command line](https://www.youtube.com/watch?v=-5SI3xFM_3E&list=PLoTScYm9O0GGWXd_4sYsADmM4og6vU1Zh)
* [ ] `ls`: list files
* [ ] `mkdir`: make directory
* [ ] `cd`: change directory
* [ ] `cp`: copy file
* [ ] `mv`: move file
* [ ] `rm`: delete file
* [ ] `man`: command manual
## First program: Hello World
* [ ] New, Edit, Save, Run Python file
## [Programming concepts](https://www.youtube.com/watch?v=bu6kwrpOqFM&list=PLoTScYm9O0GH4YQs9t4tf2RIYolHt_YwW)
* [ ] IPO (Input-Process-Output)
  * [ ] rock-paper-scissors
* [ ] sample programs:
  * [ ] [come x pay y](https://youtu.be/qqk0iTdmeTA)
  * [ ] [get historical stock prices](https://www.youtube.com/watch?v=U2YMOfGcsvg)
  * [ ] [generate QR Code](https://youtu.be/zjGXl3iLCs8)
  * [ ] [lucky phone number](https://youtu.be/OK5lP47wd3k)
  * [ ] [NATO phonetic](https://youtu.be/3sofYly_vxA)
## Class materials
* [ ] [Python playlist](https://www.youtube.com/playlist?list=PLoTScYm9O0GH4YQs9t4tf2RIYolHt_YwW)
* [ ] [book](https://www.eng.chula.ac.th/th/20535)
* [ ] [tutorial](https://www.tutorialspoint.com/python3/python_overview.htm)
## Clone class materials
* [ ] [install git](https://www.git-scm.com/)
  * [ ] [how to use github](https://www.youtube.com/watch?v=hSQgAA8bj6I&list=PLoTScYm9O0GGsV1ZAyP4m_iyAbflQrKrX)
* [ ] clone git repo to local machine
  * [ ] Windows (`cmd`)
    * [ ] clone repository
      ```bat
      cd %userprofile%
      git clone https://github.com/prasertcbs/348_2566.git lego
      ```
    * [ ] pull latest files from git repo
      ```bat
      cd %userprofile%\lego
      git pull
      ```
  * [ ] Windows (`powershell`)
    * [ ] clone repository
      ```bat
      cd ~
      git clone https://github.com/prasertcbs/348_2566.git lego
      ```
    * [ ] pull latest files from git repo
      ```bat
      cd ~\lego
      git pull
      ```  
  * [ ] mac
    * [ ] clone repository
      ```sh
      cd ~
      git clone https://github.com/prasertcbs/348_2566.git lego
      ```
    * [ ] pull latest files from git repo
      ```sh
      cd ~/lego
      git pull
      ```
## Class exercises
* [ ] find a simple real-world application (e.g., come x pay y, buy 1 get 1 free)
---
# Week 2 (16-Jan-2023)
* [ ] [week 2 clips](./week2_clips.md)
## Program design
* [ ] Interpreter vs. Compiler
* [ ] Whitespace sensitivity
* [ ] variable (w=5, h=2.54, fname='Peter')
* [ ] naming convention
  * [ ] snake case (body_mass_index)
  * [ ] camel case (bodyMassIndex)
  * [ ] Pascal case (BodyMassIndex)
* [ ] data type (int, float, bool, str, tuple, list, dict, ...)
* [ ] flow (sequence, condition, loop)
  * [ ] if...elif...else
    * [ ] rock paper scissors
## Principles of programming
* [ ] Single Responsibility: Do one thing, do it best
  * [ ] area
    * [ ] rectangle
    * [ ] square
    * [ ] triangle
    * [ ] circle
    * [ ] cylinder
  * [ ] body mass index
* [ ] How to debug your code
  * [ ] [Python Preview](https://youtu.be/4r4Qb1a1rD4)
  * [ ] [Visual Studio Code Debugger](https://youtu.be/89Ch7ON2Tqg) 
## Packages/Libraries
* [ ] math
* [ ] random
## Extra
* [ ] Customize your `terminal`
  * [ ] `Windows` (PowerShell)
    * [ ] Install Windows Terminal
    * [ ] [Install PowerShell 7](https://www.youtube.com/watch?v=FFLrObUKgwg)
    * [ ] [Install Oh-my-posh](https://www.youtube.com/watch?v=Soiqw0ooFRM)
    * [ ] [Customize Windows Terminal](https://www.youtube.com/watch?v=hgx1JnU5B4k)
  * [ ] `macOS`
    * [ ] [Install homebrew](https://www.youtube.com/watch?v=48oicKQ2qgQ)
    * [ ] Install iterm2
      * [ ] `brew install --cask iterm2`
    * [ ] [Install Oh-my-zsh](https://www.youtube.com/watch?v=-5SI3xFM_3E)
## Exercises
* [ ] zodiac/horoscope
* [ ] convert score to letter grade
---
# Week 3 (23-Jan-2023)
* [ ] [week 3 clips](./week3_clips.md)
* [ ] [survey form (book and quiz proportion)](https://forms.gle/t6x3Z6W4NWAqhmzW6)
## Variable scope (global, local)
## Function
* [ ] function (just like functions in Excel)
* [ ] function return type
  * [ ] return value(s)
  * [ ] return None
* [ ] bad function
  * [ ] mix input, process and output
  * [ ] do more than one thing
## Static vs Dynamic typing systems
* [ ] Static typing (C, Java)
* [ ] Dynamic typing (Python, JavaScript)
  * [ ] type hints
  * [ ] problem with dynamic typing
    * [ ] rectangle(5, 7)
    * [ ] rectangle("5", 7)
## For Loop
* [ ] range
* [ ] for (simple count up/down)
  * [ ] multiplication table
  * [ ] temperature table

## Keyboard shortcuts
| Action          | Shortcut                                        |
|-----------------|-------------------------------------------------|
| Select line     | <kbd>Ctrl</kbd>+<kbd>L</kbd>                    |
| Unindent code   | <kbd>Ctrl</kbd>+<kbd>[</kbd>                    |
| Indent code     | <kbd>Ctrl</kbd>+<kbd>]</kbd>                    |
| Move line up    | <kbd>Alt</kbd>+<kbd>Up</kbd>                    |
| Move line down  | <kbd>Alt</kbd>+<kbd>Down</kbd>                  |
| Copy line down  | <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>Down</kbd> |
| Format document | <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd>    |

## Exercises
* [ ] count down with time.sleep(1)
  * [ ] print(flush=True)
* [ ] [plot heart with plotly express](./example/heart.ipynb)
* [ ] download pokemon images
  * [ ] need `requests` package
---
# Week 4 (30-Jan-2023)
* [ ] [week 4 clips](./week4_clips.md)
* [ ] **สอบย่อยครั้งที่ 1 วันที่ 27 กุมภาพันธ์ 2566 (20 คะแนน) สอบพร้อมกันทุกคนเริ่มเวลา 9.00 น.**
* [ ] **วันจันทร์ที่ 6 ก.พ. 2566 ขอให้นิสิตทุกคนมาเรียนพร้อมกันตอน 9.00 น.**
* [ ] **มีการเรียนการสอนปกติในวันที่ 20 มีนาคม 2566**
* [ ] google classroom registration using `xxxxxxxxxx@student.chula.ac.th` ONLY
  * [ ] download quiz template
## while loop
* [ ] while
* [ ] break
* [ ] while vs for looop
## String and essential methods
* [ ] concatenate string (+)
* [ ] in
```py
if 'p' in 'open':
  print('yes')
else:
  print('no')
```
* [ ] repeat string (*)
* [ ] upper, lower
* [ ] slice
  * [ ] 6241234526
    * [ ] s[:2] -> 62
  * [ ] Thai National ID
  * [ ] Auspicious phone number (เบอร์มงคล)
* [ ] replace
```py
s='password'
s.replace('s', '$')
```
* [ ] find
* [ ] index
* [ ] startswith
* [ ] endswith
* [ ] join
```py
'-'.join(['J', 'A', 'R', 'V', 'I', 'S'])
```
* [ ] split
  * [ ] CSV
  * [ ] First and Last name
    * [ ] "Peter Parker"
      * [ ] fname = "Peter"
      * [ ] lname = "Parker"
* [ ] isalpha
* [ ] isdigit
  * [ ] sum each digit
## Exercises 
* [ ] เขียนฟังก์ชันเลียนแบบการทำงาน
  * [ ] =LEFT(), =RIGHT(), =MID() ของ Excel
* [ ] acronym
  * [ ] get the first character from each word
* [ ] EAN-13 (product barcode) check digit
---
# Week 5 (6-Feb-2023)
* [ ] [week 5 clips](./week5_clips.md)
* [ ] [basic markdown clips](./markdown.md)
* [ ] **สอบย่อยครั้งที่ 1 วันที่ 27 กุมภาพันธ์ 2566 (20 คะแนน) สอบพร้อมกันทุกคนเริ่มเวลา 9.00 น.**
  * [ ] Closed book quiz
  * [ ] No Internet connection during quiz
* [ ] google classroom registration using `xxxxxxxxxx@student.chula.ac.th` ONLY
  * [ ] download quiz template
## Tuple and List
* [ ] concepts
* [ ] slice
* [ ] iterate list
* [ ] key methods
  * [ ] index
  * [ ] append
  * [ ] remove
* [ ] sum, len
* [ ] multidimensional list
* [ ] list comprehension
* [ ] zip
* [ ] itertools
  * [ ] cycle
## Exercises
* [ ] [Thai National ID check digit](https://th.wikipedia.org/wiki/เลขประจำตัวประชาชนไทย)
---
# Week 6 (20-Feb-2023)
* [ ] **วันจันทร์ที่ 20 ก.พ. 2566 ขอให้นิสิตทุกคนมาเรียนพร้อมกันตอน 9.00 น.**
* [ ] **สอบย่อยครั้งที่ 1 วันที่ 27 กุมภาพันธ์ 2566 (20 คะแนน) สอบพร้อมกันทุกคนเริ่มเวลา 9.00 น.**
  * [ ] Closed book quiz
  * [ ] No Internet connection during quiz
* [ ] google classroom registration using `xxxxxxxxxx@student.chula.ac.th` ONLY
  * [ ] download quiz template
## สรุปทบทวนเนื้อหาที่ผ่านมา
* [ ] ทำ Exercises Week 1 - 5
---