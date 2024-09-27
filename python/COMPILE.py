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

def writeFile(path,content):file=open(path,content);file.write(content);file.close()


fullCode=getFullCode()
writeFile("../easyFrame.cpd",fullCode)

