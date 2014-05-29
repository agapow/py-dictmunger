"""
Transform, delete or filter the fields of a dictionary
"""

# TODO: restrict symbol export

### IMPORTS

from copy import copy
from string import lower


### CONSTANST & DEFINES

### CODE ###

class BaseDictMunger (object):
	"""
	A base class for defining dictionary transformers.

	Note that this transforms the dict inplace - the original data is lost.
	"""
	# TODO: allow for transform_value, delete/keep value

	transform_keys = []
	create_keys = []
	keep_keys = []
	delete_keys = []

	### Lifecycle

	def __init__ (self):
		pass


	### Services

	def munge (self, d):
		# so we don't mutate original data
		d = copy (d)

		# from lists, do transformation, creation and keep/delete
		self.call_transform_keys (d)
		self.call_create_keys (d)
		self.call_keep_or_delete_keys (d)

		return d
		
	def call_transform_keys (self, d):
		# get order from transform keys, otherwise assume all
		transform_keys = self.transform_keys or d.keys()
		for k in transform_keys:
			mthd = getattr (self, 'transform_%s' % self.key_to_name(k), None)
			if mthd:
				mthd (self, d, k) 
			else:
				self.default_transform (d, k)
				
	def call_creation_keys (self, d):
		for k in self.create_keys:
			d[k] = __getattr__ (self, 'create_%s' % self.key_to_name(k))(d)

	def call_keep_or_delete_keys (self, d):
		# The logic we use here is that there are 3 possible situations:
		#
		# - delete some of the fields
		# - keep some of the fields
		# - keep all of the fields
		#
		# We'd never want to delete all the rows, so there's no need to handle
		# that case. If anything is defined for 'delete_keys', we assume that
		# other than those, everything is kept. This is handled by the first
		# "if" below.
		# If anything is defined for 'keep_keys', everything else is deleted.
		# Finally, if nothing is defined for keep_keys, everything is kept
		# (execution falls through the two 'ifs' below).
		if self.delete_keys:
			for r in self.delete_keys:
				if d.has_key (r):
					del d[r]
		elif self.keep_keys:
			for k in d.keys():
				if k not in self.keep_keys:
					del d[k]
					
	def default_transform (self, d, k):
		"""
		Transforms a row value if no specific one is provided.
		
		Note this is called `default_transform` instead of `transform_default`
		so rows can use the key `default`.
		"""
		pass

	def move_key (self, d, old_key, new_key):
		"""
		Change a row by shifting it to a new key.

		A utility method to be called by subclasses. The value at the old key
		is deleted. Note that if the old and new keys are the same, nothing
		happens.
		"""
		# if the key isn't renamed, we save the time and don't delete
		if old_key != new_key:
			d[new_key] = d[old_key]
			del d[old_key]

	def transform_value (self, d, k, f):
		"""
		Change the value of a row in-place.
		
		A utility method to be called by subclasses. 
		"""
		d[k] = f(d[k])
		
	def key_to_name (self, k):
		"""
		Transforms keys to a form suitable for use in method names.
		
		Used in the dispatch to methods, this will map a key to a string
		suitable for constructing a method name, e.g. the key 'DATA1' becomes
		'data1' to called the method 'transform_data1'.
		"""
		#TODO: needs to cope with spaces and odd punctuation
		#TODO: can cache results?
		return lower (k)
