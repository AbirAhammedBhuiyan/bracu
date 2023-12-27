%{

#include"symbol_info.h"

#define YYSTYPE symbol_info*

int yyparse(void);
int yylex(void);

void yyerror(char *s);

extern FILE *yyin;

ofstream outlog;

int lines;
string str = "";

// declare any other variables or functions needed here



%}

%token IF ELSE FOR WHILE DO BREAK CONTINUE RETURN INT FLOAT CHAR VOID DOUBLE 
       SWITCH CASE DEFAULT PRINTLN ADDOP MULOP INCOP DECOP RELOP ASSIGNOP LOGICOP NOT LPAREN
       RPAREN LCURL RCURL LTHIRD RTHIRD SEMICOLON COMMA ID CONST_INT CONST_FLOAT THEN

%right THEN ELSE

%%

start : program
    {
        outlog<<"At line no: "<<lines<<" start : program "<<endl<<endl;
        outlog<<endl;
        outlog<<"Total lines: "<<lines<<endl;
    }
	;

program : program unit
    {
        outlog<<"At line no: "<<lines<<" program : program unit "<<endl<<endl;
        str = $1->getname()+"\n"+$2->getname();
        outlog<<str<<endl<<endl;
        $$ = new symbol_info(str,"program");
    }

	| unit
    {
        outlog<<"At line no: "<<lines<<" program : unit "<<endl<<endl;
        str = $1->getname();
        outlog<<str<<endl<<endl;
        $$ = new symbol_info(str, "program");
    }
	;

unit : var_declaration
        {
            outlog<<"At line no: "<<lines<<" unit : var_declaration "<<endl<<endl;
            str = $1->getname();
            outlog<<str<<endl<<endl;
            $$ = new symbol_info(str, "unit");
        }
    | func_definition
        {
            outlog<<"At line no: "<<lines<<" unit : func_definition "<<endl<<endl;
            str = $1->getname();
            outlog<<str<<endl<<endl;
            $$ = new symbol_info(str, "unit");
        }
    ;

func_definition : type_specifier ID LPAREN parameter_list RPAREN compound_statement
                    {
                        outlog<<"At line no: "<<lines<<" func_definition : type_specifier ID LPAREN parameter_list RPAREN compound_statement "<<endl<<endl;
                        str = $1->getname()+" "+$2->getname()+$3->getname()+ $4->getname()+$5->getname()+"\n"+$6->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "func_definition");
                    }
                | type_specifier ID LPAREN RPAREN compound_statement 
                    {
                        outlog<<"At line no: "<<lines<<" func_definition : type_specifier ID LPAREN RPAREN compound_statement "<<endl<<endl;
                        str = $1->getname()+" "+$2->getname()+$3->getname()+ $4->getname()+"\n"+$5->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "func_definition");
                    }
 		        ;

parameter_list : parameter_list COMMA type_specifier ID
                    {
                        outlog<<"At line no: "<<lines<<" parameter_list : parameter_list COMMA type_specifier ID "<<endl<<endl;
                        str = $1->getname() + $2->getname() + $3->getname() +" "+$4->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "parameter_list");
                    }
            | parameter_list COMMA type_specifier
                    {
                        outlog<<"At line no: "<<lines<<" parameter_list : parameter_list COMMA type_specifier "<<endl<<endl; 
                    }
            | type_specifier ID
                    {
                        outlog<<"At line no: "<<lines<<" parameter_list : type_specifier ID "<<endl<<endl;
                        str = $1->getname()+" "+$2->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "parameter_list");
                    }
            | type_specifier
                    {
                        outlog<<"At line no: "<<lines<<" parameter_list : type_specifier "<<endl<<endl;
                        str = $1->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "parameter_list");
                    }
            ;

