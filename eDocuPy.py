import sqlite3
import json
import xml.etree.ElementTree as ET
import pydoc
import os
import sys
import warnings


warnings.filterwarnings("ignore")

SubModules = {}
SubModuleCounter = 0
ModuleVersion = ''
Continue = True


def eDocuPy(ModuleForDocumentation = '__builtins__' , SubModuleDocumentation = True):

    global SubModules,SubModuleCounter,ModuleVersion #,StoragePath

    StoragePath = os.getcwd() + '\\'

    DefaultClasses = ["<class 'int'>", "<class 'float'>", "<class 'complex'>",
                      "<class 'str'>", "<class 'bool'>", "<class 'list'>",
                      "<class 'set'>", "<class 'tuple'>", "<class 'dict'>",
                      "<class 'frozenset'>", "<class 'bytes'>", "<class 'NoneType'>",
                      ]
    if ModuleForDocumentation in ['','builtins','__builtins__']:
        ModuleName = 'builtins'
        ModuleVersion = ModuleName + '-' + sys.version.split(' ')[0]
        inp = __builtins__
    else:
        try:
            inp = __import__(ModuleForDocumentation.split('.')[0])
            ModuleName = ModuleForDocumentation
        except ModuleNotFoundError as Err:
            os.system("cls")
            print("\n\t",Err,"\n\n"," " * 15, "And / Or\n\n\t","Module has not been installed !!!")
            return None

    if hasattr(inp,'__version__'):
        ModuleVersion = '-' + str(getattr(inp,'__version__')).split(" ")[0]
    elif hasattr(inp,'version'):
        ModuleVersion = '-' + str(getattr(inp,'version')).split(" ")[0]

    print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)) + ') ') * bool(SubModules) + 'Documentation of (',ModuleName,') is in progress ...\n')
    SubFolders = ModuleForDocumentation.split('.')
    SubFolders[0] += ModuleVersion
    StoragePath += '\\'.join(SubFolders) + '\\'
    
    os.makedirs(StoragePath,exist_ok=True)

    _Doc = []
    _Dir = FL(dir(inp),"_")
    _Type = list(map(lambda _ : str(type(getattr(inp,_))) , _Dir))
    _SubDir = list(map(lambda _ : FL(dir(getattr(inp,_)),"_") , _Dir))

    for i in _Dir:
        try:
            _Doc.append(pydoc.render_doc(getattr(inp,i), "%s",renderer=pydoc.plaintext))
        except:
            _Doc.append('No Documentation !!!')
            continue

    SortKey = ["<class 'type'>", "<class 'function'>", "<class 'builtin_function_or_method'>"]
    ModuleExclusiveTypes = [_ for _ in _Type if (not _ in SortKey+["<class 'module'>"])]
    ModuleExclusiveTypes = sorted([(ModuleExclusiveTypes.count(_),_) for _ in set(ModuleExclusiveTypes)],reverse=True)
    ModuleExclusiveTypes = [_[1] for _ in ModuleExclusiveTypes]
    SortKey += ModuleExclusiveTypes
    SortKey += ["<class 'module'>"]
    SortKey = dict((value,len(SortKey)-key) for (key,value) in dict(enumerate(SortKey)).items() )

    O = {}
    OutputFile = ''
    ModuleTag = ET.Element('Module')
    ModuleTag.set('Name', ModuleName)

    db = sqlite3.connect(StoragePath + 'eDocuPy (' + ModuleName + ').sqlite')  # (":memory:")
    cur = db.cursor()

    cur.execute('DROP TABLE IF EXISTS ' + 'eDocuPy')
    cur.execute('CREATE TABLE IF NOT EXISTS ' + 'eDocuPy' + ' (Type TEXT,Object TEXT,"Method(s) / Attribute(s)" TEXT,Documetation TEXT)')

    for i in sorted(zip(_Dir,_Type,_Doc,_SubDir),key=(lambda _ : (SortKey.get(_[1]),len(_[3]))),reverse=True):

        O.setdefault(i[1],{})
        TypeTag = ET.SubElement(ModuleTag, 'Class')
        TypeTag.set('Type',i[1])

        if (i[1] in DefaultClasses) | (i[3] == []):

            O[i[1]].setdefault(i[0],i[2])
            OutputFile +=  FormatDoc('TYPE: ' + i[1],'','','') + FormatDoc('','Object: ' +  ModuleName + '.' + i[0],'','') + FormatDoc('','','Documentation on ' + ModuleName + '.' + i[0] + ':',i[2])

            ObjectTag = ET.SubElement(TypeTag, 'Object')
            ObjectTag.set('Name',ModuleName + '.' + i[0])

            ObjectDoc = ET.SubElement(ObjectTag,'Doc')
            ObjectDoc.text = i[2]

            cur.execute('INSERT INTO ' + 'eDocuPy' + ' (Type,Object,"Method(s) / Attribute(s)",Documetation) VALUES (?,?,?,?)', (i[1],ModuleName + '.' + i[0],'',i[2]))

        else:

            if (i[1] == "<class 'module'>" and ModuleName not in SubModules):
                SubModules.setdefault(ModuleName + '.' + i[0],0)
            elif ModuleName in SubModules:
                SubModules[ModuleName] = 1

            O[i[1]].setdefault(i[0],[[],''])
            O[i[1]][i[0]][0].append(i[3])
            O[i[1]][i[0]][1] = i[2]
            OutputFile +=  FormatDoc('TYPE: ' + i[1],'','','') + FormatDoc('','Object: ' +  ModuleName + '.' + i[0],'','') + FormatDoc('','',r'Method(s) / Attribute(s):',str(i[3])) + FormatDoc('','','Documentation on ' + ModuleName + '.' + i[0] + ':',i[2])

            ObjectTag = ET.SubElement(TypeTag, 'Object')
            ObjectTag.set('Name',ModuleName + '.' + i[0])

            ObjectMethAttr = ET.SubElement(ObjectTag,'Methods_Attributes')
            ObjectMethAttr.text = '\n' + str(i[3])

            ObjectDoc = ET.SubElement(ObjectTag,'Doc')
            ObjectDoc.text = i[2]

            cur.execute('INSERT INTO ' + 'eDocuPy' + ' (Type,Object,"Method(s) / Attribute(s)",Documetation) VALUES (?,?,?,?)', (i[1],ModuleName + '.' + i[0],str(i[3]),i[2]))

    db.commit()
    db.close()

    OutputFile += '\n' + ('*' * 70) + '\n'

    XMLSTR = ET.tostring(ModuleTag)

    with open(StoragePath + 'eDocuPy (' + ModuleName + ').txt',mode='w', encoding="utf-8") as TXTFN:
        TXTFN.write(OutputFile)

    tree = ET.ElementTree(ModuleTag)
    tree.write(StoragePath + 'eDocuPy (' + ModuleName + ').xml')

    JS = json.dumps (O,indent= 5)
    with open(StoragePath + 'eDocuPy (' + ModuleName + ').json',mode='w') as JSNFN:
        json.dump(O,JSNFN)

    print(' '*5 + 'Documentation of (',ModuleName,') is Completed.\n')
    SubModuleCounter += 1

    if SubModuleDocumentation:
        for k,v in SubModules.items():
            if (v == 0):
                eDocuPy(k)
            else:
                continue

    return None

