#!/bin/bash

flex 20101197.l && g++ lex.yy.c -o scanner && ./scanner input.txt

