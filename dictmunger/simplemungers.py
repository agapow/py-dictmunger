"""
Some simple sublcasses of DictMunger, partly for use and partly as an example.

By convention, mungers are named after what they do, in the singular.
"""
#TODO: restrict symbol export

### IMPORTS

from dictmunger import BaseDictMunger

from string import lower


### CONSTANTS & DEFINES

### CODE ###

class LowercaseKeyMunger (BaseDictMunger):
	"""
	Change all keys in a dictionary into lowercase.

	Old / original rows are deleted.
	"""
	def default_transform (self, d, k):
		self.move_key (d, k, lower(k))


class TransformValMunger (BaseDictMunger):
	"""
	Transform all values in a dictionary with the same function.
	"""
	
	def __init__ (self, trans_fn):
		self.trans_fn = trans_fn

	def default_transform (self, d, k):
		self.transform_value (d, k, self.trans_fn)


class DeleteEmptyValMunger (BaseDictMunger):
	"""
	Delete any rows in the dictionary with an 'empty' value.

	Empty values are defined as None and zero-content strings, lists and dicts.
	This may be adjusted with the constructor.
	"""
	
	empty_vals = [
		'',
		[],
		{},
		None,
	]

	def __init__ (self, empty_vals=None):
		if empty_vals is not None:
			self.empty_vals = empty_vals

	def default_transform (self, d, k):
		if d[k] in self.empty_vals:
			del d[k]


class KeepKeyMunger  (BaseDictMunger):
	"""
	Keep only rows in the dict with the given keys, delete all others.
	
	Note that due to the way this works in the base class, if an empty list
	is passed, all keys are kept.
	"""
	def __init__ (self, keep_keys):
		self.keep_keys = keep_keys


class DelKeyMunger  (BaseDictMunger):
	"""
	Delete rows in the dict with the given keys, keep all others.
	"""
	def __init__ (self, delete_keys):
		self.delete_keys = delete_keys


### END ###