compound_statement : LCURL statements RCURL
                        {
                            outlog<<"At line no: "<<lines<<" compound_statement : LCURL statements RCURL "<<endl<<endl;
                            str = $1->getname()+"\n"+$2->getname()+"\n"+$3->getname();
                            outlog<<str<<endl<<endl;
                            $$ = new symbol_info(str, "compound_statement");
                    
                        }
                | LCURL RCURL
                        {
                            outlog<<"At line no: "<<lines<<" compund_statement : LCURL RCURL "<<endl<<endl;
                            str = $1->getname()+$2->getname();
                            outlog<<str<<endl<<endl;
                            $$ = new symbol_info(str, "compound_statement");
                        }
                ;

var_declaration : type_specifier declaration_list SEMICOLON
                    {
                        outlog<<"At line no: "<<lines<<" var_declaration : type_specifier declaration_list SEMICOLON "<<endl<<endl;
                        str = $1->getname() + " " + $2->getname() + $3->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "var_declaration");
                    }
            ;

type_specifier : INT 
                {
                    outlog<<"At line no: "<<lines<<" type_specifier : INT "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "type_specifier");
                }
            | FLOAT
                {
                    outlog<<"At line no: "<<lines<<" type_specifier : FLOAT "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "type_specifier");
                }
            | VOID
                {
                    outlog<<"At line no: "<<lines<<" type_specifier : VOID "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "type_specifier");
                }
            ;

declaration_list : declaration_list COMMA ID
                    {
                        outlog<<"At line no: "<<lines<<" declaration_list : declaration_list COMMA ID "<<endl<<endl;
                        str = $1->getname()+$2->getname()+$3->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "declaration_list");
                    }
                | declaration_list COMMA ID LTHIRD CONST_INT RTHIRD
                    {
                        outlog<<"At line no: "<<lines<<" declaration_list : declaration_list COMMA ID LTHIRD CONST_INT RTHIRD "<<endl<<endl;
                        str = $1->getname() + $2->getname() + $3->getname() + $4->getname() + $5->getname() + $6->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "declaration_list");
                    }
                | ID
                    {
                        outlog<<"At line no: "<<lines<<" declaration_list : ID "<<endl<<endl;
                        str = $1->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "declaration_list");
                        
                    }
                | ID LTHIRD CONST_INT RTHIRD
                    {
                        outlog<<"At line no: "<<lines<<" declaration_list : ID LTHIRD CONST_INT RTHIRD "<<endl<<endl;
                        str = $1->getname() + $2->getname() + $3->getname() + $4->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "declaration_list");
                    }
                ;

statements : statement
                {
                    outlog<<"At line no: "<<lines<<" statements : statement "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statements");
                }
        | statements statement
                {
                    outlog<<"At line no: "<<lines<<" statements : statements statement "<<endl<<endl;
                    str = $1->getname()+"\n"+$2->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statements");
                }
        ;

