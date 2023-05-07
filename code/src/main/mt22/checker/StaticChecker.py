from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

def check2Type(a, b):
        if type(a) is not type(b):
            return False
        else:
            if type(a) is ArrayType:
                if len(a.dimensions) != len(b.dimensions) or type(a.typ) is not type(b.typ):
                    return False
                for i in range(len(a.dimensions)):
                    if a.dimensions[i] != b.dimensions[i]:
                        return False
                return True
            else:
                ############
                return True

def setType(ctx, typ, o):
        if type(ctx) is Id:
            for i in range(len(o)-1):
                for ele in o[i]:
                    if type(ele) is VarDecl or type(ele) is ParamDecl:
                        if ctx.name == ele.name:
                            ele.typ = typ
                            break
        elif type(ctx) is FuncCall:
            for ele in o[-1]:
                if type(ele) is FuncDecl:
                    if ctx.name == ele.name:
                        ele.return_type = typ
                        break

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def infer(id, type, o):
        for env in o:
            if id.name in env:
                env[id.name] = type
                return type

    def intersection(lst1, lst2): 
        lst3 = [value for value in lst1 if value in lst2] 
        return lst3
    # def visitProgram(self,ctx: Program,o):
    #     raise NoEntryPoint("alo")
    # def visitFuncDecl(self,ctx: FuncDecl,o):
    #     raise NoEntryPoint("alo")
    def visitIntegerType(self, ctx, o):
        return IntegerType()
    def visitFloatType(self, ctx, o):
        return FloatType()
    def visitBooleanType(self, ctx, o):
        return BooleanType()
    def visitStringType(self, ctx, o):
        return StringType()
    def visitArrayType(self, ctx, o):
        return ctx
    def visitAutoType(self, ctx, o):
        return AutoType()
    def visitVoidType(self, ctx, o):
        return VoidType()
#####################################
    def setType(ctx, typ, o):
        if type(ctx) is Id:
            for i in range(len(o)-1):
                for ele in o[i]:
                    if type(ele) is VarDecl:
                        if ctx.name == ele.name:
                            ele.typ = typ
                            break
        elif type(ctx) is FuncCall:
            for ele in o[-1]:
                if type(ele) is FuncDecl:
                    if ctx.name == ele.name:
                        ele.return_type = typ
                        break
