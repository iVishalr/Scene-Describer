# Scene Describer

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![made-with-lua](https://img.shields.io/badge/Made%20With-Lua-%23277cf2)](https://www.lua.org) [![made-with-nodejs](https://img.shields.io/badge/Made%20With-NodeJs-darkgreen)](https://nodejs.org/en/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/SummerProjectCODS/Scene-Describer/graphs/commit-activity)

## Requirements

1. NodeJs 
2. Lua
3. Torch
4. Caffe
5. OpenCV
6. Python3.7
7. ffpmeg
8. moviepy
9. nltk

### Building the project

1. Clone the repository onto your local computer.
2. `$ cd` to the project directory.
3. In the terminal type `$ npm install`

This will install all the node modules required to run the project.

This project requires Lua to be preinstalled locally. To install Lua and its libraries, refer to the [Lua Installation](https://github.com/SummerProjectCODS/Scene-Describer/tree/master/Lua-Installation) folder.

If your do not have node installed, [click here](https://nodejs.org/en/download/). Please download the latest stable version of node.

If you do not have python dependencies (OpenCV, moviepy, ffpmeg, nltk) installed, type `$ pip install -r requirements.txt` in your terminal.

Place data folder, timestamp.json in the previous directory.
Example, if your project is placed in your desktop directory, then both data folder and timestamp.json must be in the desktop directory and not in project directory.

### Executing the project

In your terminal type `$ node app.js` to start a local server. Then go to your browser and make a GET request to `http://localhost:5000/`.

If you make any changes in any of the javascript files, please restart the server to reflect the changes.

Alternatively, you can start your server by typing `$ nodemon app.js` in terminal. This will restart your server automatically when you make changes in the server files.

### Whats public folder?

This is a folder that the server will serve when it gets a GET request from the user. Remember, if you add any image or anything that the user will see, must go to this folder. 

How can I add image to the webpage?

For example, when you add an image to the webpage, do not mention public in the path to the image. This is because the server serves this public folder. 

### Report

We have provided a detailed report of our project. Please refer [Scene Describer](https://github.com/SummerProjectCODS/Scene-Describer/tree/master/Scene_Describer.pdf)