statement : var_declaration
                {
                    outlog<<"At line no: "<<lines<<" statement : var_declaration "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | expression_statement
                {
                    outlog<<"At line no: "<<lines<<" statement : expression_statement "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | compound_statement
                {
                    outlog<<"At line no: "<<lines<<" statement : compound_statement "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | FOR LPAREN expression_statement expression_statement expression RPAREN statement
                {
                    outlog<<"At line no: "<<lines<<" statement : FOR LPAREN expression_statement expression_statement expression RPAREN statement "<<endl<<endl;
                    str = $1->getname()+$2->getname()+$3->getname()+$4->getname()+$5->getname()+$6->getname()+"\n"+$7->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | IF LPAREN expression RPAREN statement             %prec THEN
                {
                    outlog<<"At line no: "<<lines<<" statement : IF LPAREN expression RPAREN statement "<<endl<<endl;
                    str = $1->getname()+$2->getname()+$3->getname()+$4->getname()+"\n"+$5->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | IF LPAREN expression RPAREN statement ELSE statement
                {
                    outlog<<"At line no: "<<lines<<" statement : IF LPAREN expression RPAREN statement ELSE statement "<<endl<<endl;
                    str = $1->getname()+$2->getname()+$3->getname()+$4->getname()+"\n"+$5->getname()+"\n"+$6->getname()+"\n"+$7->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | WHILE LPAREN expression RPAREN statement
                {
                    outlog<<"At line no: "<<lines<<" statement : WHILE LPAREN expression RPAREN statement "<<endl<<endl;
                    str = $1->getname() + $2->getname() + $3->getname() + $4->getname() + "\n" +$5->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | PRINTLN LPAREN ID RPAREN SEMICOLON
                {
                    outlog<<"At line no: "<<lines<<" statement : PRINTLN LPAREN ID RPAREN SEMICOLON "<<endl<<endl;
                    str = $1->getname() + $2->getname() + $3->getname() + $4->getname() + $5->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                }
        | RETURN expression SEMICOLON
                {
                    outlog<<"At line no: "<<lines<<" statement : RETURN expression SEMICOLON "<<endl<<endl;
                    str = $1->getname() + " " + $2->getname()+ $3->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "statement");
                    
                }
        ;

expression_statement : SEMICOLON
                        {
                            outlog<<"At line no: "<<lines<<" expression_statement : SEMICOLON "<<endl<<endl;
                            str = $1->getname();
                            outlog<<str<<endl<<endl;
                            $$ = new symbol_info(str, "expression_statement");
                        }
                    | expression SEMICOLON
                        {
                            outlog<<"At line no: "<<lines<<" expression_statement : expression SEMICOLON "<<endl<<endl;
                            str = $1->getname()+$2->getname();
                            outlog<<str<<endl<<endl;;
                            $$ = new symbol_info(str, "expression_statement");
                        }
                    ;

variable : ID
            {
                outlog<<"At line no: "<<lines<<" variable : ID "<<endl<<endl;
                str = $1->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "variable");
            }
        | ID LTHIRD expression RTHIRD
            {
                outlog<<"At line no: "<<lines<<" variable : ID LTHIRD expression RTHIRD "<<endl<<endl;
                str = $1->getname()+$2->getname()+$3->getname()+$4->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "variable");
            }
        ;

expression : logic_expression
            {
                outlog<<"At line no: "<<lines<<" expression : logic_expression "<<endl<<endl;
                str = $1->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "expression");
            }
        | variable ASSIGNOP logic_expression
            {
                outlog<<"At line no: "<<lines<<" expression : variable ASSIGNOP logic_expression "<<endl<<endl;
                str = $1->getname()+$2->getname()+$3->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "expression");
            }
        ;

logic_expression : rel_expression
                    {
                        outlog<<"At line no: "<<lines<<" logic_expression : rel_expression "<<endl<<endl;
                        str = $1->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "logic_expression");
                    }
                | rel_expression LOGICOP rel_expression
                    {
                        outlog<<"At line no: "<<lines<<" logic_expression : rel_expression LOGICOP rel_expression "<<endl<<endl;
                        str = $1->getname()+$2->getname()+$3->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "logic_expression");
                    }
                ;

rel_expression : simple_expression
                    {
                        outlog<<"At line no: "<<lines<<" rel_expression : simple_expression "<<endl<<endl;
                        str = $1->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "rel_expression");
                    }
            | simple_expression RELOP simple_expression
                    {
                        outlog<<"At line no: "<<lines<<" rel_expression : simple_expression RELOP simple_expression "<<endl<<endl;
                        str = $1->getname()+$2->getname()+$3->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "rel_expression");
                    }
            ;

simple_expression : term
                    {
                        outlog<<"At line no: "<<lines<<" simple_expression : term "<<endl<<endl;
                        str = $1->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "simple_expression");
                    }
                | simple_expression ADDOP term
                    {
                        outlog<<"At line no: "<<lines<<" simple_expression : simple_expression ADDOP term "<<endl<<endl;
                        str = $1->getname() + $2->getname() + $3->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "simple_expression");
                    }
                ;

