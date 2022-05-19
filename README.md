# eDocuPy
To extract internal documentation of any official Python Package/Module from its heart.

Main idea behind the script is extracting internal documentations of any official Python Package/Module and help users to learn that Package/Module functionality more easily. eDocuPy explores any Python module, extract each and every objects inside it (includig Classes, Functions, Attribues) along with internal Help/Documentation contents corresponding to each of them, sort the outputs in a very special order and provide users with 5 different formats. Internal documentations of any official Python Package/Module are re-arranged in a way that from the point of the author's view would be more efficient for self-studying. eDocuPy's output is considered to be helpful because of the following reasons:
	
	* provides an all-in-one help eDocument
	* speed-up investigations and exploring Help contents
	* contents are sorted by the module's internal object types (Classes, Functions, DATA)
	* all attributes/methods/DATA are extracted as well. alongside,
	* internal Help() for all commands are extracted in a blink.
	* original Help() document is extracted by eDocuPy to provide users with 

To clarify more, eDocuPy combines Dir() & Help() outputs of each and every one of the objects inside an installed Python module that users might gain from the >>> 'Chevron prompt' of the interactive Python interpreter as a piece of cake. It should be mentioned that all Dunder (Double UNDERscore) methods/attributes are ignored deliberately to make the outputs more eye-caching.

Finally, *.JSON, *.XML, *.TXT, *.SQLITE and *.zip formats are the ones that eDocuPy can help you with. Apply them as you wish Pythonistas !!!

# Instruction:
	1. Download the script.
	2. Run it as follows:
		in Win OS  =>	Python eDocuPy.py
		in Mac OS  =>	Python3 eDocuPy.py

# Some Sample Screen Captures:
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/VL5ZqQkf/e-Docu-Py-importlib-I.png" alt="e-Docu-Py-importlib-I"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/KYh9h1rj/e-Docu-Py-importlib-II.png" alt="e-Docu-Py-importlib-II"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/vZVPKrnC/e-Docu-Py-numpy-I.png" alt="e-Docu-Py-numpy-I"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/4NMLwLYz/e-Docu-Py-numpy-II.png" alt="e-Docu-Py-numpy-II"/></a><br/><br/>
<a href="https://postimg.cc/zHnK3JhM" target="_blank"><img src="https://i.postimg.cc/d3fBH3Vq/e-Docu-Py-numpy-III.png" alt="e-Docu-Py-numpy-III"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/hjpMmpFQ/e-Docu-Py-numpy-IV.png" alt="e-Docu-Py-numpy-IV"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/DZ2BmRNK/e-Docu-Py-numpy-V.png" alt="e-Docu-Py-numpy-V"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/YSNdrtb3/e-Docu-Py-numpy-VI.png" alt="e-Docu-Py-numpy-VI"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/4yyPQVZL/e-Docu-Py-numpy-VII.png" alt="e-Docu-Py-numpy-VII"/></a><br/><br/>


