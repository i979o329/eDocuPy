import sqlite3
import json
import xml.etree.ElementTree as ET
import pydoc
import os
import warnings
import shutil
import inspect
import pkgutil
import tempfile
import datetime
#import sys

#sys.setrecursionlimit(10000)
warnings.filterwarnings("ignore")

SubModules = {}
SubModuleCounter = 0
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

def eDocuPy(ModuleForDocumentation = 'builtins' , SubModuleDocumentation = True):
    
    global StoragePath,StorageSubFolders,SubModules,SubModuleCounter,ModuleVersion,LogFile,LogFilePath,PackageHandler,PKGs

    StoragePath = os.getcwd() + '\\' + (ModuleForDocumentation.split('.')[0] if ModuleForDocumentation !='' else 'builtins')
    if PackageHandler == '' : LogFilePath = StoragePath + '\\#ReadME ' + datetime.datetime.now().isoformat(sep=',', timespec='auto').replace(':','-') + '.LOG'
    LogFile += "Module ( " + (ModuleForDocumentation if ModuleForDocumentation !='' else 'builtins') + " ) Documentation Status: \n"

    StorageSubFolders = ''

    try:
        if SubModules == {} :        
            if ModuleForDocumentation in ['','builtins','__builtins__']:
                inp = __import__('builtins')
                os.makedirs(StoragePath,exist_ok=True)
            elif ModuleForDocumentation.split('.')[0] in PKGs:
                PackageHandler = __import__(ModuleForDocumentation, fromlist=[''])    
                os.makedirs(StoragePath,exist_ok=True)
                inp = PackageHandler
        else:
            if hasattr(PackageHandler,ModuleForDocumentation.split('.')[-1]):
                inp = getattr(PackageHandler,ModuleForDocumentation.split('.')[-1])
            else:
                PackageHandler = __import__('.'.join(ModuleForDocumentation.split('.')[:-1]), fromlist=[''])
                inp = __import__(ModuleForDocumentation, fromlist=[''])  

    except BaseException as Err:
        print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of ( ',ModuleForDocumentation,' ) is in progress ...\n')
        print("\n\t",Err,'!!!') #,"\n\n"," " * 15, "And / Or\n\n\t", "Module has not been installed yet !!!\n\n")
        
        LogFile += "*** Error Ocurred During the Documentation of ( " + ModuleForDocumentation + " ) : " + str(Err) + '!!!\n'
        with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
            LOGFILE.write(LogFile)

        SubModuleCounter += 1
        SubModules[ModuleForDocumentation] = 1
        return 'ErrorOccured'

    DefaultClasses = ("<class 'int'>", "<class 'float'>", "<class 'complex'>",
                      "<class 'str'>", "<class 'bool'>", "<class 'list'>",
                      "<class 'set'>", "<class 'tuple'>", "<class 'dict'>",
                      "<class 'frozenset'>", "<class 'bytes'>", "<class 'NoneType'>",
                      )

    ModuleName = ''
    ModuleFilePath = []

    if ModuleForDocumentation in ['','builtins','__builtins__']:

        ModuleName = getattr(inp,'__name__') #'builtins'
        ModuleVersion = '' # ModuleName + '-' + sys.version.split(' ')[0]
        print('\n',('(' + str(SubModuleCounter) + '/' + str(len(SubModules)-1) + ') ') * bool(SubModules) + 'Documentation of (',ModuleName,') is in progress ...\n')

    elif ModuleForDocumentation.split('.')[0] in PKGs: #.get(ModuleForDocumentation),None):
        try:

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

        except BaseException as Err:

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
    _Type = list(map(lambda _ : str(type(getattr(inp,_))) , _Dir))

    SortKey = ["<class 'type'>", "<class 'function'>", "<class 'builtin_function_or_method'>"]
    ModuleExclusiveTypes = [_ for _ in _Type if (not _ in SortKey+["<class 'module'>"])]
    ModuleExclusiveTypes = sorted([(ModuleExclusiveTypes.count(_),_) for _ in set(ModuleExclusiveTypes)],reverse=True)
    ModuleExclusiveTypes = [_[1] for _ in ModuleExclusiveTypes]
    SortKey += ModuleExclusiveTypes
    #SortKey += ["<class 'module'>"]
    SortKey = dict((value,len(SortKey)-key) for (key,value) in dict(enumerate(SortKey)).items() )

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
    O = {}
    OutputFile = '' ; SepratedOutputFile = ''
    ModuleTag = ET.Element('Module')
    ModuleTag.set('Name', ModuleName)

    db = sqlite3.connect(StoragePath + StorageSubFolders + '#eDocuPy (' + ModuleName + ').sqlite')  # (":memory:")
    cur = db.cursor()

    cur.execute('DROP TABLE IF EXISTS ' + 'eDocuPy')
    cur.execute('CREATE TABLE IF NOT EXISTS ' + 'eDocuPy' + ' (Type TEXT,Object TEXT,"Method, Attribute / Data" TEXT,Documetation TEXT)')

    for i in sorted(zip(_Dir,_Type,_Doc,_SubDir),key=(lambda _ : (SortKey.get(_[1]),len(_[3]))),reverse=True):

        O.setdefault(i[1],{})
        TypeTag = ET.SubElement(ModuleTag, 'Class')
        TypeTag.set('Type',i[1])

        if i[3] == []:

            O[i[1]].setdefault(i[0],i[2])

            SepratedOutputFile =  FormatDoc('TYPE: ' + i[1],'','','') + FormatDoc('','Object: ' +  (ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0],'','') + FormatDoc('','','Documentation on ' + (ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0] + ':',i[2])
            OutputFile +=  SepratedOutputFile

            ObjectTag = ET.SubElement(TypeTag, 'Object')
            ObjectTag.set('Name',(ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0])

            ObjectDoc = ET.SubElement(ObjectTag,'Doc')
            ObjectDoc.text = i[2]
            
            with open(TempFolder + i[1].replace('<','(').replace('>',')') + ' ~.' + i[0] + '.txt',mode='w', encoding="utf-8") as SepTXTFN:
                SepTXTFN.write(SepratedOutputFile)

            cur.execute('INSERT INTO ' + 'eDocuPy' + ' (Type,Object,"Method, Attribute / Data",Documetation) VALUES (?,?,?,?)', (i[1],(ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0],'',i[2]))

        else:

            O[i[1]].setdefault(i[0],[[],''])
            O[i[1]][i[0]][0].append(i[3])
            O[i[1]][i[0]][1] = i[2]
            
            SepratedOutputFile =  FormatDoc('TYPE: ' + i[1],'','','') + FormatDoc('','Object: ' +  (ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0],'','') + FormatDoc('','',r'Method, Attribute / Data:',str(i[3])) + FormatDoc('','','Documentation on ' + (ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0] + ':',i[2])
            OutputFile += SepratedOutputFile

            ObjectTag = ET.SubElement(TypeTag, 'Object')
            ObjectTag.set('Name',(ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0])

            ObjectMethAttr = ET.SubElement(ObjectTag,'Method-Attribute_Data')
            ObjectMethAttr.text = '\n' + str(i[3])

            ObjectDoc = ET.SubElement(ObjectTag,'Doc')
            ObjectDoc.text = i[2]

            with open(TempFolder + i[1].replace('<','(').replace('>',')') + ' ~.' + i[0] + '.txt',mode='w', encoding="utf-8") as SepTXTFN:
                SepTXTFN.write(SepratedOutputFile)

            cur.execute('INSERT INTO ' + 'eDocuPy' + ' (Type,Object,"Method, Attribute / Data",Documetation) VALUES (?,?,?,?)', (i[1],(ModuleName + '.') * bool(ModuleName + '.' != 'builtins.') + i[0],str(i[3]),i[2]))

    db.commit()
    db.close()

    OutputFile += '\n' + ('*' * 70) + '\n'

    XMLSTR = ET.tostring(ModuleTag)

    shutil.make_archive(StoragePath + StorageSubFolders + '#eDocuPy (' + ModuleName + ')\\', 'zip', TempFolder)
    shutil.rmtree(TempFolder,ignore_errors = True)
    
    with open(StoragePath + StorageSubFolders + '#Original (' + ModuleName + ').txt',mode='w', encoding="utf-8") as OrgDoc:
        try:
            OrgDoc.write(pydoc.render_doc(ModuleForDocumentation, "%s",renderer=pydoc.plaintext))
        except BaseException:
            OrgDoc.write('No Original Module Documentation !!!')

    with open(StoragePath + StorageSubFolders + '#eDocuPy (' + ModuleName + ').txt',mode='w', encoding="utf-8") as TXTFN:
        TXTFN.write(OutputFile)

    tree = ET.ElementTree(ModuleTag)
    tree.write(StoragePath + StorageSubFolders + '#eDocuPy (' + ModuleName + ').xml')

    JS = json.dumps (O,indent= 5)
    with open(StoragePath + StorageSubFolders + '#eDocuPy (' + ModuleName + ').json',mode='w') as JSNFN:
        json.dump(O,JSNFN)

    print(' '*5 + 'Documentation of (',ModuleName,') is Completed.\n')
    LogFile += '>>> Documentation of ( ' + ModuleName + ' ) Module is Completed.\n'
    SubModuleCounter += 1
    SubModules[ModuleForDocumentation] = 1

    with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
        LOGFILE.write(LogFile)
    
    del inp
        
    return 'DocumentationSucceeded'