#####################################
    def visitBinExpr(self, ctx, o):
        l = self.visit(ctx.left, o)
        r = self.visit(ctx.right, o)
        op = ctx.op
        if op in ['+','-','*','/']:
            if type(l) is not AutoType and type(r) is not AutoType:
                if (type(l) is not IntegerType and type(l) is not FloatType) or (type(r) is not IntegerType and type(r) is not FloatType):
                    raise TypeMismatchInExpression(ctx)
                elif type(l) is FloatType or type(r) is FloatType:
                    return FloatType()
                else:
                    return IntegerType()
            else:
                if type(l) is type(r):
                    return AutoType()
                else:
                    if type(l) is AutoType:
                        if type(r) is not IntegerType and type(r) is not FloatType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.left, r, o)
                            return r
                    else:
                        if type(l) is not IntegerType and type(l) is not FloatType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.right, l, o)
                            return l
        elif op in ['>','>=','<','<=']:
            if type(l) is not AutoType and type(r) is not AutoType:
                if (type(l) is not IntegerType and type(l) is not FloatType) or (type(r) is not IntegerType and type(r) is not FloatType):
                    raise TypeMismatchInExpression(ctx)
                else:
                    return BooleanType()
            else:
                if type(l) is type(r):
                    return BooleanType()
                else:
                    if type(l) is AutoType:
                        if type(r) is not IntegerType and type(r) is not FloatType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.left, r, o)
                            return BooleanType()
                    else:
                        if type(l) is not IntegerType and type(l) is not FloatType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.right, l, o)
                            return BooleanType()
        elif op in ['!=','==']:
            if type(l) is not AutoType and type(r) is not AutoType:
                if (type(l) is not IntegerType and type(l) is not BooleanType) or (type(r) is not IntegerType and type(r) is not BooleanType):
                    raise TypeMismatchInExpression(ctx)
                else:
                    return BooleanType()
            else:
                if type(l) is type(r):
                    return BooleanType()
                else:
                    if type(l) is AutoType:
                        if type(r) is not IntegerType and type(r) is not BooleanType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.left, r, o)
                            return BooleanType()
                    else:
                        if type(l) is not IntegerType and type(l) is not BooleanType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.right, l, o)
                            return BooleanType()
                        
        elif op in ['&&','||']:
            if type(l) is not AutoType and type(r) is not AutoType:
                if type(l) is not BooleanType or type(r) is not BooleanType:
                    raise TypeMismatchInExpression(ctx)
                else:
                    return BooleanType()
            else:
                if type(l) is type(r):
                    return BooleanType()
                else:
                    if type(l) is AutoType:
                        if type(r) is not BooleanType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.left, r, o)
                            return BooleanType()
                    else:
                        if type(l) is not BooleanType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.right, l, o)
                            return BooleanType()
        elif op == '%':
            if type(l) is not AutoType and type(r) is not AutoType:
                if type(l) is not IntegerType or type(r) is not IntegerType:
                    raise TypeMismatchInExpression(ctx)
                else:
                    return IntegerType()
            else:
                if type(l) is type(r):
                    return IntegerType()
                else:
                    if type(l) is AutoType:
                        if type(r) is not IntegerType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.left, r, o)
                            return IntegerType()
                    else:
                        if type(l) is not IntegerType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.right, l, o)
                            return IntegerType()
        elif op == '::':
            if type(l) is not AutoType and type(r) is not AutoType:
                if type(l) is not StringType or type(r) is not StringType:
                    raise TypeMismatchInExpression(ctx)
                else:
                    return StringType()
            else:
                if type(l) is type(r):
                    return StringType()
                else:
                    if type(l) is AutoType:
                        if type(r) is not StringType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.left, r, o)
                            return StringType()
                    else:
                        if type(l) is not StringType:
                            raise TypeMismatchInExpression(ctx)
                        else:
                            setType(ctx.right, l, o)
                            return StringType()

                
    def visitUnExpr(self, ctx, o):
        op = ctx.op
        val_typ = self.visit(ctx.val, o)
        if op == '!':
            if type(val_typ) is BooleanType or type(val_typ) is AutoType:
                if type(val_typ) is AutoType:
                    setType(ctx.val, BooleanType(), o)
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ctx)
        else:
            if type(val_typ) is not IntegerType and type(val_typ) is not FloatType and type(val_typ) is not AutoType :
                raise TypeMismatchInExpression(ctx)
            else:
                if type(val_typ) is AutoType:
                    setType(ctx.val, IntegerType(), o)
                    return IntegerType()
                return val_typ


    def visitId(self, ctx, o):
        name = ctx.name
        typ = ""
        for i in range(len(o)-1):
            for ele in o[i]:
                if type(ele) is VarDecl or type(ele) is ParamDecl:
                    if name == ele.name:
                        return ele.typ
        raise Undeclared(Identifier(), name)
    def visitArrayCell(self, ctx, o):
        for i in range(len(o)-1):
            for ele in o[i]:
                if (type(ele) is VarDecl or type(ele) is ParamDecl) and type(ele.typ) is ArrayType:
                    if ctx.name == ele.name:
                        if len(ele.typ.dimensions) < len(ctx.cell):
                            raise TypeMismatchInExpression(ctx)
                        else:
                            dimension = ele.typ.dimensions.copy()
                            for expr in ctx.cell:
                                typ_val = self.visit(expr, o)
                                if type(typ_val) is not IntegerType:
                                    raise TypeMismatchInExpression(ctx)
                                dimension.pop(0)
                            typ = ele.typ.typ
                            if len(dimension) == 0:
                                return typ
                            else:
                                return ArrayType(dimension, typ)
        raise Undeclared(Identifier(),ctx.name)

    def visitIntegerLit(self, ctx, o):
        return IntegerType()
    def visitFloatLit(self, ctx, o):
        return FloatType()
    def visitStringLit(self, ctx, o):
        return StringType()
    def visitBooleanLit(self, ctx, o):
        return BooleanType()
