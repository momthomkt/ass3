import unittest
from TestUtils import TestChecker
from AST import *

from Visitor import Visitor
from StaticError import *
from abc import ABC

class CheckerSuite(unittest.TestCase):
#     def test_TypeMismatchInSTMT_for1(self):
#         """test_TypeMismatchInBinExp_REMAINDER""" 
#         # OPERAND TYPE: INT
#         input = """_block: function void( block : string){
#     _e456 : integer = 672;
# 	do{block= "Block!";continue;}while(true || false);
# }
# main : function void(){}"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 401))
    def test_1(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = '''
            voidTS: function integer(){
                a,b,c,d,e : integer = 7,6,9,10,11;
                return 3*6*9;
            }
            main: function void () {
                delta: integer = (5);
                delta = voidTS();
            }
        '''
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        """mixed test"""
        input = """
        comeflywithme: function string() {
                return "come" + "fly" * "with" == "me";
        }
        """
        expect = """Type mismatch in expression: BinExpr(*, StringLit(fly), StringLit(with))"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """/*int a, b, c;
	a, b, c = 1, 2, 3;
	//int _123 = 456; cout << _123;
	string s = "alo		";
	//if (false);
	//else cout << 5;*/
_a_b_c : boolean = true;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_5(self):
        input = """a: integer;
b :boolean = true;
c :	string = "Hello World!";
main : function void(){}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_6(self):
        input = input = """y: integer = 300;
fuck: function integer(z : integer)
{
	if (z == 0) return 0;
	else return z + fuck(y - 1);
}
main: function void(){
	alpha: integer = fuck(100);
	flag: boolean = true;
}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_7(self):
        input = """tiger: function array [5,5] of float(x : float)
{
	if (x >= 0) return (5);
	else return z * tiger((x - 1));
}
function main: void(){}"""
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_8(self):
        input = """part : integer = 1+23*999/(85 + (2%4));"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_9(self):
        input = """main: function void(){
   init : integer = 0;
	for (i = 0, i < 100, i + 2) {
		a = init / 2 + init;
	}
}"""
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_10(self):
        input = """main: function integer(){
   init: integer = 0;
	while(5 > 3) init = init * 2;
}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 410))
################################################################################
    
    def test_11(self):
        input = """main: function array[5,5] of float(inherit out x : auto) {
    x = 1 + main(x) + (95);
}
return_ : boolean = false;"""
        expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), FuncCall(main, [Id(x)]))"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """  foo: function boolean(inherit out u : integer) inherit main{
        preventDefault();
        init: integer = 0;
	  do
	  {
		  init = init + 1_000_000;
	  } while (init < 100_000_000);
  }
  main : function void(){}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
        fact : function integer(inherit a : float, b: boolean){}
        main : function void() inherit fact{
            b : auto = .e-6;
            a : array[3] of string;
        }"""
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_14(self):
        input = """dream : function float(out o : boolean){return !true;}
        main : function void(){}"""
        expect = """Type mismatch in statement: ReturnStmt(UnExpr(!, BooleanLit(True)))"""
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_15(self):
        input = """main : function void(){
        a : integer;
if(a==6) printString("Toi nam nay hon 70 tuoi ma toi chua gap cai truong hop nao ma no nhu the nay ca");
}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test_16(self):
        input = """arr : array [3,3,3] of float;solokill : string = "My name is Master Yi"; main : function void(){}"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_17(self):
        input = """split_string : function string(inherit s : string) inherit fact{
    prev_x : boolean = true;
    return "Hello everyone";
}"""
        expect = """Undeclared Function: fact"""
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test_18(self):
        input = """plan : integer = 89;
reserve : function void(out param : integer){
    return param * (param/7 + 6);
}"""    
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(*, Id(param), BinExpr(+, BinExpr(/, Id(param), IntegerLit(7)), IntegerLit(6))))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test_19(self):
        input = """test_number : function boolean(inherit s : string){
    prev : string = "Hi, Peter";
    printString(prev);
    return true;
}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test_20(self):
        input = """d,e,f : float = 9.*2, .e45-3.5e4, 10.e45;
y,u,t :boolean = false,true, true;
z :	string = "My mom will visit me today";"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """foo: function auto() {break;}
        main : function void(){}"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """sentences,paragraph : array [5] of string = {"a","b","c","d","e"},{"f","g","h","i","j"};
        main : function void(){
        while(5){
        flash : boolean;
        }
        }"""
        expect = """Type mismatch in statement: WhileStmt(IntegerLit(5), BlockStmt([VarDecl(flash, BooleanType)]))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """hcmut_1 : array [2,2] of integer = {{1,2},{3,4}};"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_24(self):
        input = """
