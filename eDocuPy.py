import sqlite3
import json
import xml.etree.ElementTree as ET
import pydoc
import os
import sys
import warnings
import shutil


warnings.filterwarnings("ignore")

SubModules = {}
SubModuleCounter = 0
<<<<<<< HEAD
ModuleVersion = ''
Continue = True
||||||| ee519fd (Some Bugs Fixed)
#ModuleVersion = ''
LogFile = ''
PackageHandler = ''
PKGs = dict([(MName,(IsPack,MPath)) for (MPath,MName,IsPack) in pkgutil.iter_modules(None,'')])
StoragePath = ''
StorageSubFolders = ''
OutputFolder = ''
LogFilePath = ''
=======
<<<<<<< HEAD
#ModuleVersion = ''
LogFile = ''
PackageHandler = ''
PKGs = dict([(MName,(IsPack,MPath)) for (MPath,MName,IsPack) in pkgutil.iter_modules(None,'')])
StoragePath = ''
StorageSubFolders = ''
OutputFolder = ''
LogFilePath = ''
||||||| d90b2e4
ModuleVersion = ''
Continue = True
=======
#ModuleVersion = ''
LogFile = ''
PackageHandler = ''
PKGs = dict([(MName,IsPack) for (MPath,MName,IsPack) in pkgutil.iter_modules(None,'')])
StoragePath = ''
StorageSubFolders = ''
OutputFolder = ''
LogFilePath = ''
>>>>>>> a078e210a69c83d1b585111c2421cfc337b2fda7
>>>>>>> parent of ee519fd (Some Bugs Fixed)

def eDocuPy(ModuleForDocumentation = '__builtins__' , SubModuleDocumentation = True):

    global SubModules,SubModuleCounter,ModuleVersion

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

<<<<<<< HEAD
    if hasattr(inp,'__version__'):
        ModuleVersion = '-' + str(getattr(inp,'__version__')).split(" ")[0]
    elif hasattr(inp,'version'):
        ModuleVersion = '-' + str(getattr(inp,'version')).split(" ")[0]
||||||| ee519fd (Some Bugs Fixed)
            ModuleName = getattr(inp,'__name__') #ModuleForDocumentation
            if hasattr(inp,'__file__'):
                ModuleFilePath.append(os.path.dirname(inp.__file__))
            else:
                ModuleFilePath.append(PKGs[ModuleForDocumentation.split('.')[0]][1].path + '\\' + '\\'.join(ModuleForDocumentation.split('.')))#ModuleFilePath.append(os.path.dirname(inp.__file__))
            print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of (',ModuleName,') is in progress ...\n')
=======
<<<<<<< HEAD
            ModuleName = getattr(inp,'__name__') #ModuleForDocumentation
            if hasattr(inp,'__file__'):
                ModuleFilePath.append(os.path.dirname(inp.__file__))
            else:
                ModuleFilePath.append(PKGs[ModuleForDocumentation.split('.')[0]][1].path + '\\' + '\\'.join(ModuleForDocumentation.split('.')))#ModuleFilePath.append(os.path.dirname(inp.__file__))
            print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of (',ModuleName,') is in progress ...\n')
||||||| d90b2e4
    if hasattr(inp,'__version__'):
        ModuleVersion = '-' + str(getattr(inp,'__version__')).split(" ")[0]
    elif hasattr(inp,'version'):
        ModuleVersion = '-' + str(getattr(inp,'version')).split(" ")[0]
=======
            ModuleFilePath.append(os.path.dirname(inp.__file__))
            ModuleName = getattr(inp,'__name__') #ModuleForDocumentation
            print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of (',ModuleName,') is in progress ...\n')
>>>>>>> a078e210a69c83d1b585111c2421cfc337b2fda7
>>>>>>> parent of ee519fd (Some Bugs Fixed)

    print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)) + ') ') * bool(SubModules) + 'Documentation of (',ModuleName,') is in progress ...\n')
    SubFolders = ModuleForDocumentation.split('.')
    SubFolders[0] += ModuleVersion
    StoragePath += '\\'.join(SubFolders) + '\\'
    
    os.makedirs(StoragePath,exist_ok=True);os.makedirs(StoragePath + '\\#eDocuPy (' + ModuleName + ')\\',exist_ok=True)