term : unary_expression
                {
                    outlog<<"At line no: "<<lines<<" term : unary_expression "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "term");
                }
    | term MULOP unary_expression
                {
                    outlog<<"At line no: "<<lines<<" term : term MULOP unary_expression "<<endl<<endl;
                    str = $1->getname()+$2->getname()+$3->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "term");
                }
    ;

unary_expression : ADDOP unary_expression
                    {
                        outlog<<"At line no: "<<lines<<" unary_expression : ADDOP unary_expression "<<endl<<endl;
                        str = $1->getname()+$2->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "unary_expression");
                    }
                | NOT unary_expression
                    {
                        outlog<<"At line no: "<<lines<<" unary_expression : NOT unary_expression "<<endl<<endl;
                        str = $1->getname()+$2->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "unary_expression");
                    }
                | factor
                    {
                        outlog<<"At line no: "<<lines<<" unary_expression : factor "<<endl<<endl;
                        str = $1->getname();
                        outlog<<str<<endl<<endl;
                        $$ = new symbol_info(str, "unary_expression");
                    }
                ;

factor : variable 
            {
                outlog<<"At line no: "<<lines<<" factor : variable "<<endl<<endl;
                str = $1->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
                
            }
    | ID LPAREN argument_list RPAREN
            {
                outlog<<"At line no: "<<lines<<" factor : ID LPAREN argument_list RPAREN "<<endl<<endl;
                str = $1->getname()+$2->getname()+$3->getname()+$4->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
            }
    | LPAREN expression RPAREN
            {
                outlog<<"At line no: "<<lines<<" factor : LPAREN expression RPAREN "<<endl<<endl;
                str = $1->getname()+$2->getname()+$3->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
            }
    | CONST_INT 
            {
                outlog<<"At line no: "<<lines<<" factor : CONST_INT "<<endl<<endl;
                str = $1->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
            }
    | CONST_FLOAT 
            {
                outlog<<"At line no: "<<lines<<" factor : CONST_FLOAT "<<endl<<endl;
                str = $1->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
            }
    | variable INCOP
            {
                outlog<<"At line no: "<<lines<<" factor : variable INCOP "<<endl<<endl;
                str = $1->getname()+$2->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
            }
    | variable DECOP
            {
                outlog<<"At line no: "<<lines<<" factor : variable DECOP "<<endl<<endl;
                str = $1->getname()+$2->getname();
                outlog<<str<<endl<<endl;
                $$ = new symbol_info(str, "factor");
            }
    ;

argument_list : arguments
                {
                    outlog<<"At line no: "<<lines<<" argument_list : arguments "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "argument_list");
                }
            |
                {
                    outlog<<"At line no: "<<lines<<" argument_list : "<<endl<<endl;
                    str = "";
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "argument_list");
                }
            ;

arguments : arguments COMMA logic_expression
                {
                    outlog<<"At line no: "<<lines<<" arguments : arguments COMMA logic_expression "<<endl<<endl;
                    str = $1->getname()+$2->getname()+$3->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "arguments");
                }
        | logic_expression
                {
                    outlog<<"At line no: "<<lines<<" arguments : logic_expression "<<endl<<endl;
                    str = $1->getname();
                    outlog<<str<<endl<<endl;
                    $$ = new symbol_info(str, "arguments");
                }
        ;

%%

void yyerror(char *s) {
    printf("BAD\n");
}


int main(int argc, char *argv[])
{
    ++lines;
	if(argc != 2) 
	{
        // check if filename given
	}
	yyin = fopen(argv[1], "r");
	outlog.open("output.txt", ios::trunc);
	
	if(yyin == NULL)
	{
		cout<<"Couldn't open file"<<endl;
		return 0;
	}
    
	yyparse();
	
	//print number of lines
	
	outlog.close();
	
	fclose(yyin);
	
	return 0;
}
