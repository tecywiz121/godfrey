#!/bin/bash

# Async stuff

# lib dance
wget http://maltparser.org/dist/maltparser-1.7.2.tar.gz&
WGET_MALP_PID=$!
wget http://www.maltparser.org/mco/english_parser/engmalt.linear-1.7.mco&
WGET_GRAMMAR_PID=$!

# venv dance
virtualenv --distribute venv&
VENV_INSTALL_PID=$!

# Sync stuff

# libs
wait $WGET_MALT_PID
tar xf maltparser-1.7.2.tar.gz
rm maltparser-1.7.2.tar.gz
mv maltparser-1.7.2 maltparse
mv maltparse/maltparser-1.7.2.jar maltparse/malt.jar

wait $WGET_GRAMMAR_PID
mv engmalt.linear-1.7.mco maltparse/engmalt.linear-1.2.mco

# pip
wait $VENV_INSTALL_PID
source venv/bin/activate
pip install -r requirements.txt
PIP_INSTALL_PID=$!

echo "import nltk; nltk.download(); exit()" > python

# done!
echo "######################################################################"
echo "All set!  Run 'source venv/bin/activate' to get into your environment!"
echo "######################################################################"

