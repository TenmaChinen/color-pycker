# color-pycker

## Description
Desktop Python App to pick colors from anywhere in your screen, just clicking while the pick mode is active, the selected color will be shown as his hex and rgb representation. Finally, just one click to choose which format you need and the text will be copied to your current clipboard.

This app it's just tested on windows system.

- standard library modules used:
 - Tkinter - framework to create simple GUI that already comes installed with python.

 - PIL - mainly used to work with images, but in this case used to take screen captures of one size pixel.

- Project was made entirely in Python 3.9.0, but works in old versions too.

## Setup

- Clone the repository in your local machine.
- Install the needed libraries from requirements.txt with:

  `pip -r requirements.txt`

- You can run the program by clicking directly the file `main.pyw`

- There is no need to execute the program everytime to open it. The program will still running after closin the window.

- To open the window again, just left click the bottom icon from window tools.

- To close the program, just right click on the bottom icon from tools and click `Quit` option.

## Future Work
- Add the functionality to open the window by a shortcut with keyboard library.
- Add color selector functionality to work as a full color picker.
- Make the app more user friendly by converting it as an executable file by Pyinstaller module.

## Screenshots
#### Picking color

![sample_1](https://user-images.githubusercontent.com/36393143/185993249-e20266be-75d7-4ac6-a8d9-5c9b000a8eeb.png)

#### Still running after closing

![sample_2](https://user-images.githubusercontent.com/36393143/185995942-b79dae9c-d5fe-40c9-9d7c-cdcb05fe7b03.png)
