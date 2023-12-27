#!/bin/bash

yacc -d -y --debug --verbose 'syntax_analyzer.y' &&
echo 'Generated the parser C file as well the header file' &&
g++ -w -c -o y.o y.tab.c &&
echo 'Generated the parser object file' &&
flex 'lex_analyzer.l' &&
echo 'Generated the scanner C file' &&
g++ -fpermissive -w -c -o l.o lex.yy.c && 
# if the above command doesn't work try g++ -fpermissive -w -c -o l.o lex.yy.c
echo 'Generated the scanner object file' &&
g++ y.o l.o -o parser &&
echo "Cleaning byproduct files" &&
find . ! -name '*.l' ! -name '*.y' ! -name '*.txt' ! -name 'parser' ! -name '*.sh' ! -name 'symbol_info.h' ! -name 'TreeNode.h' -type f -exec rm {} +
echo 'All ready, running' && 
./parser ./input.txt 