def SubModulesExtrFunc(SubModulesInp):
    global StoragePath,StorageSubFolders,SubModules,LogFile,LogFilePath,OutputFolder
    #sys.setrecursionlimit(1000+len(SubModules))

    for k,v in SubModulesInp.items():
        if (v == 0):
            with open(LogFilePath,mode='w', encoding="utf-8") as LOGFILE:
                LOGFILE.write(LogFile)
            eDocuPy(k,False)
        else:
            continue

def FL(INPUT):
    if isinstance(INPUT, list):
        return [_ for _ in INPUT if _.count('__') < 2]
    elif isinstance(INPUT, dict):
        return {k:v for k,v in INPUT.items() if k.count('__') < 2}

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

    ModuleForDocumentation = input("\nEnter an {Existing Module Name} to start documentaion process\n\n" + " " * 3 + \
                                    "Or\n\n" + \
                                    "Enter (B) / (Builtins) to document Builtins module\n\n" + " " * 3 + \
                                    "Or\n\n" + \
                                    "Enter (X) / (eXit) to terminate:\n\n").strip()

    SubModuleExtractionNotOK = True
    PackageHandler = ''
    LogFile = ''
    
    if ModuleForDocumentation.lower() in ['x','exit']:
        ModuleNameNotOK = False
        os.system("cls")
        print('\nSee U Soon. Thank you ...\n\n')
        quit()
    elif ModuleForDocumentation.lower() in ['b','builtins']:
        ModuleNameNotOK = True
        ModuleForDocumentation = ''
        SubModulesExtractionStr = 'False'
    elif ModuleForDocumentation.split('.')[0] in PKGs:
        if not(PKGs.get(ModuleForDocumentation.split('.')[0],True)):
            ModuleNameNotOK = True
            SubModulesExtractionStr = 'False'
        else:
            ModuleNameNotOK = True
    else:
        ModuleNameNotOK = True
        SubModuleExtractionNotOK = False
    
    while SubModuleExtractionNotOK:

        os.system("cls")
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
            SubModuleExtractionNotOK = False
            SubModulesExtraction = (SubModulesExtractionStr.capitalize() in ['True','T'])
            os.system("cls")
            print('\nProcess started. Please wait ...\n')
            eDocuPy(ModuleForDocumentation,SubModulesExtraction)
            SubModulesExtrFunc(SubModules)

            if sum(SubModules.values()) == len(SubModules) : 
                OutputFolder = '\\'.join((StoragePath + StorageSubFolders).split('\\')[:1+len(os.getcwd().split('\\'))]) + '\\'
                os.system(f'start {OutputFolder}')

            SubModules = {}
            SubModuleCounter = 0
            ModuleVersion = ''
        elif SubModulesExtractionStr.lower() in ['x','exit']:
            SubModuleExtractionNotOK = False
            os.system("cls")
            print('\nSee U Soon. Thank you ...\n\n')
            quit()   
        elif SubModulesExtractionStr.lower() in ['p','previous']:
            ModuleNameNotOK = True
            SubModuleExtractionNotOK = False