<<<<<<< HEAD
    _Doc = []
    _Dir = FL(dir(inp),"_")
||||||| ee519fd (Some Bugs Fixed)
            print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of ( ',ModuleForDocumentation,' ) is in progress ...\n')
            print("\n\t",Err,'!!!') #,"\n\n"," " * 15, "And / Or\n\n\t", "Module has not been installed yet !!!\n\n")
            
            LogFile += "*** Error Ocurred During the Documentation of ( " + ModuleForDocumentation + " ) : " + str(Err) + '!!!\n'

            with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
                LOGFILE.write(LogFile)

            SubModuleCounter += 1
            SubModules[ModuleForDocumentation] = 1

            return 'ErrorOccured'

    if ModuleName == '' : return 'ErrorOccured'

    if SubModules == {} :
        with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
            LOGFILE.write(LogFile)        

        if PKGs.get(inp.__name__,False)[0] and SubModuleDocumentation:
            SortedSubModules = sorted([ModuleForDocumentation] + [MName for (MPath,MName,IsPack) in pkgutil.walk_packages(ModuleFilePath,inp.__name__+'.',lambda i : None) if not(MName.endswith('__main__'))],key=lambda i:(i.count('.'),i) )
            SubModules = {i:0 for i in SortedSubModules}

    SubFolders = ModuleForDocumentation.split('.')[1:]
    StorageSubFolders = '\\' * bool(SubFolders) + '\\'.join(SubFolders) + '\\'
    TempFolder = tempfile.mkdtemp() + '\\'
    os.makedirs(TempFolder ,exist_ok=True)
    os.makedirs(StoragePath + StorageSubFolders,exist_ok=True)

    _Dir = [i for i in dir(inp) if str(type(getattr(inp,i))) != "<class 'module'>"] #FL(dir(inp))
=======
<<<<<<< HEAD
            print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of ( ',ModuleForDocumentation,' ) is in progress ...\n')
            print("\n\t",Err,'!!!') #,"\n\n"," " * 15, "And / Or\n\n\t", "Module has not been installed yet !!!\n\n")
            
            LogFile += "*** Error Ocurred During the Documentation of ( " + ModuleForDocumentation + " ) : " + str(Err) + '!!!\n'

            with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
                LOGFILE.write(LogFile)

            SubModuleCounter += 1
            SubModules[ModuleForDocumentation] = 1

            return 'ErrorOccured'

    if ModuleName == '' : return 'ErrorOccured'

    if SubModules == {} :
        with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
            LOGFILE.write(LogFile)        

        if PKGs.get(inp.__name__,False)[0] and SubModuleDocumentation:
            SortedSubModules = sorted([ModuleForDocumentation] + [MName for (MPath,MName,IsPack) in pkgutil.walk_packages(ModuleFilePath,inp.__name__+'.',lambda i : None) if not(MName.endswith('__main__'))],key=lambda i:(i.count('.'),i) )
            SubModules = {i:0 for i in SortedSubModules}

    SubFolders = ModuleForDocumentation.split('.')[1:]
    StorageSubFolders = '\\' * bool(SubFolders) + '\\'.join(SubFolders) + '\\'
    TempFolder = tempfile.mkdtemp() + '\\'
    os.makedirs(TempFolder ,exist_ok=True)
    os.makedirs(StoragePath + StorageSubFolders,exist_ok=True)

    _Dir = [i for i in dir(inp) if str(type(getattr(inp,i))) != "<class 'module'>"] #FL(dir(inp))
||||||| d90b2e4
    _Doc = []
    _Dir = FL(dir(inp),"_")
