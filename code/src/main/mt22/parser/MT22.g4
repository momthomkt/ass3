// 1915063
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF ;
// 5. Declarations
decllist: decl decllist | decl;
decl: vardecl | funcdecl;
vardecl: (idlist COLON var_typ SEMI) | (IDENTIFIER vardecl_mid value_assigned SEMI);
vardecl_mid: (COMMA IDENTIFIER vardecl_mid value_assigned COMMA) | (COLON var_typ ASSIGN);
// value_assigned: expr | arraylit;
value_assigned: expr;
// (idlist COLON var_typ ASSIGN exprlist SEMI)
idlist: IDENTIFIER COMMA idlist | IDENTIFIER;

//// 5.2. Function declarations
funcdecl: func_prototype func_body;

// function prototype
func_prototype: IDENTIFIER COLON FUNCTION typ paramdecl ((INHERIT IDENTIFIER) | );
paramdecl: LB paramlist RB;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: (INHERIT | ) (OUT | ) IDENTIFIER COLON var_typ;

//  function body
func_body: LP content_list RP;
content_list: content_prime | ;
content_prime: content content_list | content;
content: vardecl | stmt;

// 7. Statements
stmtlist: stmt stmtlist | ;
stmt: assignstmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | continue_stmt | return_stmt | func_call_stmt | block_stmt;

//// 7.1 Assignment Statement
assignstmt: lhs ASSIGN expr SEMI;
lhs: (IDENTIFIER index_operator) | (IDENTIFIER);

//// 7.2 If statement
if_stmt: (IF LB expr RB stmt)  | (IF LB expr RB stmt ELSE stmt);
//// 7.3 For statement
for_stmt: FOR LB (IDENTIFIER | array_operand) ASSIGN expr COMMA expr COMMA expr RB stmt;

//// 7.4. While statement
while_stmt: WHILE LB expr RB stmt;

//// 7.5. Do-while statement
// dowhile_stmt: DO block_stmt WHILE LB expr RB SEMI;
dowhile_stmt: DO stmt WHILE LB expr RB SEMI;

//// 7.6. Break statement
break_stmt: BREAK SEMI;

//// 7.7. Continue statement
continue_stmt: CONTINUE SEMI;

//// 7.8. Return statement
return_stmt: (RTURN expr SEMI) | (RTURN SEMI);

//// 7.10. Block statement
block_stmt: func_body;
// bb: vardecl | stmtlist;

///    Function call
func_call_stmt: IDENTIFIER LB exprlist RB SEMI;

/////6. Expression
exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;

expr: expr1 DOUBLE_COLON expr1 | expr1;
// expr1: expr2 (EQUAL | DIFF | LESS | LARGER | LESSE | LARGERE) expr2 | expr2;
expr1: expr1 (EQUAL | DIFF | LESS | LARGER | LESSE | LARGERE) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: IDENTIFIER index_operator | operands;
// expr7: expr7 IDENTIFIER index_operator | operands;
index_operator: LSB exprlist RSB;
operands: (LB expr RB) | BOOLEANLIT | IDENTIFIER | INTLIT | FLOATLIT | STRINGLIT | func_call | array_operand | arraylit;
array_operand: IDENTIFIER index_operator;
func_call: IDENTIFIER LB exprlist RB;
//Array
arraylit: LP exprlist RP;


//Type
typ: atomic_typ | array_typ | void_typ | auto_typ;
var_typ: atomic_typ | array_typ | auto_typ;
atomic_typ: BOOLEAN | INTEGER | FLOAT | STRING;

array_typ: ARRAY LSB intlist RSB OF atomic_typ;
intlist: INTLIT COMMA intlist | INTLIT;

void_typ: VOID;
auto_typ: AUTO;
//Comment/////////////////////////////////
// - C-style
C_CMT: '/*' .*? '*/' -> skip ;
// - C++-style
Cpp_CMT: '/' '/' .*? ([\r\n\f] | EOF) -> skip;

// Keywords ///////////////////////////////
AUTO: 'auto'; BREAK: 'break'; BOOLEAN: 'boolean'; DO: 'do'; ELSE: 'else';
/*FALSE: 'false';*/ FLOAT: 'float'; FOR: 'for'; FUNCTION: 'function'; IF: 'if';
INTEGER: 'integer'; RTURN: 'return'; STRING: 'string'; /*TRUE: 'true';*/ WHILE: 'while';
VOID: 'void'; OUT: 'out'; CONTINUE: 'continue'; OF: 'of'; INHERIT: 'inherit';
ARRAY: 'array';

// Operators
ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%';
NOT: '!'; AND: '&&'; OR: '||'; EQUAL: '=='; DIFF: '!=';
LESS: '<'; LESSE: '<='; LARGER: '>'; LARGERE: '>='; DOUBLE_COLON: '::';

// Seperators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOTS: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LP: '{';
RP: '}';
ASSIGN: '=';


//Boolean
BOOLEANLIT: 'true' | 'false';
// Identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
INTLIT: ('0' | [1-9] [0-9]* ('_' [0-9]+)*) {self.text = self.text.replace("_", "")};

// Float
FLOATLIT: ((INTPART DECPART) | (INTPART DECPART? EXPPART) | (DECPART EXPPART)){self.text = self.text.replace("_", "")};
fragment INTPART: ('0' | [1-9] [0-9]* ('_' [0-9]+)*);
fragment DECPART: DOTS [0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;

//String
STRINGLIT: (DoubleQ (CHAR_SET |('\\' DoubleQ))* DoubleQ) {self.text = self.text[1:-1]};
fragment DoubleQ: '"';
fragment CHAR_SET: ~(["\r\n] | '\\') | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt'\\];




// 4. Type system and values
//// 4.1. Atomic types
////// 4.1.1. Boolean type
BOOLEAN_OP: NOT | AND | OR | EQUAL | DIFF;

////// 4.1.2 Integer type
INT_OP: ADD | SUB | MUL | DIV | MOD | EQUAL | DIFF | LARGER | LARGERE | LESS | LESSE;

//////4.1.3 Float type
FLOAT_OP: ADD | SUB | MUL | DIV | EQUAL | DIFF | LARGER | LARGERE | LESS | LESSE;

////// 4.1.4. String
STRING_OP: DOUBLE_COLON;

////// 4.2. Array
// Đã làm

WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: (DoubleQ (CHAR_SET |'\\' DoubleQ)* (EOF | [\r\n])){
z = self.text
if z[-1] in ['\r', '\n', '\f']:
	raise UncloseString(z[1:-1])
else:
    raise UncloseString(z[1:])
};

ILLEGAL_ESCAPE: (DoubleQ (CHAR_SET |'\\' DoubleQ)* ESC_ILLEGAL){
	raise IllegalEscape(self.text[1:])
};
fragment ESC_ILLEGAL: '\\' ~[bfrnt'"\\] | '\\';
ERROR_TOKEN: . {raise ErrorToken(self.text)};