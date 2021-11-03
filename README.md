# RHTML
RHTML stands for Reusable-Hyper-Text-Markup-Language, and is pronounced "Rech-tee-em-el" despite how its abbreviation is. 
As the name stands, RHTML is a compiler-like-thing that lets you reuse HTML codes, so you won't have to spend 5 minutes on updating the navbar on your website across all 50+ pages by copy pasting. Well now that I've confused everyone even more, let's get into the actual important stuff.

### Installation
It is as easy as grabbing one of the binaries from [the latest release](https://github.com/TheDuckDev/RHTML/releases/tag/v1.0). You may place the binary anywhere in your system. Adding that directory to your system PATH would make it easier for you. Otherwise you'll have to copy and paste this binary at the root directory of every singlle project. 

Note: RHTML can only be used with Vanilla HTML. Aka it cannot be used with frameworks like NodeJS/ReactJS/etc. Besides there's no need for RHTML to support such frameworks as most of them already has this feature built in. 

### Creating an empty RHTML project
- Run the command `init`.
Windows:
```
./rhtml.exe init
```
Linux:
```
./rhtml init
```

### Integrating RHTML into an existing project
- Run the same command `init`. 
- Move your entire website source code into the newly created `./src` directory.

### Usage
- The newly created `./project.json` JSON file is used to store info about the RHTML project you're working on. It has a pages array, in which you may add the pages that is going to be in the final build. **Note: Not including any files in here will result in the build directory being empty after building. So you must add the .html files' name here.**
- The directory `./src` contains all of the website source code. The RHTML compiler (or transpiler idk) will compile from this directory, to the `./build` directory.
- Reusing another .html file is done by using
```
#include(file.html)
```
*in a new line.* Include in RHTML is very similar to c++ `#include ""`'s. Except, it uses a parenthesis.

### Building
- Run the commmand `build` to build your files. 
Windows:
```
./rhtml.exe build
```
Linux:
```
./rhtml build
```
The build is written to the directory `./build`

Yep that's it. Have fun. :) 
If you have any questions/features/etc., feel free to make a new issue about it. Now this small project of mine is almost finished so I won't be actively working on it. Still, I might do a little bit of improvements.