main1 : function void() inherit cut{
    decimal : boolean = !true;
}
cut : function integer(inherit decimal : integer){{{
    return decimal*decimal/5-2;
}}}"""
        expect = """Invalid statement in function: main1"""
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_25(self):
        input = """x: float = 301;
undercut: function integer(y : integer)
{
	if ((y != 0) || (y % 20 == 5)) {return 0;}
	else return y + undercut(y + 1);
}
main: function void(){
	alpha: integer = undercut(111);
	return false;
}"""
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_26(self):
        input = """glass : float = 1-2.E4*342%(85 * (4%2));
        main : function void(){}"""
        expect = r"""Type mismatch in expression: BinExpr(%, BinExpr(*, FloatLit(20000.0), IntegerLit(342)), BinExpr(*, IntegerLit(85), BinExpr(%, IntegerLit(4), IntegerLit(2))))"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """cat: function array [3] of integer(y : integer)
{
	if (1) {return {1,2,3};}
	else return {5,6,7};
}
main : function void(){}"""
        expect = r"""Type mismatch in statement: IfStmt(IntegerLit(1), BlockStmt([ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]), ReturnStmt(ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7)])))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """s_string : string = "I will get out by my way";
        main : function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """main: function integer(inherit out argg : auto){
    return 0;
}"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """extra: function void(_5678 : boolean){
    _b5678 : integer = 890;
	do{_b5678 = -5;}while((_b5678<1000) || (_b5678 %2==0));
}"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 430))
#################################################################################   
    def test_31(self):
        input = """f_cook : function boolean(inherit out u_cook : integer){
  initial: float = 0;
	  do
	  {
      init : float = .e-7;
		  run(init + 1.e45);
	  } while (initial < 987_654);
  }
  run : function void(a : float) inherit f_cook{}
  main : function void(){}"""
        expect = r"""Invalid statement in function: run"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """main : function void(){
    printString("Error");
    return 0;
}"""
        expect = r"""Type mismatch in statement: ReturnStmt(IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """hust_2 : array [2,3] of boolean = {{true,true,false},{false,false,true}};"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_34(self):
        input = """pop : function integer(out stack : array[5] of integer){
    {{}}
    return stack[0];
}
main : function void(){
i : integer;
    for(i = 3, i + 5, i+1){
        break;
    }
}"""
        expect = r"""Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([BreakStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_35(self):
        input = """main : function void(){}
circle: integer = 3000;
globular: function integer(x : integer, y : integer, z : boolean)
{
	if (x != 987 + 5 ) {return 112;}
	else return y * circle(y - 5);
}"""
        expect = r"""Undeclared Function: circle"""
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_36(self):
        input = """dog: function integer(a : float)
{
	if (a == true) {return 3/(5*4)/6+9;}
	else return 0;
}"""
        expect = r"""Type mismatch in expression: BinExpr(==, Id(a), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_37(self):
        input = """mountain : auto = {1,3.e5,"Hello World!"};
        main : function void(){}"""
        expect = r"""Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(300000.0), StringLit(Hello World!)])"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_38(self):
        input = """Soobin: function integer(music : integer) inherit single{
    return music + single("Hello");
}
single : function integer(inherit name : string){}
main : function void(){}"""
        expect = r"""Invalid statement in function: Soobin"""
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_39(self):
        input = """SONTUNGMTP: function void(_chay_ngay_di_ : float){
    _hay_trao_cho_anh : string;
	do{_hay_trao_cho_anh = "Wow!";break;}while(_chay_ngay_di_ > -6 || (_chay_ngay_di_ * 2 < 6));
}"""
        expect = r"""Type mismatch in expression: BinExpr(||, UnExpr(-, IntegerLit(6)), BinExpr(<, BinExpr(*, Id(_chay_ngay_di_), IntegerLit(2)), IntegerLit(6)))"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_40(self):
        input = """  repeat: function void(out u_cook : integer){
  after: float = 81;
	  do
	  {
        continue;
		  x = after + .e+06;
	  }while ("alo123");
  }
main : function void(){}"""
        expect = r"""Type mismatch in statement: DoWhileStmt(StringLit(alo123), BlockStmt([ContinueStmt(), AssignStmt(Id(x), BinExpr(+, Id(after), FloatLit(0.0)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
#######################################################################################################
    def test_41(self):
        input = """interger : function integer(){
    string1 : string = "Hello World";
    printfirs_lesson();
    return 1;
}"""
        expect = r"""Undeclared Function: printfirs_lesson"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """QSB_1 : array [1,1] of float = {{3.5E+6}};
main : function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        bigbang: function string(out gangto : string) {
                return gangto + bigbang(gangto);
                bigbang(gangto);
        }
        main : function void(){}
        """
        expect = r"""Type mismatch in expression: BinExpr(+, Id(gangto), FuncCall(bigbang, [Id(gangto)]))"""
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_44(self):
        input = """top : function boolean(out queue : array[5] of integer){{
    for(i = 6,i<100,i*2) readInteger();
}}
main : function void(){}"""
        expect = r"""Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_45(self):
        input = """square: integer = 25;
cube: function integer(a : integer,out b : float,inherit i : integer)
{
	if (a != 0 || b > 2 == true) {
        for(i = 0, i >-50, i-1)
        a = a * 2;
        break;
    }
	else return "";
}"""
        expect = r"""Type mismatch in expression: BinExpr(||, IntegerLit(0), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_46(self):
        input = """bird: function array [6,6] of float(nump : integer, oop : float) inherit sunny{}
    sunny : function boolean(){}
    main : function void(){
        return 0;
    }"""
        expect = r"""Type mismatch in statement: ReturnStmt(IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_47(self):
        input = """forest : auto = "Nguyen Van Tan"::"{1,2,3}";"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_48(self):
        input = """main : function void(){
    arr : array[5,5] of boolean;
}
Bac_Da : function string(meme : string){
    return "Toi nam nay 70 tuoi ma toi chua gap truong hop nao nhu the nay";
}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_49(self):
        input = """apolo,gaia,roto : integer = 1,23,{a[5],6,g,(rainy())};
        main : function void(){}"""
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_50(self):
        input = """main : function void(){}
prepare: function void(inherit u_cook : array[2,3,4] of integer){
  prepare: float = 64;
  while (prepare >= 987_654)
	  {
        continue;
		u_cook[5,6*2] = {1,2,3,4};
	  }
}
alo : function void() inherit prepare{
    u_cook : string = "You cut";
}"""
        expect = r"""Invalid statement in function: alo"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """main : function void(){
    _void();
}
_void : function void(){
     second_lesson : string = "Hello World";
printString(firs_lesson);
    return ;
}"""
        expect = r"""Undeclared Identifier: firs_lesson"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """UEH_1 : array [2] of string = {"Nguyen Minh Quoc;",";"};"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """main :function void(){}
T1_faker : function float(inherit mid : string){{
    for(j = -1,j<10*4,5+1) readFloat();
}}"""
        expect = r"""Undeclared Identifier: j"""
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_54(self):
        input = """rectangle: integer = 225;
rectangular: function string(u : float, v : float, x : string) inherit main
{
	return "!1";
}
main : function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_55(self):
        input = """elephant: function array [1000,1000] of string(out head : integer, main : float){  
    funtion : string;{
    }
}main :function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_56(self):
        input = """main: function void(){}
        main : string = "alo123";main,int : float = 123456.e5,35.34;"""
        expect = r"""Redeclared Variable: main"""
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_57(self):
        input = """main : function void(){}
        many_tree : function void() {
{
    option : boolean;
    {
        option : string = "Alo";
        {
            option : integer = 5;
        }
    }
    {
        return ;
    }
}
        }"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_58(self):
        input = """min : function integer(){
    place,go,lexer_rule : boolean;
    place = true;
    go = false;
    lexer_rule = fals;
}
main : function void(){
    min();
}"""
        expect = r"""Undeclared Identifier: fals"""
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_59(self):
        input = """venus,mar,earth : float = 1,e45,5e56;"""
        expect = r"""Undeclared Identifier: e45"""
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_60(self):
        input = """main : function void(){}
solar_system: function integer(planet : integer){
initial : integer = 0;
  while (initial < 987_654)
	  {
        i : integer = 0;
        for(i = 5,i<5555,i*5)
        if(planet > 50_00_00){
            planet = (planet + 5 -4 == 2) != 500_0;
        }
        else{}
        break;
	  }
}"""
        expect = r"""Type mismatch in statement: AssignStmt(Id(planet), BinExpr(!=, BinExpr(==, BinExpr(-, BinExpr(+, Id(planet), IntegerLit(5)), IntegerLit(4)), IntegerLit(2)), IntegerLit(5000)))"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """zues : function integer(a : integer){{
    if(((2+3/5 == 8 != 98)))
    if(false) return 2;
}}
main :function void(){zues();}"""
        expect = r"""Type mismatch in statement: CallStmt(zues, )"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """colombia : integer;mar : float = 96; index : integer = 5;colombiia : auto = 99;"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """main :function void(){__6bgh9(5.4e+2);}
__6bgh9 : function integer(inherit out flag : float) inherit foo{
            preventDefault();{
    do {flag = flag * 2;}
    while((true));}
    return 555%5;
}
foo : function auto(flag : integer){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_64(self):
        input = """main :function void(){{{}}}
parallelogram: function auto(a : auto, b : auto, h : auto) inherit main
{
	return (a + b) * h / 2;
    return;
}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """main :  function void(){}
        spider: function array [1024,1024] of integer(weight : float, height : float){{
        return (weight + 6) * height;
    }
}"""
        expect = r"""Type mismatch in statement: ReturnStmt(BinExpr(*, BinExpr(+, Id(weight), IntegerLit(6)), Id(height)))"""
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_66(self):
        input = """alo : integer = 98;
main : function void(out a : auto){
    foo : float;
    arr : array[2,2] of float = {{2+6,2/5},{foo,alo}};
    arr[0,0] = 9;
}
"""
        expect = r"""Illegal array literal: ArrayLit([Id(foo), Id(alo)])"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """description : string = "I am the best";
main1 : function integer(a : auto){
    a = "string";
    b : float = a;
    return 0;
}
main : function void(){}"""
        expect = r"""Type mismatch in Variable Declaration: VarDecl(b, FloatType, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """string_TheRock : string = "I will kill you. Fuck you!"; _inta : integer; """
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """_main_main: function float(inherit arg : auto){
    return 0;
}"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """plus: function auto(a : integer,b : integer){
    return (a + b);
}
main : function void(){{
    s: string = plus(5,6);
}}"""
        expect = r"""Type mismatch in Variable Declaration: VarDecl(s, StringType, FuncCall(plus, [IntegerLit(5), IntegerLit(6)]))"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """  shark: function array[2,4] of integer(out float_shark : integer){shark();
  }"""
        expect = r"""Type mismatch in statement: CallStmt(shark, )"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """main : function void(){impact("alo");}
    impact : function integer(inherit oop : string) inherit foo{
    super("Goodbye");
    i : integer;
    s = "Hello";
    for(i = 0,true ,i+1){
        s: float;
    }


    return -0;
}
foo : function void(inherit s :  string){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """UEL_1 : array [2,3] of string = {false,true,false,false,true,true};"""
        expect = r"""Type mismatch in Variable Declaration: VarDecl(UEL_1, ArrayType([2, 3], StringType), ArrayLit([BooleanLit(False), BooleanLit(True), BooleanLit(False), BooleanLit(False), BooleanLit(True), BooleanLit(True)]))"""
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_74(self):
        input = """enqueue : function integer(queue : array[5] of integer){
    return queue[-1];
    {{}}
}
main : function void(){enqueue({1,2,3,4,5});}"""
        expect = r"""Type mismatch in statement: CallStmt(enqueue, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_75(self):
        input = """Cone, au_to, cont : integer = 3000, fizz(), 300;"""
        expect = r"""Undeclared Function: fizz"""
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_76(self):
        input = """_5chicken_: function array [9,5,6,10] of integer(a : float)
{
	return "Hello World!";
}
main : function void(){}"""
        expect = r"""Type mismatch in statement: ReturnStmt(StringLit(Hello World!))"""
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_77(self):
        input = """TOM: function array [2,3] of integer(A : array [2,3] of integer) inherit i
{
    preventDefault();
	return A;
}
i :  function void(A: boolean){}
main : function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_78(self):
        input = """Nuclear_Power: function boolean(power : string){
    return power;
}"""
        expect = r"""Type mismatch in statement: ReturnStmt(Id(power))"""
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_79(self):
        input = """_block: function void( block : string){
    _e456 : integer = 672;
	do{block= "Block!";continue;}while(true || false);
}
main : function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_80(self):
        input = """  arrange: function array[5,5,5,5,5,5] of boolean(inherit out u_cook : auto){
    arrange : integer = 81;
    if (arrange % 9 == 0) printString("So nay chia het cho 9");
    printString("So nay khong chia het cho 9");
  }"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """class : function float(subClass : float){
        init_index : boolean = false == true;
    if(subClass + 5 - 6 + 7 <= 5.e-6)
    {
        while(init_index || subClass){
            sub_index : float = 9.;
        }
    }
    else return .e9999999999999;
}
main : function void(){}"""
        expect = r"""Type mismatch in expression: BinExpr(||, Id(init_index), Id(subClass))"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """_2k1 :  string = "See you again";Mexico : integer;taco : float; Cactus : integer = 5;Mexiico : string = _2k1;
        main :  function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """main : function void(){}
solve_function : function array[3,5] of integer(param1 : integer, out param2 : integer, inherit param3 : integer)inherit triangle{}"""
        expect = r"""Undeclared Function: triangle"""
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_84(self):
        input = """main : function void(){}
triangle: function float(inherit day: float, chieu_cao : float)
{
    S : float = day * chieu_cao / 2;
	return S;
}
square : function float() inherit triangle{
    super(5,6);
    chieu_cao : string = "Hello";
    {
        day : boolean = true;
    }
}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = """flower : function auto(inherit properties : auto) inherit plant{
        super(properties);
    return properties;
}
plant : function integer(c :  integer){
    a :  integer = flower(c);
    b : integer = flower("alo");
}
main : function void(){}"""
        expect = r"""Type mismatch in expression: FuncCall(flower, [StringLit(alo)])"""
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test_86(self):
        input = """alo : string = "That's a beautiful girl";
alo : function float(feeling : string){
    
} main : function void(){}
"""
        expect = r"""Redeclared Function: alo"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """description : string = "Follow me, go straight ahead!.";
main : function void(a : string){
    a = description :: "If you don\\'t do it you will die.";
}"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """mind : function auto(feeling : string){
            if(feeling == "") feeling = "You make my heart flutter";
            else
            printString(feeling);
        }"""
        expect = r"""Type mismatch in expression: BinExpr(==, Id(feeling), StringLit())"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """main : function void(){}
        chill : function boolean(feeling : string){
    k : integer;
    for(k = 5.4,k == 999999,k%8)
    feeling = "I'm still waiting until you come";
}"""
        expect = r"""Type mismatch in statement: AssignStmt(Id(k), FloatLit(5.4))"""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """main : function void(){
        a : integer = mul(9.,.e-7);
        }
mul: function auto(a : float,b : float){
    return (a * b);
}"""
        expect = r"""Type mismatch in statement: ReturnStmt(BinExpr(*, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 490))
####################################################################
    def test_91(self):
        input = """sub_overide: function float(x : float,y : float){
    return a - b;
}"""
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """plus_overide_arr : function array[5] of integer(array1 : array[5] of integer, array2 : array[5] of integer){
    i : integer = 5;
    gam : integer = array1[i] + array2[i];
}"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """otrafford : array[3] of string = {"Man", "ches", "ter"};"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_94(self):
        input = """linklist : function auto(inherit linklist : array[9] of integer){
    {{
        c : auto = linklist[-9];
        linklist[-9] = linklist[9];
        linklist[9] = c;
    }}
    return c;
}"""
        expect = r"""Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_95(self):
        input = """main : function integer(){
    s : string = "Hello every one. This is my account.\t";
}
main : function void(){}"""
        expect = r"""Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_96(self):
        input = """fast: function array [5,8] of float(and : float)
{
	do
    and = .e67;
    while(1);
}main : function void(){}"""
        expect = r"""Type mismatch in statement: DoWhileStmt(IntegerLit(1), AssignStmt(Id(and), FloatLit(0.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test_97(self):
        input = """SU_57: function integer(_5th_generation_fighter : auto)
{
	return _5th_generation_fighter * 5;
}"""
        expect = r"""No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_98(self):
        input = """fusion_energy: function boolean(energy : string){
    h : boolean = 5 == 7;
    printBoolean(h);
    return h;
} main : function void(){}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_99(self):
        input = """main : function void(){}
_socpe: function void( scope : string){
    _sub_scope : string = scope :: "{}";
	do{_sub_scope= "New scope!";break;}while(true != false);
}"""
        expect = r""""""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test_100(self):
        input = """
foo : function boolean(x : string, inherit out y: integer){}
a, b, c : float = 5., .e-4, 7.e+5;
main : function void() inherit foo
{
    super("truy cap",99);
        y = 5;
        x = 6;
}"""
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 500))