## Here is an example of eDocuPy's output style run over the 'importlib' builtin module in *.TXT format:

	TYPE: <class 'function'>
	------------------------
			

		Object: importlib.__import__
		----------------------------
			

		Documentation on importlib.__import__:
		--------------------------------------
			function __import__ in module importlib._bootstrap
			
			__import__(name, globals=None, locals=None, fromlist=(), level=0)
				Import a module.
				
				The 'globals' argument is used to infer where the import is occurring from
				to handle relative imports. The 'locals' argument is ignored. The
				'fromlist' argument specifies what should exist as attributes on the module
				being imported (e.g. ``from module import <fromlist>``).  The 'level'
				argument represents the package location to import from in a relative
				import (e.g. ``from ..pkg import mod`` would have a 'level' of 2).
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: importlib._pack_uint32
		------------------------------
			

		Documentation on importlib._pack_uint32:
		----------------------------------------
			function _pack_uint32 in module importlib._bootstrap_external
			
			_pack_uint32(x)
				Convert a 32-bit integer to little-endian.
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: importlib._unpack_uint32
		--------------------------------
			

		Documentation on importlib._unpack_uint32:
		------------------------------------------
			function _unpack_uint32 in module importlib._bootstrap_external
			
			_unpack_uint32(data)
				Convert 4 bytes in little-endian to an integer.
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: importlib.find_loader
		-----------------------------
			

		Documentation on importlib.find_loader:
		---------------------------------------
			function find_loader in module importlib
			
			find_loader(name, path=None)
				Return the loader for the specified module.
				
				This is a backward-compatible wrapper around find_spec().
				
				This function is deprecated in favor of importlib.util.find_spec().
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: importlib.import_module
		-------------------------------
			

		Documentation on importlib.import_module:
		-----------------------------------------
			function import_module in module importlib
			
			import_module(name, package=None)
				Import a module.
				
				The 'package' argument is required when performing a relative import. It
				specifies the package to use as the anchor point from which to resolve the
				relative import to an absolute import.
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: importlib.invalidate_caches
		-----------------------------------
			

		Documentation on importlib.invalidate_caches:
		---------------------------------------------
			function invalidate_caches in module importlib
			
			invalidate_caches()
				Call the invalidate_caches() method on all meta path finders stored in
				sys.meta_path (where implemented).
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: importlib.reload
		------------------------
			

		Documentation on importlib.reload:
		----------------------------------
			function reload in module importlib
			
			reload(module)
				Reload the module and return it.
				
				The module must have been successfully imported before.
			
			
	TYPE: <class 'str'>
	-------------------
			

		Object: importlib.__cached__
		----------------------------
			

		Method, Attribute / Data:
		-------------------------
			'C:\\Program Files\\Python38\\lib\\importlib\\__pycache__\\__init__.cpython-38.pyc'
			

		Documentation on importlib.__cached__:
		--------------------------------------
			DATA
			
	TYPE: <class 'str'>
	-------------------
			

		Object: importlib.__file__
		--------------------------
			

		Method, Attribute / Data:
		-------------------------
			'C:\\Program Files\\Python38\\lib\\importlib\\__init__.py'
			

		Documentation on importlib.__file__:
		------------------------------------
			DATA
			
	TYPE: <class 'str'>
	-------------------
			

		Object: importlib.__doc__
		-------------------------
			

		Method, Attribute / Data:
		-------------------------
			'A pure Python implementation of import.'
			

		Documentation on importlib.__doc__:
		-----------------------------------
			DATA
			
	TYPE: <class 'str'>
	-------------------
			

		Object: importlib.__name__
		--------------------------
			

		Method, Attribute / Data:
		-------------------------
			'importlib'
			

		Documentation on importlib.__name__:
		------------------------------------
			DATA
			
	TYPE: <class 'str'>
	-------------------
			

		Object: importlib.__package__
		-----------------------------
			

		Method, Attribute / Data:
		-------------------------
			'importlib'
			

		Documentation on importlib.__package__:
		---------------------------------------
			DATA
			
	TYPE: <class 'list'>
	--------------------
			

		Object: importlib.__all__
		-------------------------
			

		Method, Attribute / Data:
		-------------------------
			['__import__', 'import_module', 'invalidate_caches', 'reload']
			

		Documentation on importlib.__all__:
		-----------------------------------
			DATA
			
	TYPE: <class 'list'>
	--------------------
			

		Object: importlib.__path__
		--------------------------
			

		Method, Attribute / Data:
		-------------------------
			['C:\\Program Files\\Python38\\lib\\importlib']
			

		Documentation on importlib.__path__:
		------------------------------------
			DATA
			
	TYPE: <class 'dict'>
	--------------------
			

		Object: importlib.__builtins__
		------------------------------
			

		Method, Attribute / Data:
		-------------------------
			{'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'WindowsError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-Z plus Return to exit, 'exit': Use exit() or Ctrl-Z plus Return to exit, 'copyright': Copyright (c) 2001-2019 Python Software Foundation.
			All Rights Reserved.
			
			Copyright (c) 2000 BeOpen.com.
			All Rights Reserved.
			
			Copyright (c) 1995-2001 Corporation for National Research Initiatives.
			All Rights Reserved.
			
			Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
			All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
				for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object.}
			

		Documentation on importlib.__builtins__:
		----------------------------------------
			DATA
			
	TYPE: <class 'dict'>
	--------------------
			

		Object: importlib._RELOADING
		----------------------------
			

		Method, Attribute / Data:
		-------------------------
			{}
			

		Documentation on importlib._RELOADING:
		--------------------------------------
			DATA
			
	TYPE: <class '_frozen_importlib_external.SourceFileLoader'>
	-----------------------------------------------------------
			

		Object: importlib.__loader__
		----------------------------
			

		Method, Attribute / Data:
		-------------------------
			<_frozen_importlib_external.SourceFileLoader object at 0x0000000002634C40>
			

		Documentation on importlib.__loader__:
		--------------------------------------
			DATA
			
	TYPE: <class '_frozen_importlib.ModuleSpec'>
	--------------------------------------------
			

		Object: importlib.__spec__
		--------------------------
			

		Method, Attribute / Data:
		-------------------------
			ModuleSpec(name='importlib', loader=<_frozen_importlib_external.SourceFileLoader object at 0x0000000002634C40>, origin='C:\\Program Files\\Python38\\lib\\importlib\\__init__.py', submodule_search_locations=['C:\\Program Files\\Python38\\lib\\importlib'])
			

		Documentation on importlib.__spec__:
		------------------------------------
			DATA
			

	**********************************************************************


# Discover the power of eDocuPy yourself !!!