##########################################
    def check2Type(a, b):
        if type(a) is not type(b):
            return False
        else:
            if type(a) is ArrayType:
                if len(a.dimensions) != len(b.dimensions) or type(a.typ) is not type(b.typ):
                    return False
                for i in range(len(a.dimensions)):
                    if a.dimensions[i] != b.dimensions[i]:
                        return False
                return True
            else:
                return False
############################################
    def visitArrayLit(self, ctx, o):
        flag = True
        preTyp = self.visit(ctx.explist[0], o)
        for expr in ctx.explist:
            currTyp = self.visit(expr, o)
            if not check2Type(preTyp, currTyp):
                raise IllegalArrayLiteral(ctx)
        typ = None
        dimension = []
        if type(preTyp) is ArrayType:
            typ = preTyp.typ
            dimension = dimension + preTyp.dimensions.copy()
        else:
            typ = preTyp
        dimension.insert(0,len(ctx.explist))
        return ArrayType(dimension, typ)
    def visitFuncCall(self, ctx, o):
        exist = False
        currFunc = None
        for decl in o[-1]:
            if ctx.name == decl.name and type(decl) is FuncDecl:
                if type(decl.return_type) is VoidType:
                    raise TypeMismatchInExpression(ctx)
                else:
                    exist = True
                    currFunc = decl
                    break
        if not exist:
            raise Undeclared(Function(),ctx.name)
        if currFunc.name != 'super':
            if len(currFunc.params) != len(ctx.args):
                raise TypeMismatchInExpression(ctx)
            
            for i in range(len(currFunc.params)):
                typ_left = currFunc.params[i].typ
                typ_right = self.visit(ctx.args[i], o)

                if type(typ_left) is VoidType or type(typ_left) is ArrayType or type(typ_right) is VoidType or type(typ_right) is ArrayType:
                    raise TypeMismatchInExpression(ctx)

                if not check2Type(typ_left, typ_right):
                    if type(typ_left) is FloatType and type(typ_right) is IntegerType:
                            pass
                    elif type(typ_left) is AutoType:
                        currFunc.params[i].typ = typ_right
                    elif type(typ_right) is AutoType:
                        setType(ctx.args[i], typ_left, o)
                    # elif type(typ_left) is ArrayType and type(typ_right) is ArrayType:
                    #     if type(typ_left.typ) is FloatType and type(typ_right.typ) is IntegerType and typ_left.dimensions == typ_right.dimensions:
                    #         ####
                    #         pass
                    #     else:
                    #         raise TypeMismatchInExpression(ctx)
                    else:
                        raise TypeMismatchInExpression(ctx)
            return currFunc.return_type
        else:
            pass

    def visitAssignStmt(self, ctx, o):
        typ_lhs = self.visit(ctx.lhs, o)
        typ_rhs = self.visit(ctx.rhs, o)

        if not check2Type(typ_lhs, typ_rhs):
            if type(typ_lhs) is FloatType and type(typ_rhs) is IntegerType:
                pass
            elif type(typ_lhs) is AutoType:
                setType(ctx.lhs, typ_rhs, o)
            elif type(typ_rhs) is AutoType:
                setType(ctx.lhs, typ_rhs, o)
            # elif type(typ_lhs) is ArrayType and type(typ_rhs) is ArrayType and typ_lhs.dimensions == typ_rhs.dimensions:
            #     if type(typ_lhs.typ) is FloatType and type(typ_rhs.typ) is IntegerType:
            #         pass
            #     else:
            #         raise TypeMismatchInStatement(ctx)
            else:
                raise TypeMismatchInStatement(ctx)
    def visitBlockStmt(self, ctx, o):
        visit = False
        for ele in ctx.body:
            if type(ele) is BlockStmt:
                o.insert(0,[])
            if type(ele) is ReturnStmt:
                if visit == False:
                    visit = True
                    self.visit(ele, o)
            else:
                self.visit(ele, o)
        o.pop(0)
    def visitIfStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.tstmt) is BlockStmt:
            o.insert(0,[])
        self.visit(ctx.tstmt, o)

        if ctx.fstmt:
            if type(ctx.fstmt) is BlockStmt:
                o.insert(0,[])
            self.visit(ctx.fstmt, o)
    def visitForStmt(self, ctx, o):
        self.visit(ctx.init, o)
        init_typ = self.visit(ctx.init.lhs,o)
        initvalue_typ = self.visit(ctx.init.rhs,o)
        if type(init_typ) is not IntegerType or type(initvalue_typ) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        upd_typ = self.visit(ctx.upd, o)
        if type(upd_typ) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        o[0].append(ctx)
        o.insert(0,[])
        self.visit(ctx.stmt, o)
        if type(ctx.stmt) is not BlockStmt:
            o.pop(0)
        
    def visitWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        o[0].append(ctx)
        o.insert(0,[])
        self.visit(ctx.stmt, o)
        if type(ctx.stmt) is not BlockStmt:
            o.pop(0)

    def visitDoWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        o[0].append(ctx)
        o.insert(0,[])
        self.visit(ctx.stmt, o)
        if type(ctx.stmt) is not BlockStmt:
            o.pop(0)

    def visitBreakStmt(self, ctx, o):
        flag = False
        for i in range(1, len(o)-2):
            if type(o[i][-1]) is ForStmt or type(o[i][-1]) is WhileStmt or type(o[i][-1]) is DoWhileStmt:
                flag = True
        if not flag:
            raise MustInLoop(ctx)

    def visitContinueStmt(self, ctx, o):
        flag = False
        for i in range(1, len(o)-2):
            if type(o[i][-1]) is ForStmt or type(o[i][-1]) is WhileStmt or type(o[i][-1]) is DoWhileStmt:
                flag = True
        if not flag:
            raise MustInLoop(ctx)
        
    def visitReturnStmt(self, ctx, o):
        currFunc = o[-2][-1]
        typ = None
        if ctx.expr:
            typ = self.visit(ctx.expr, o)
        else:
            typ = VoidType()
        if not check2Type(currFunc.return_type, typ):

            if type(currFunc.return_type) is FloatType and type(typ) is IntegerType:
                pass
            elif type(currFunc.return_type) is AutoType:
                currFunc.return_type = typ
            elif type(typ) is AutoType:
                setType(ctx.expr, currFunc.return_type, o)
            elif type(currFunc.return_type) is ArrayType and type(typ) is ArrayType:
                if type(currFunc.return_type.typ) is FloatType and type(typ.typ) is IntegerType and currFunc.return_type.dimensions == typ.dimensions:
                    pass
                else:
                    raise TypeMismatchInStatement(ctx)
            else:
                raise TypeMismatchInStatement(ctx)
        else:
            pass

    def visitCallStmt(self, ctx, o):
        exist = False
        currFunc = None
        for decl in o[-1]:
            if ctx.name == decl.name and type(decl) is FuncDecl:
                exist = True
                currFunc = decl
                break
        if not exist:
            raise Undeclared(Function(),ctx.name)
        if currFunc.name != 'super':
            if len(currFunc.params) != len(ctx.args):
                raise TypeMismatchInStatement(ctx)
            for i in range(len(currFunc.params)):
                typ_left = currFunc.params[i].typ
                typ_right = self.visit(ctx.args[i], o)
                if type(typ_left) is VoidType or type(typ_left) is ArrayType or type(typ_right) is VoidType or type(typ_right) is ArrayType:
                    raise TypeMismatchInStatement(ctx)
                if not check2Type(typ_left, typ_right):
                    if type(typ_left) is FloatType and type(typ_right) is IntegerType:
                            pass
                    elif type(typ_left) is AutoType:
                        currFunc.params[i].typ = typ_right
                    elif type(typ_right) is AutoType:
                        setType(ctx.args[i], typ_left, o)
                    # elif type(typ_left) is ArrayType and type(typ_right) is ArrayType:
                    #     if type(typ_left.typ) is FloatType and type(typ_right.typ) is IntegerType and typ_left.dimensions == typ_right.dimensions:
                    #         pass
                    #     else:
                    #         raise TypeMismatchInStatement(ctx)
                    else:
                        raise TypeMismatchInStatement(ctx)
        else:
            if o[-2][-1].inherit:
                currFunc = o[-2][-1]
                exist = False
                parentFunc = None
                for decl in o[-1]:
                    if currFunc.inherit == decl.name and type(decl) is FuncDecl:
                        exist = True
                        parentFunc = decl
                if not exist:
                    raise Undeclared(Function(),currFunc.inherit)
                if len(parentFunc.params) > len(ctx.args):
                    raise TypeMismatchInExpression()
                elif len(parentFunc.params) < len(ctx.args):
                    raise TypeMismatchInExpression(ctx.args[len(parentFunc.params)])
                else:
                    for i in range(len(parentFunc.params)):
                        typ_left = parentFunc.params[i].typ
                        typ_right = self.visit(ctx.args[i], o)

                        if type(typ_left) is VoidType or type(typ_left) is ArrayType or type(typ_right) is VoidType or type(typ_right) is ArrayType:
                            raise TypeMismatchInExpression(ctx.args[i])
                        if not check2Type(typ_left, typ_right):
                            if type(typ_left) is FloatType and type(typ_right) is IntegerType:
                                    pass
                            elif type(typ_left) is AutoType:
                                parentFunc.params[i].typ = typ_right
                            elif type(typ_right) is AutoType:
                                setType(ctx.args[i], typ_left, o)
                            else:
                                raise TypeMismatchInExpression(ctx.args[i])
            else:
                raise TypeMismatchInStatement(ctx)
    def visitVarDecl(self, ctx, o):
        name = ctx.name
        for ele in o[0]:
            if type(ele) is VarDecl or type(ele) is FuncDecl or type(ele) is ParamDecl:
                if ctx.name == ele.name:
                    raise Redeclared(Variable(),name)
        declTyp = self.visit(ctx.typ,o)
        if ctx.init:
            initTyp = self.visit(ctx.init,o)
            if not check2Type(declTyp,initTyp):
                if type(declTyp) is AutoType:
                    ctx.typ = initTyp
                elif type(declTyp) is FloatType and type(initTyp) is IntegerType:
                    pass
                elif type(declTyp) is ArrayType and type(initTyp) is ArrayType and declTyp.dimensions == initTyp.dimensions:
                    if type(declTyp.typ) is FloatType and type(initTyp.typ) is IntegerType:
                        pass
                    else:
                        raise TypeMismatchInVarDecl(ctx)
                elif type(initTyp) is AutoType:
                    setType(ctx.init, declTyp, o)
                else:
                    raise TypeMismatchInVarDecl(ctx)
        else:
            if type(declTyp) is AutoType:
                raise Invalid(Variable(), name)   
        o[0] = o[0] + [ctx]
            
    def visitParamDecl(self, ctx, o):
        for decl in o[0]:
            if ctx.name == decl.name:
                raise Invalid(Parameter(),ctx.name)
        o[0].append(ctx)
        
    def visitFuncDecl(self, ctx, o):
        name = ctx.name
        for ele in o[0]:
            if name == ele.name:
                raise Redeclared(Function(),name)
        o[0] = o[0] + [ctx]
        o.insert(0,[])
        if ctx.inherit:
            flag = False
            funcInher = None
            for decl in o[-1]:
                if ctx.inherit == decl.name and type(decl) is FuncDecl:
                    flag = True
                    funcInher = decl
            if not flag :
                raise Undeclared(Function(), ctx.inherit)
            
            if len(funcInher.params) == 0:
                if len(ctx.body.body) > 0:
                    
                    firsStmt = ctx.body.body[0]
                    for line in ctx.body.body:
                        if type(line) is Stmt:
                            firsStmt = line 


                    if type(firsStmt) is CallStmt:
                        if firsStmt.name == 'preventDefault' and len(firsStmt.args) == 0:
                            pass
                        else:
                            pass
                            # for param in funcInher.params:
                            #     if param.inherit:
                            #         o[0] = o[0] + [param]
                    else:
                        pass
                        # for param in funcInher.params:
                        #         if param.inherit:
                        #             o[0] = o[0] + [param]

                else:
                    pass
                    # for param in funcInher.params:
                    #     if param.inherit:
                    #         o[0] = o[0] + [param]
            else:
                if len(ctx.body.body) > 0:
                    firsStmt = ctx.body.body[0]
                    for line in ctx.body.body:
                        if type(line) is Stmt:
                            firsStmt = line
                    if type(firsStmt) is CallStmt:
                        if firsStmt.name == 'preventDefault' and len(firsStmt.args) == 0:
                            pass
                        elif firsStmt.name == 'super':
                            for param in funcInher.params:
                                if param.inherit:
                                    o[0] = o[0] + [param]
                        else:
                            raise InvalidStatementInFunction(name)
                    else:
                        raise InvalidStatementInFunction(name)
                else:
                    raise InvalidStatementInFunction(name)
        for param in ctx.params:
            self.visit(param, o)
        self.visit(ctx.body, o)
        # o.pop(0)
    def visitProgram(self, ctx, o):
        init = [FuncDecl('readInteger',VoidType(),[],None,BlockStmt([])),
                FuncDecl('printInteger',VoidType(),[ParamDecl('anArg',IntegerType(),False,False)],None,BlockStmt([])),
                FuncDecl('readFloat',VoidType(),[],None,BlockStmt([])),
                FuncDecl('writeFloat',VoidType(),[ParamDecl('anArg',FloatType(),False,False)],None,BlockStmt([])),
                FuncDecl('readBoolean',VoidType(),[],None,BlockStmt([])),
                FuncDecl('printBoolean',VoidType(),[ParamDecl('anArg',BooleanType(),False,False)],None,BlockStmt([])),
                FuncDecl('readString',VoidType(),[],None,BlockStmt([])),
                FuncDecl('printString',VoidType(),[ParamDecl('anArg',StringType(),False,False)],None,BlockStmt([])),
                FuncDecl('super',VoidType(),[],None,BlockStmt([])),
                FuncDecl('preventDefault',VoidType(),[],None,BlockStmt([]))]
        o = [[],init]
        entryPoint = False
        for decl in ctx.decls:
            if type(decl) is FuncDecl:
                if decl.name == "main" and type(decl.return_type) is VoidType and len(decl.params) == 0:
                    entryPoint = True
                lenParams = len(decl.params)
                for i in range(lenParams):
                    for j in range(i+1, lenParams):
                        if decl.params[i].name == decl.params[j].name:
                            raise Redeclared(Parameter(),decl.params[j].name)
            o[-1] = o[-1] + [decl]

        for decl in ctx.decls:
            self.visit(decl, o)
            if type(decl) is FuncDecl: pass
                # o.pop(0)
        if entryPoint == False:
            raise NoEntryPoint()