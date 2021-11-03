import sys
import os
import json
import argparse
import shutil, errno

# Compiling: pyinstaller -D -F -n rhtml -w "__main__.py"

parser = argparse.ArgumentParser(description="A Python program where you can make use of simple components system.")
parser.add_argument("action", help="The action you wanted to do. It should be either `init` or `build`.")
args = parser.parse_args()

def build():
    filePath = "./src"
    
    errorCount = 0
    
    # if json project file exists
    if os.path.isfile("project.json"):
        # extract pages from json file
        with open("project.json", "r") as data:
            data = json.load(data)
            pages = data["pages"]
    else:
        print("Error: project.json not found, use init command to create project file.")
        sys.exit()

    if os.path.isdir(filePath) == False:
        print("No source code found. Please add source code to 'src' folder.")
        sys.exit()
    
    print("Building from " + filePath + " to ./build")

    if os.path.exists("build") == False:
        os.mkdir("build")

    # copy files from source to build
    if os.path.isdir("./build/"):
        shutil.rmtree("./build/")
    try:
        shutil.copytree(filePath, "./build/")
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise


    for subdir, dirs, files in os.walk("./build"):
        for file in files:
            if file.endswith(".html"):
                # go through every "#include" statement in the file
                with open("./build/" + file) as f:
                    for line in f.readlines():
                        if line.strip().startswith("#include"):
                            # get the file name
                            fileName = line.split("\"")[1]

                            # get the file content
                            if os.path.isfile("./build/" + fileName):
                                f = open("./build/" + fileName, "r")
                                content = f.read()
                                f.close()

                                # replace the "#include" statement with the file content
                                            
                                fr = open("./build/" + file, "r")
                                content = fr.read().replace(line, content)
                                fr.close()

                                f = open("./build/" + file, "w")
                                f.write(content + '\n')
                                f.close()
                            else:
                                print("Error: " + fileName + " not found.")
                                errorCount += 1

    for file in os.listdir("./build"):
        if os.path.isfile(file):
            # remove non-page files
            if file in pages:
                continue
            elif file.endswith(".html"):
                os.remove("./build/" + file)

    print("Build completed with " + str(errorCount) + " errors!")

command = args.action
if command == "init":
    # make json project file
    f = open("project.json", "w")
    f.write("{\n\t\"pages\":[\n\t]\n}")
    f.close()

    # make directory "src"
    if os.path.isdir("./src") == False:
        os.mkdir("src")
elif command == "build":
    build()
