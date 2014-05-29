About dictmunger
================

   **munge**
   /muhnj/ *vt.* 
   
   1. To manipulate (raw data), especially to convert from one format to another
   2. [derogatory] To imperfectly transform information. 
   3. To modify data in some way the speaker doesn't need to go into right now or cannot describe.
   
A common programming task in Python is to take a stream of dictionaries - common data *lingua franca*, often extracted from a spreadsheet or database - and transform these in some way, modifying some values, deleting some keys, creating or renaming others. To this end, `dictmunger` is a package that simplifies writing the code for such transformations, providing base classes and functions for customisation.


Overview
--------

.. note: By convention, we refer our transforming and filtering classes as "mungers" and the key-value pairs in a dict as a "row".

The general idiom for using a munger is::

   >>> m = Munger()
   >>> d_1 = {1: 'one', 2: 'two', 3: 'three'}
   >>> d_2 = {'a': 'one', 'b': 'two', 'c': 'three'}
   >>> new_dict_1 = m.munge (d_1)
   >>> new_dict_2 = m.munge (d_2)
   
That is, create a munger and feed dicts through, catching the output. Note that the original dicts are not mutated in any way.

Some simple mungers are provided, but many transformation tasks can be achieved by subclassing `BaseDictMunger`. There are several ways to achieve this. First, by overriding class members:

* `transform_keys`: any rows with a matching key in this list will be dispatched to transformation methods. Rows will be processed by their order in the list. If the list is empty, all rows will be processed. The munger will first look a method `transform_<row name>` and otherwise will use `default_transform`.

* `create_keys`: the munger will create a row in the dict with the key passed in this list, and the value of the method `create_<row name>`.

* `keep_keys`: if any keys are defined in this list, only those rows are kept. If none are defined, all are kept.

* `delete_keys`: if any keys are defined in this list, those rows are deleted.

Next, by overriding various functions:

* `transform_<row key>()` 
* `default_transform()` for any row without a specific `transform_` method
* `move_key()` and `transform_value()` can be called by any custom methods to change keys and values respectively.


Built-in mungers
----------------

Some simple 







