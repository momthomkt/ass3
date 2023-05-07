# 1915063
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    ## program: decllist EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # return Program([])
        return Program(self.visit(ctx.decllist()))
    
    ## decllist: decl decllist | decl;
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.decllist():
            return self.visit(ctx.decl()) + self.visit(ctx.decllist())
        else:
            return self.visit(ctx.decl())

    ## decl: vardecl | funcdecl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) ## List
        else:
            return [self.visit(ctx.funcdecl())] ## List
    
# ## vardecl

    ## vardecl: (idlist COLON var_typ SEMI) | (IDENTIFIER vardecl_mid value_assigned SEMI);
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.vardecl_mid():
            prevVardecl = self.visit(ctx.vardecl_mid())
            vartyp = prevVardecl[-1]
            prevVardecl.pop(-1)
            id = ctx.IDENTIFIER().__str__()
            value_ass = self.visit(ctx.value_assigned())
            lstVardecl = [VarDecl(id,vartyp,value_ass)] + prevVardecl

            result = []
            _max = len(lstVardecl)
            for i in range(_max):
                ele = VarDecl(lstVardecl[i].name,lstVardecl[i].typ,lstVardecl[i].init)
                ele.init = lstVardecl[-(i+1)].init
                result = result + [ele]
            
            return result
        else:
            id_lst = self.visit(ctx.idlist())
            vartyp = self.visit(ctx.var_typ())
            return [(VarDecl(x, vartyp)) for x in id_lst]

    ## idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.COMMA():
            return [ctx.IDENTIFIER().__str__()] + self.visit(ctx.idlist())
        else:
            return [ctx.IDENTIFIER().__str__()]

    ## var_typ: atomic_typ | array_typ | auto_typ;
    def visitVar_typ(self, ctx: MT22Parser.Var_typContext):
        if ctx.atomic_typ():
            return self.visit(ctx.atomic_typ())
        elif ctx.array_typ():
            return self.visit(ctx.array_typ())
        else:
            return self.visit(ctx.auto_typ())
    
    ## vardecl_mid: (COMMA IDENTIFIER vardecl_mid value_assigned COMMA) | (COLON var_typ ASSIGN);
    def visitVardecl_mid(self, ctx: MT22Parser.Vardecl_midContext):
        if ctx.vardecl_mid():
            id = ctx.IDENTIFIER().__str__()
            vartyp = self.visit(ctx.vardecl_mid())[-1]
            init = self.visit(ctx.value_assigned())
            return [VarDecl(id,vartyp,init)] + self.visit(ctx.vardecl_mid())
        else:
            return [self.visit(ctx.var_typ())]
    
    ## value_assigned: expr;
    def visitValue_assigned(self, ctx: MT22Parser.Value_assignedContext):
        return self.visit(ctx.expr())
    #########################################################################
    