=======
            print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of ( ',ModuleForDocumentation,' ) is in progress ...\n')
            print("\n\t",Err,'!!!') #,"\n\n"," " * 15, "And / Or\n\n\t", "Module has not been installed yet !!!\n\n")
            
            LogFile += "*** Error Ocurred During the Documentation of ( " + ModuleForDocumentation + " ) : " + str(Err) + '!!!\n'

            with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
                LOGFILE.write(LogFile)

            SubModuleCounter += 1
            SubModules[ModuleForDocumentation] = 1

            return 'ErrorOccured'

    if ModuleName == '' : return 'ErrorOccured'

    if SubModules == {} :
        with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
            LOGFILE.write(LogFile)        

        if PKGs.get(inp.__name__,False) and SubModuleDocumentation:
            SortedSubModules = sorted([ModuleForDocumentation] + [MName for (MPath,MName,IsPack) in pkgutil.walk_packages(ModuleFilePath,inp.__name__+'.',lambda i : None) if not(MName.endswith('__main__'))],key=lambda i:(i.count('.'),i) )
            SubModules = {i:0 for i in SortedSubModules}

    SubFolders = ModuleForDocumentation.split('.')[1:]
    StorageSubFolders = '\\' * bool(SubFolders) + '\\'.join(SubFolders) + '\\'
    TempFolder = tempfile.mkdtemp() + '\\'
    os.makedirs(TempFolder ,exist_ok=True)
    os.makedirs(StoragePath + StorageSubFolders,exist_ok=True)

    _Dir = dir(inp) #FL(dir(inp))
>>>>>>> a078e210a69c83d1b585111c2421cfc337b2fda7
>>>>>>> parent of ee519fd (Some Bugs Fixed)
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

<<<<<<< HEAD
||||||| ee519fd (Some Bugs Fixed)
    DataObjects = (set(ModuleExclusiveTypes).union(DefaultClasses))
    _SubDir = []
    _Doc = []    
    
    for _ in _Dir:
        try:
            ObjAttr = getattr(inp,_)
            #if inspect.ismodule(ObjAttr):
            #    _SubDir.append(repr(ObjAttr))
            #    _Doc.append('Module Dependencies')
            #elif str(type(ObjAttr)) in DataObjects:
            if str(type(ObjAttr)) in DataObjects:
                _SubDir.append(repr(ObjAttr))
                _Doc.append('DATA')
            else:
                _SubDir.append(FL(dir(ObjAttr)))
                _Doc.append(pydoc.render_doc(ObjAttr, "%s",renderer=pydoc.plaintext))
        
        except BaseException:
            _Doc.append('No Documentation !!!')
            continue

=======
<<<<<<< HEAD
    DataObjects = (set(ModuleExclusiveTypes).union(DefaultClasses))
    _SubDir = []
    _Doc = []    
    
    for _ in _Dir:
        try:
            ObjAttr = getattr(inp,_)
            #if inspect.ismodule(ObjAttr):
            #    _SubDir.append(repr(ObjAttr))
            #    _Doc.append('Module Dependencies')
            #elif str(type(ObjAttr)) in DataObjects:
            if str(type(ObjAttr)) in DataObjects:
                _SubDir.append(repr(ObjAttr))
                _Doc.append('DATA')
            else:
                _SubDir.append(FL(dir(ObjAttr)))
                _Doc.append(pydoc.render_doc(ObjAttr, "%s",renderer=pydoc.plaintext))
        
        except BaseException:
            _Doc.append('No Documentation !!!')
            continue

||||||| d90b2e4
=======
    DataObjects = (set(ModuleExclusiveTypes).union(DefaultClasses))
    _SubDir = []
    _Doc = []    
    
    for _ in _Dir:
        try:
            ObjAttr = getattr(inp,_)
            if inspect.ismodule(ObjAttr) | \
                (str(type(ObjAttr)) in DataObjects) :
                _SubDir.append(repr(ObjAttr))
                _Doc.append('')
            else:
                _SubDir.append(FL(dir(ObjAttr)))
                _Doc.append(pydoc.render_doc(ObjAttr, "%s",renderer=pydoc.plaintext))
        
        except BaseException:
            _Doc.append('No Documentation !!!')
            continue

