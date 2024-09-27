# compile easyFrame

import os

def getFiles(path, ext):
    try:    return [f for f in os.listdir(path) if f.endswith(ext) and os.path.isfile(os.path.join(path, f))]
    except: return []

def readFile(path):
    try:    
        with open(path, 'r', encoding='utf-8') as file: content=file.read()
        return content
    except: return ""

def clearText(path):
    clearLines=[]
    for x in readFile(path).split("\n"):
        x=clearLine(x)
        if len(x): clearLines.append(x)
    return "\n".join(clearLines)

def clearLine(line):
    line=line.replace("\n"," ");line=line.replace("\t"," ");line=line.replace("  "," ")
    chars=[]
    for x in line.split(" "):
        if len(x):chars.append(x)
    line=" ".join(chars)    
    line=line.strip()
    line=line.replace("' <!--","'<!--");line=line.replace('" <!--',"'<!--");line=line.replace('"<!--',"'<!--")
    if "'<!--" in line:return line[: line.find("'<!--")]
    else:return line

def getFullCode():
    code=[]
    for x in getFiles("../Framework",".cpd"):code.append(clearText("../Framework/"+x))
    return "\n".join(code)

def writeFile(path,content):file=open(path,"w",encoding="utf-8");file.write(content);file.close()

def getVars(code):
    storage=[]
    onMacro=False
    for x in code.split("\n"):
        if not(onMacro) and x.startswith("#def ") and ("=" in x):
            x=x.replace("#def ","")
            storage.append(x[: x.find("=")].strip()[:])
        elif  not(onMacro) and x.startswith("#def ") and not("=" in x):
            onMacro=True
            x=x.replace("#def ","")
            storage.append(x.strip()[:])
        elif onMacro and x.startswith("#end def"):
            onMacro=False
        elif not(onMacro) and ("=" in x):
            storage.append(x[: x.find("=")].strip()[:])
    storage=list(set(storage))
    storage.sort()
    var=[]
    macros=[]
    for x in storage:
        if "$" in x:macros.append([x[: x.find("(")].strip()[:],x[::]])
        else: var.append(x[::])
    return [var,macros]

def makeREADME(varArray):
    txt="# EasyFrame -  by Edwin Saul\n\n"
    for x in varArray[0]:
        txt+="### "+x+"\n  framework variable\n\n"
    for x in varArray[1]:
        txt+="### "+x[0]+"\n  "+x[1]+"\n\n"
    writeFile("./README.md",txt)


fullCode=getFullCode()
writeFile("../EasyFrame.cpd",fullCode)
writeFile("../Examples/easyFrame.cpd",fullCode)
libvars=getVars(fullCode)
makeREADME(libvars)