# ## funcdecl

    ## funcdecl: func_prototype func_body;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        prototype = self.visit(ctx.func_prototype()) ## List
        body = self.visit(ctx.func_body()) ## Object BlockStmt()
        name = prototype[0]
        return_type = prototype[1]
        params = prototype[2]
        if (len(prototype) == 3):
            return FuncDecl(name, return_type, params, None, body)
        else:
            inher = prototype[3]
            return FuncDecl(name, return_type, params, inher, body)
    
    ## func_prototype: IDENTIFIER COLON FUNCTION typ paramdecl ((INHERIT IDENTIFIER) | );
    def visitFunc_prototype(self, ctx: MT22Parser.Func_prototypeContext):
        if ctx.INHERIT():
            return [ctx.IDENTIFIER(0).__str__(), self.visit(ctx.typ()), self.visit(ctx.paramdecl()), ctx.IDENTIFIER(1).__str__()] ##[str, Typ, [object ParamDecl(),...], str]
        else:
            return [ctx.IDENTIFIER(0).__str__(), self.visit(ctx.typ()), self.visit(ctx.paramdecl())] ##[str, Typ, [object ParamDecl(),...]]
    ## func_body: LP content_list RP;
    def visitFunc_body(self, ctx: MT22Parser.Func_bodyContext):
        return BlockStmt(self.visit(ctx.content_list()))
    
    ## paramdecl: LB paramlist RB;
    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        return self.visit(ctx.paramlist())
    
    ## paramlist: paramprime | ;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.paramprime():
            return self.visit(ctx.paramprime())
        else:
            return []
    

    ## paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.COMMA():
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
        else:
            return [self.visit(ctx.param())]
    
    ## param: (INHERIT | ) (OUT | ) IDENTIFIER COLON var_typ;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        inherit = False
        out = False
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True

        return ParamDecl(ctx.IDENTIFIER().__str__(), self.visit(ctx.var_typ()), out, inherit)
    
    ## content_list: content_prime | ;
    def visitContent_list(self, ctx: MT22Parser.Content_listContext):
        if ctx.content_prime():
            return self.visit(ctx.content_prime())
        return []
    
    ## content_prime: content content_list | content;
    def visitContent_prime(self, ctx: MT22Parser.Content_primeContext):
        if ctx.content_list():
            return self.visit(ctx.content()) + self.visit(ctx.content_list())
        else:
            return self.visit(ctx.content())
    
    ## content: vardecl | stmt;
    def visitContent(self, ctx: MT22Parser.ContentContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return [self.visit(ctx.stmt())]

# ## stmt
    
    ## stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
        else:
            return []

    ## stmt: assignstmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | continue_stmt | return_stmt | func_call_stmt |block_stmt;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.dowhile_stmt():
            return self.visit(ctx.dowhile_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.func_call_stmt():
            return self.visit(ctx.func_call_stmt())
        else:
            return self.visit(ctx.block_stmt())
    
    ## assignstmt: lhs ASSIGN expr SEMI;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    ## if_stmt: (IF LB expr RB stmt)  | (IF LB expr RB stmt ELSE stmt);
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        else:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))
    
    ## for_stmt: FOR LB IDENTIFIER ASSIGN expr COMMA expr COMMA expr RB stmt;
    ## for_stmt: FOR LB (IDENTIFIER | array_operand) ASSIGN expr COMMA expr COMMA expr RB stmt;
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        lhs=""
        expr0 = self.visit(ctx.expr(0))
        expr1 = self.visit(ctx.expr(1))
        expr2 = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        if ctx.IDENTIFIER():
            lhs = Id(ctx.IDENTIFIER().__str__())
        else:
            lhs = self.visit(ctx.array_operand())
        return ForStmt(AssignStmt(lhs,expr0),expr1,expr2,stmt)
    
    ## while_stmt: WHILE LB expr RB stmt;
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))
    
    ## dowhile_stmt: DO stmt WHILE LB expr RB SEMI;
    def visitDowhile_stmt(self, ctx: MT22Parser.Dowhile_stmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))
    
    ## break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    ## continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return ContinueStmt()

    ## return_stmt: (re_turn expr SEMI) | (re_turn SEMI);    
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()
    
    ## func_call_stmt: IDENTIFIER LB exprlist RB SEMI;
    def visitFunc_call_stmt(self, ctx: MT22Parser.Func_call_stmtContext):
        return CallStmt(ctx.IDENTIFIER().__str__(), self.visit(ctx.exprlist()))
    
    ## block_stmt: func_body;
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return self.visit(ctx.func_body())
    
    ## lhs: (IDENTIFIER index_operator) | (IDENTIFIER);
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.index_operator():
            return ArrayCell(ctx.IDENTIFIER().__str__(), self.visit(ctx.index_operator()))
        else:
            return Id(ctx.IDENTIFIER().__str__())
