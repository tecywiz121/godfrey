godfrey
=======

A natural language shell

INSTALLATION
============

Install nltk using pip

	$ pip install nltk

Install MaltParser from:

	http://www.maltparser.org/download.html
	1. Extract folder as /<path to godfrey>/maltparse
	2. Rename jar file in ./maltparse to malt.jar

Download the grammar from:

	http://www.maltparser.org/mco/english_parser/engmalt.linear-1.7.mco
	Move engmalt.linear-1.7.mco into the ./malparse folder

Install the proper NLTK tagger
	
	start a python instance
	>> nltk.download()
	Downloader> d
	Identifier> maxent_treebank_pos_tagger

Before running the program do this:

	$ export MALTPARSERHOME="/path/to/maltparser/"
