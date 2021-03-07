# Scene Describer

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![made-with-lua](https://img.shields.io/badge/Made%20With-Lua-%23277cf2)](https://www.lua.org) [![made-with-nodejs](https://img.shields.io/badge/Made%20With-NodeJs-darkgreen)](https://nodejs.org/en/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/iVishalr/Scene-Describer/graphs/commit-activity)

This project was done as a part of Summer Project organized by the CODS Community of PES University. I would like to thank CODS for giving us this opportunity. Thank You!

I'm just leaving this project here for academic and non-commercial use only.

## Contributors

[Vishal R \*](https://github.com/iVishalr)

[Royston E Tauro \*](https://github.com/lucasace)

*\*(Equal Contributions)*

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

This project requires Lua to be preinstalled locally. To install Lua and its libraries, refer to the [Lua Installation](https://github.com/iVishalr/Scene-Describer/tree/master/Lua-Installation) folder. Please make sure you have not skipped the above step. You must also download the model weights depending on the hardware you have in your system. 

If your do not have node installed, [click here](https://nodejs.org/en/download/). Please download the latest stable version of node.

If you do not have python dependencies (OpenCV, moviepy, ffpmeg, nltk) installed, type `$ pip install -r requirements.txt` in your terminal.

Place data folder, timestamp.json in the previous directory.
Example, if your project is placed in your desktop directory, then both data folder and timestamp.json must be in the desktop directory and not in project directory.

### Executing the project

In your terminal type `$ node app.js` to start a local server. Then go to your browser and make a GET request to `http://localhost:5000/`.

If you make any changes in any of the javascript files, please restart the server to reflect the changes.

Alternatively, you can start your server by typing `$ nodemon app.js` in terminal. This will restart your server automatically when you make changes in the server files.


### Report

We have provided a detailed report of our project. Please refer [Scene Describer](https://github.com/iVishalr/Scene-Describer/tree/master/Scene_Describer.pdf)
