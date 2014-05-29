from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='dictmunger',
	version=version,
	description="Mapping and transformation of dictionaries",
	long_description="""\
A common programming task is to munge a stream of dicts resulting reading a
a CSV file, a database table or so on. This package aids that process by
providing a classes to transform and filter dicts and their contents.
	""",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
	],
	keywords='dict transformation xml',
	author='Paul Agapow',
	author_email='pma@agapow.net',
	url='http://www.agapow.net/software/dictmunger/',
	license='MIT',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
	# -*- Extra requirements: -*-
	],
	entry_points="""
	# -*- Entry points: -*-
	""",
	test_suite='nose.collector',
	tests_require=['nose'],
)