# ####6. Expression  

    ## exprlist: exprprime | ;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.exprprime():
            return self.visit(ctx.exprprime())
        else:
            return []
    
    ## exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())
        else:
            return [self.visit(ctx.expr())]
    
    ## expr: expr1 DOUBLE_COLON expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.DOUBLE_COLON():
            return BinExpr(ctx.DOUBLE_COLON().__str__(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1(0))
    
    ## expr1: expr1 (EQUAL | DIFF | LESS | LARGER | LESSE | LARGERE) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.expr1():
            oPeRator = ""
            if ctx.EQUAL():
                oPeRator = ctx.EQUAL().__str__()
            elif ctx.DIFF():
                oPeRator = ctx.DIFF().__str__()
            elif ctx.LESS():
                oPeRator = ctx.LESS().__str__()
            elif ctx.LARGER():
                oPeRator = ctx.LARGER().__str__()
            elif ctx.LESSE():
                oPeRator = ctx.LESSE().__str__()
            else:
                oPeRator = ctx.LARGERE().__str__()

            return BinExpr(oPeRator, self.visit(ctx.expr1()), self.visit(ctx.expr2()))
        else:
            return self.visit(ctx.expr2())
    
    ## expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.expr2():
            oPeRator = ""
            if ctx.AND():
                oPeRator = ctx.AND().__str__()
            else:
                oPeRator = ctx.OR().__str__()

            return BinExpr(oPeRator, self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())
    
    ## expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.expr3():
            oPeRator = ""
            if ctx.ADD():
                oPeRator = ctx.ADD().__str__()
            else:
                oPeRator = ctx.SUB().__str__()

            return BinExpr(oPeRator, self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())

   ## expr4: expr4 (MUL | DIV | MOD) expr5 | expr5; 
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.expr4():
            oPeRator = ""
            if ctx.MUL():
                oPeRator = ctx.MUL().__str__()
            elif ctx.DIV():
                oPeRator = ctx.DIV().__str__()
            else:
                oPeRator = ctx.MOD().__str__()
            return BinExpr(oPeRator, self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())
    
    ## expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.expr6():
            return self.visit(ctx.expr6())
        else:
            return UnExpr(ctx.NOT().__str__(), self.visit(ctx.expr5()))
    

    ## expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.expr7():
            return self.visit(ctx.expr7())
        else:
            return UnExpr(ctx.SUB().__str__(), self.visit(ctx.expr6()))
    
    ## expr7: IDENTIFIER index_operator | operands;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.IDENTIFIER():
            return ArrayCell(ctx.IDENTIFIER().__str__(), self.visit(ctx.index_operator()))
        else:
            return self.visit(ctx.operands())
    
    ## index_operator: LSB exprlist RSB;
    def visitIndex_operator(self, ctx: MT22Parser.Index_operatorContext):
        return self.visit(ctx.exprlist())
    
    ## operands: (LB expr RB) | BOOLEANLIT | IDENTIFIER | INTLIT | FLOATLIT | STRINGLIT | func_call | array_operand | arraylit;
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.BOOLEANLIT():
            if str(ctx.BOOLEANLIT()) == "true":
                return BooleanLit(True)
            else:
                return BooleanLit(False)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().__str__())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            x = ctx.FLOATLIT().getText()
            if x[0] == '.':
                x = '0' + x
            return FloatLit(float(x))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.array_operand():
            return self.visit(ctx.array_operand())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
    
    ## func_call: IDENTIFIER LB exprlist RB;
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        return FuncCall(ctx.IDENTIFIER().__str__(), self.visit(ctx.exprlist()))
    
    ## array_operand: IDENTIFIER index_operator;
    def visitArray_operand(self, ctx: MT22Parser.Array_operandContext):
        return ArrayCell(ctx.IDENTIFIER().__str__(), self.visit(ctx.index_operator()))
    
    ## arraylit: LP exprlist RP;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))
# ##Type

    ## typ: atomic_typ | array_typ | void_typ | auto_typ;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.atomic_typ():
            return self.visit(ctx.atomic_typ())
        elif ctx.array_typ():
            return self.visit(ctx.array_typ())
        elif ctx.void_typ():
            return self.visit(ctx.void_typ())
        elif ctx.auto_typ():
            return self.visit(ctx.auto_typ())

    ## atomic_typ: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomic_typ(self, ctx: MT22Parser.Atomic_typContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()

    ## array_typ: ARRAY LSB intlist RSB OF atomic_typ;   
    def visitArray_typ(self, ctx: MT22Parser.Array_typContext):
        return ArrayType(self.visit(ctx.intlist()), self.visit(ctx.atomic_typ()))

    ## void_typ: VOID;
    def visitVoid_typ(self, ctx: MT22Parser.Void_typContext):
        return VoidType()
    
    ## auto_typ: AUTO;
    def visitAuto_typ(self, ctx: MT22Parser.Auto_typContext):
        return AutoType()

    # intlist: INTLIT COMMA intlist | INTLIT;
    def visitIntlist(self, ctx: MT22Parser.IntlistContext):
        if ctx.intlist():
            return [int(ctx.INTLIT().__str__())] + self.visit(ctx.intlist())
        else:
            return [int(ctx.INTLIT().__str__())]
