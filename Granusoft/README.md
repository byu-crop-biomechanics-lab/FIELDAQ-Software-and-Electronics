# Plant Stalk Measurement Device Software

To run the software, you must have python3 and Kivy installed.

Navigate to the src/ folder in terminal and run:

	python3 main.py

## Compiling the Docmentation as PDF

- Download Doxygen and open Doxyfile and run
	- Make sure to ouput LaTeX files "as an intermediate format for [hyperlinked] PDF"
- Download LaTeX https://www.latex-project.org/get/
- Add LaTeX's binaries and scripts to your PATH
- Run the make file in the LaTeX folder to generate a PDF


## TODO LIST
- When you press save when changing the folder name it crashes. Look at the get and set function and the config.json file 
- Figure out why the config.json is being reset every time the application runs 