>>>>>>> a078e210a69c83d1b585111c2421cfc337b2fda7
>>>>>>> parent of ee519fd (Some Bugs Fixed)
    O = {}
    OutputFile = '' ; SepratedOutputFile = ''
    ModuleTag = ET.Element('Module')
    ModuleTag.set('Name', ModuleName)

    db = sqlite3.connect(StoragePath + '#eDocuPy (' + ModuleName + ').sqlite')  # (":memory:")
    cur = db.cursor()

    cur.execute('DROP TABLE IF EXISTS ' + 'eDocuPy')
    cur.execute('CREATE TABLE IF NOT EXISTS ' + 'eDocuPy' + ' (Type TEXT,Object TEXT,"Method(s) / Attribute(s)" TEXT,Documetation TEXT)')

    for i in sorted(zip(_Dir,_Type,_Doc,_SubDir),key=(lambda _ : (SortKey.get(_[1]),len(_[3]))),reverse=True):

        O.setdefault(i[1],{})
        TypeTag = ET.SubElement(ModuleTag, 'Class')
        TypeTag.set('Type',i[1])

        if (i[1] in DefaultClasses) | (i[3] == []):

            O[i[1]].setdefault(i[0],i[2])

            SepratedOutputFile =  FormatDoc('TYPE: ' + i[1],'','','') + FormatDoc('','Object: ' +  ModuleName + '.' + i[0],'','') + FormatDoc('','','Documentation on ' + ModuleName + '.' + i[0] + ':',i[2])
            OutputFile +=  SepratedOutputFile

            ObjectTag = ET.SubElement(TypeTag, 'Object')
            ObjectTag.set('Name',ModuleName + '.' + i[0])

            ObjectDoc = ET.SubElement(ObjectTag,'Doc')
            ObjectDoc.text = i[2]
            
            with open(StoragePath + '\\#eDocuPy (' + ModuleName + ')\\' + i[1].replace('<','(').replace('>',')') + ' ~ ' + ModuleName + '.' + i[0] + '.txt',mode='w', encoding="utf-8") as TXTFN:
                TXTFN.write(SepratedOutputFile)

            cur.execute('INSERT INTO ' + 'eDocuPy' + ' (Type,Object,"Method(s) / Attribute(s)",Documetation) VALUES (?,?,?,?)', (i[1],ModuleName + '.' + i[0],'',i[2]))

        else:

            if (i[1] == "<class 'module'>" and ModuleName not in SubModules):
                SubModules.setdefault(ModuleName + '.' + i[0],0)
            elif ModuleName in SubModules:
                SubModules[ModuleName] = 1

            O[i[1]].setdefault(i[0],[[],''])
            O[i[1]][i[0]][0].append(i[3])
            O[i[1]][i[0]][1] = i[2]
            
            SepratedOutputFile =  FormatDoc('TYPE: ' + i[1],'','','') + FormatDoc('','Object: ' +  ModuleName + '.' + i[0],'','') + FormatDoc('','',r'Method(s) / Attribute(s):',str(i[3])) + FormatDoc('','','Documentation on ' + ModuleName + '.' + i[0] + ':',i[2])
            OutputFile += SepratedOutputFile

            ObjectTag = ET.SubElement(TypeTag, 'Object')
            ObjectTag.set('Name',ModuleName + '.' + i[0])

            ObjectMethAttr = ET.SubElement(ObjectTag,'Methods_Attributes')
            ObjectMethAttr.text = '\n' + str(i[3])

            ObjectDoc = ET.SubElement(ObjectTag,'Doc')
            ObjectDoc.text = i[2]

            with open(StoragePath + '\\#eDocuPy (' + ModuleName + ')\\' + i[1].replace('<','(').replace('>',')') + ' ~ ' + ModuleName + '.' + i[0] + '.txt',mode='w', encoding="utf-8") as TXTFN:
                TXTFN.write(SepratedOutputFile)

            cur.execute('INSERT INTO ' + 'eDocuPy' + ' (Type,Object,"Method(s) / Attribute(s)",Documetation) VALUES (?,?,?,?)', (i[1],ModuleName + '.' + i[0],str(i[3]),i[2]))

    db.commit()
    db.close()

    OutputFile += '\n' + ('*' * 70) + '\n'

    XMLSTR = ET.tostring(ModuleTag)

    shutil.make_archive(StoragePath + '#eDocuPy (' + ModuleName + ')', 'zip', StoragePath + '\\#eDocuPy (' + ModuleName + ')\\')
    shutil.rmtree(StoragePath + '\\#eDocuPy (' + ModuleName + ')\\')
    
    with open(StoragePath + '#eDocuPy (' + ModuleName + ').txt',mode='w', encoding="utf-8") as TXTFN:
        TXTFN.write(OutputFile)

    tree = ET.ElementTree(ModuleTag)
    tree.write(StoragePath + '#eDocuPy (' + ModuleName + ').xml')

    JS = json.dumps (O,indent= 5)
    with open(StoragePath + '#eDocuPy (' + ModuleName + ').json',mode='w') as JSNFN:
        json.dump(O,JSNFN)

    print(' '*5 + 'Documentation of (',ModuleName,') is Completed.\n')
    SubModuleCounter += 1

    if SubModuleDocumentation:
        for k,v in SubModules.items():
            if (v == 0):
                eDocuPy(k)
            else:
                continue

    os.system(f'start {os.path.realpath(os.getcwd())}')

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
<<<<<<< HEAD
        
        SubModulesExtraction = input("\nEnter (True / False) for any subModules to be documented if applicable\n\n" + " " * 3 + "Or\n\n" + "Enter (P) to back to the previous menu\n\n" + " " * 3 + "Or\n\n" + "Enter (X) to stop:\n\n")