def FL(INP,STR):
    return list(filter(lambda _ : not(_.startswith(STR)) , INP))

def FormatDoc(Type,Object,Method,Doc):
    FDString = (Type + '\n' + '-' * len(Type)) * bool(Type) + ('\n\t' + Object + '\n\t' + '-' * len(Object)) * bool(Object) + ('\n\t' + Method + '\n\t' + '-' * len(Method) + '\n\t\t') * bool(Method)
    for i in Doc.split('\n'):
        FDString += '' + i + '\n\t\t'
    return FDString + '\n'


ModuleNameNotOK = True
while ModuleNameNotOK:
    ModuleForDocumentation = ''
    SubModulesExtraction = False

    os.system("cls")

    ModuleForDocumentation = input("\nEnter an installed (Module Name) to start documentaion process\n\n" + " " * 3 + "Or\n\n" + "Enter (B) to document Builtin module\n\n" + " " * 3 + "Or\n\n" + "Enter (X) to stop:\n\n")

    if ModuleForDocumentation.lower() == 'x':
        ModuleForDocumentation = ''
        SubModulesExtraction = ''
        ModuleNameNotOK = False
        os.system("cls")
        print('\nSee U Soon. Thank you ...')
        quit()
    elif ModuleForDocumentation.lower() == 'b':
        ModuleNameNotOK = False
        ModuleForDocumentation = ''
    else:
        ModuleNameNotOK = False

    SubModuleExtractionNotOK = True
    while SubModuleExtractionNotOK:

        os.system("cls")
        
        SubModulesExtraction = input("\nEnter (True / False) for any subModules to be documented if applicable\n\n" + " " * 3 + "Or\n\n" + "Enter (P) to back to the previous menu\n\n" + " " * 3 + "Or\n\n" + "Enter (X) to stop:\n\n")

        if SubModulesExtraction.lower() in ['true','false']:
            SubModuleExtractionNotOK = False
            SubModulesExtraction = (SubModulesExtraction.capitalize() == 'True')
            eDocuPy(ModuleForDocumentation,SubModulesExtraction)
        elif SubModulesExtraction.lower() == 'x':
            SubModuleExtractionNotOK = False
            ModuleForDocumentation = ''
            SubModulesExtraction = ''
            os.system("cls")
            print('\nSee U Soon. Thank you ...')
            quit()   
        elif SubModulesExtraction.lower() == 'p':
            SubModuleExtractionNotOK = False
            ModuleNameNotOK = True