# eDocuPy
To extract internal documentation of any official Python module from its heart.

The main idea behind the script is extracting documentations inside any official Python module and help the users to learn it more easily. eDocuPy explores Python modules, extract each and every objects inside the modules (includig Classes, Functions, Attribues or even internal Modules) along with their internal Help/Documentation contents and list them all in a very special order. The output is re-arranged in a way that from the point of the author's view is more efficient. eDocuPy's output is considered to be helpful because it is an all-in-one help document and the contents are sorted by the module's classes, functions & methods. All attributes/methods are extracted as well. Alongside, internal Help for all commands are extracted and represented in a pack.
To clarify more, eDocuPy combines Dir() & Help() outputs of each and every one of the objects inside an installed Python module that a user might gain from the Chevron prompt of the interactive Python interpreter. It should be mentioned that all Dunder (Double UNDERscore) methods are ignored deliberately to make the outputs more eye-caching.
Finally, eDocuPy generates the beforementioned e-documentations in four different formats (*.JSON, *.XML, *.TXT and *.SQLITE).

# Instruction:
	1. Download the script.
	2. Run it as follows:
		in Windows =>	Python eDocuPy.py
		in Mac OS  =>	Python3 eDocuPy.py

## Here is an example of eDocuPy's output run over the 'xml' builtin module in *.TXT format:

		TYPE: <class 'module'>
		----------------------
				

			Object: xml.etree
			-----------------
				

			Method(s) / Attribute(s):
			-------------------------
				['ElementPath', 'ElementTree']
				

			Documentation on xml.etree:
			---------------------------
				package xml.etree in xml
				
				NAME
				    xml.etree
				
				DESCRIPTION
				    # $Id: __init__.py 3375 2008-02-13 08:05:08Z fredrik $
				    # elementtree package
				
				PACKAGE CONTENTS
				    ElementInclude
				    ElementPath
				    ElementTree
				    cElementTree
				
				FILE
				    c:\program files\python38\lib\xml\etree\__init__.py
				
				
				

		**********************************************************************

# Discover the power of eDocuPy yourself !!!