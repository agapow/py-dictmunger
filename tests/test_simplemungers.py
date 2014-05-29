"""
Test the simplemungers package, with nose.
"""

### IMPORTS

from dictmunger.simplemungers import *


### CONSTANTS & DEFINES

# dictionaries for testing
TEST_DICT_1 = {
	'one': 1,
	'Two': 2,
	'THREE': 3,
}

TEST_DICT_EMPTY = {
	'one': False,
	'two': None,
	'three': '',
	'four': [],
	'five': 'EMPTY',
}

### CODE ###

def test_lowercase():
	m = LowercaseKeyMunger()
	munged_d = m.munge (TEST_DICT_1) 

	print (munged_d)
	print sorted (munged_d.keys())

	assert (sorted (munged_d.keys()) == ['one', 'three', 'two'])


def test_transformval():
	fn = lambda x: max (1.5, x)
	m = TransformValMunger (fn)
	munged_d = m.munge (TEST_DICT_1) 

	print (munged_d)
	print sorted (munged_d.values())

	assert (sorted (munged_d.values()) == [1.5, 2, 3])

def test_deleteemptyval_1 ():
	m = DeleteEmptyValMunger()
	munged_d = m.munge (TEST_DICT_1) 

	assert (len (munged_d) == 3)


def test_deleteemptyval_2 ():
	m = DeleteEmptyValMunger()
	munged_d = m.munge (TEST_DICT_EMPTY) 

	assert (len (munged_d) == 2)
	assert (False in munged_d.values())
	assert ('EMPTY' in munged_d.values())

def test_deleteemptyval_3 ():
	m = DeleteEmptyValMunger ([False, 'EMPTY', 'foo'])
	munged_d = m.munge (TEST_DICT_EMPTY) 

	assert (len (munged_d) == 3)
	for x in [None, '', []]:
		assert (x in munged_d.values())

def test_keepkey_1():
	# an unexpected result - but look at definition fo keep_keys
	m = KeepKeyMunger([])
	munged_d = m.munge (TEST_DICT_EMPTY)
	assert (len (munged_d) == 4)

def test_keepkey_2 ():
	m = KeepKeyMunger (['one', 'two', 'Three', 'seven'])
	munged_d = m.munge (TEST_DICT_EMPTY) 

	assert (len (munged_d) == 2)
	for x in ['one', 'two']:
		assert (x in munged_d.keys())

def test_delkey_1():
	m = DelKeyMunger([])
	munged_d = m.munge (TEST_DICT_EMPTY)
	assert (len (munged_d) == 5)

def test_delkey_2 ():
	m = DelKeyMunger (['one', 'two', 'Three', 'seven'])
	munged_d = m.munge (TEST_DICT_EMPTY) 

	assert (len (munged_d) == 3)
	for x in ['three', 'four', 'five']:
		assert (x in munged_d.keys())



### END ###