||||||| ee519fd (Some Bugs Fixed)
        SubModulesExtractionStr = 'False'
=======
<<<<<<< HEAD
        SubModulesExtractionStr = 'False'
||||||| d90b2e4
        
        SubModulesExtraction = input("\nEnter (True / False) for any subModules to be documented if applicable\n\n" + " " * 3 + "Or\n\n" + "Enter (P) to back to the previous menu\n\n" + " " * 3 + "Or\n\n" + "Enter (X) to stop:\n\n")
=======
        
        if PKGs.get(ModuleForDocumentation.split('.')[0],None):
            SubModulesExtractionStr = input("\nEnter (T)rue / (F)alse for any subModules to be documented if applicable\n\n" + " " * 3 + \
                                        "Or\n\n" + \
                                        "Enter (P) / (Previous) to back to the main menu\n\n" + " " * 3 + \
                                        "Or\n\n" + \
                                        "Enter (X) / (eXit) to stop:\n\n").strip()
>>>>>>> a078e210a69c83d1b585111c2421cfc337b2fda7
>>>>>>> parent of ee519fd (Some Bugs Fixed)

<<<<<<< HEAD
        if SubModulesExtraction.lower() in ['true','false']:
||||||| ee519fd (Some Bugs Fixed)
        if PKGs.get(ModuleForDocumentation.split('.')[0],(None,))[0]:
            SubModulesExtractionStr = input("\nEnter (T)rue / (F)alse for any subModules to be documented if applicable\n\n" + " " * 3 + \
                                        "Or\n\n" + \
                                        "Enter (P) / (Previous) to back to the main menu\n\n" + " " * 3 + \
                                        "Or\n\n" + \
                                        "Enter (X) / (eXit) to stop:\n\n").strip()

        if SubModulesExtractionStr.lower() in ['true','false','t','f']:
=======
<<<<<<< HEAD
        if PKGs.get(ModuleForDocumentation.split('.')[0],(None,))[0]:
            SubModulesExtractionStr = input("\nEnter (T)rue / (F)alse for any subModules to be documented if applicable\n\n" + " " * 3 + \
                                        "Or\n\n" + \
                                        "Enter (P) / (Previous) to back to the main menu\n\n" + " " * 3 + \
                                        "Or\n\n" + \
                                        "Enter (X) / (eXit) to stop:\n\n").strip()

        if SubModulesExtractionStr.lower() in ['true','false','t','f']:
||||||| d90b2e4
        if SubModulesExtraction.lower() in ['true','false']:
=======
        if SubModulesExtractionStr.lower() in ['true','false','t','f']:
>>>>>>> a078e210a69c83d1b585111c2421cfc337b2fda7
>>>>>>> parent of ee519fd (Some Bugs Fixed)
            SubModuleExtractionNotOK = False
            SubModulesExtraction = (SubModulesExtraction.capitalize() == 'True')
            os.system("cls")
            print('\nProcess started. Please wait ...\n')
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