# eDocuPy
To extract internal documentation of any official Python module from its heart.

The main idea behind the script is extracting internal documentations of any official Python module and help users to learn that module functionality more easily. eDocuPy explores Python module, extract each and every objects inside the module (includig Classes, Functions, Attribues or even internal Sub-Modules) along with internal Help/Documentation contents corresponding to each of them and sort the output contents in a very special order. eDocumentaion is re-arranged in a way that from the point of the author's view would be more efficient for self-studying. eDocuPy's output is considered to be helpful because of the following reasons:
	
	*provides an all-in-one help eDocument
	*contents are sorted by the module's internal object types (Classes, Functions, Attribues, Sub-Modules)
	*all attributes/methods are extracted as well. alongside,
	*internal Help() for all commands are extracted in a blink.

To clarify more, eDocuPy combines Dir() & Help() outputs of each and every one of the objects inside an installed Python module that users might gain from the Chevron prompt of the interactive Python interpreter as a piece of cake. It should be mentioned that all Dunder (Double UNDERscore) methods are ignored deliberately to make the outputs more eye-caching.

Finally, eDocuPy generates the beforementioned e-documentations in five different formats from now on (*.JSON, *.XML, *.TXT, *.SQLITE and *.zip format).

# Instruction:
	1. Download the script.
	2. Run it as follows:
		in Windows =>	Python eDocuPy.py
		in Mac OS  =>	Python3 eDocuPy.py

## Here is an example of eDocuPy's output shape run over the 'string' builtin module in *.TXT format:

	TYPE: <class 'type'>
	--------------------
			

		Object: string.Formatter
		------------------------
			

		Method(s) / Attribute(s):
		-------------------------
			['check_unused_args', 'convert_field', 'format', 'format_field', 'get_field', 'get_value', 'parse', 'vformat']
			

		Documentation on string.Formatter:
		----------------------------------
			class Formatter in module string
			
			class Formatter(builtins.object)
			 |  Methods defined here:
			 |  
			 |  check_unused_args(self, used_args, args, kwargs)
			 |  
			 |  convert_field(self, value, conversion)
			 |  
			 |  format(self, format_string, /, *args, **kwargs)
			 |  
			 |  format_field(self, value, format_spec)
			 |  
			 |  get_field(self, field_name, args, kwargs)
			 |      # given a field_name, find the object it references.
			 |      #  field_name:   the field being looked up, e.g. "0.name"
			 |      #                 or "lookup[3]"
			 |      #  used_args:    a set of which args have been used
			 |      #  args, kwargs: as passed in to vformat
			 |  
			 |  get_value(self, key, args, kwargs)
			 |  
			 |  parse(self, format_string)
			 |      # returns an iterable that contains tuples of the form:
			 |      # (literal_text, field_name, format_spec, conversion)
			 |      # literal_text can be zero length
			 |      # field_name can be None, in which case there's no
			 |      #  object to format and output
			 |      # if field_name is not None, it is looked up, formatted
			 |      #  with format_spec and conversion and then used
			 |  
			 |  vformat(self, format_string, args, kwargs)
			 |  
			 |  ----------------------------------------------------------------------
			 |  Data descriptors defined here:
			 |  
			 |  __dict__
			 |      dictionary for instance variables (if defined)
			 |  
			 |  __weakref__
			 |      list of weak references to the object (if defined)
			
			
	TYPE: <class 'function'>
	------------------------
			

		Object: string.capwords
		-----------------------
			

		Documentation on string.capwords:
		---------------------------------
			function capwords in module string
			
			capwords(s, sep=None)
			    capwords(s [,sep]) -> string
			    
			    Split the argument into words using split, capitalize each
			    word using capitalize, and join the capitalized words using
			    join.  If the optional second argument sep is absent or None,
			    runs of whitespace characters are replaced by a single space
			    and leading and trailing whitespace are removed, otherwise
			    sep is used to split and join the words.
			
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.ascii_letters
		----------------------------
			

		Documentation on string.ascii_letters:
		--------------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.ascii_lowercase
		------------------------------
			

		Documentation on string.ascii_lowercase:
		----------------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.ascii_uppercase
		------------------------------
			

		Documentation on string.ascii_uppercase:
		----------------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.digits
		---------------------
			

		Documentation on string.digits:
		-------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.hexdigits
		------------------------
			

		Documentation on string.hexdigits:
		----------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.octdigits
		------------------------
			

		Documentation on string.octdigits:
		----------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.printable
		------------------------
			

		Documentation on string.printable:
		----------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.punctuation
		--------------------------
			

		Documentation on string.punctuation:
		------------------------------------
			No Documentation !!!
			
	TYPE: <class 'str'>
	-------------------
			

		Object: string.whitespace
		-------------------------
			

		Documentation on string.whitespace:
		-----------------------------------
			No Documentation !!!
			
	TYPE: <class 'string._TemplateMetaclass'>
	-----------------------------------------
			

		Object: string.Template
		-----------------------
			

		Method(s) / Attribute(s):
		-------------------------
			['braceidpattern', 'delimiter', 'flags', 'idpattern', 'pattern', 'safe_substitute', 'substitute']
			

		Documentation on string.Template:
		---------------------------------
			class Template in module string
			
			class Template(builtins.object)
			 |  Template(template)
			 |  
			 |  A string class for supporting $-substitutions.
			 |  
			 |  Methods defined here:
			 |  
			 |  __init__(self, template)
			 |      Initialize self.  See help(type(self)) for accurate signature.
			 |  
			 |  safe_substitute(self, mapping={}, /, **kws)
			 |  
			 |  substitute(self, mapping={}, /, **kws)
			 |  
			 |  ----------------------------------------------------------------------
			 |  Data descriptors defined here:
			 |  
			 |  __dict__
			 |      dictionary for instance variables (if defined)
			 |  
			 |  __weakref__
			 |      list of weak references to the object (if defined)
			 |  
			 |  ----------------------------------------------------------------------
			 |  Data and other attributes defined here:
			 |  
			 |  braceidpattern = None
			 |  
			 |  delimiter = '$'
			 |  
			 |  flags = re.IGNORECASE
			 |  
			 |  idpattern = '(?a:[_a-z][_a-z0-9]*)'
			 |  
			 |  pattern = re.compile('\n    \\$(?:\n      (?P<escaped>\\$)...ced>(?a:[...
			
			

	**********************************************************************


# Discover the power of eDocuPy yourself !!!