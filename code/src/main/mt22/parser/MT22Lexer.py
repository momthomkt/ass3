# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u020f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\7\3\u009b\n\3\f\3\16")
        buf.write("\3\u009e\13\3\3\3\5\3\u00a1\n\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u0159\n\61\3\62\3\62\7\62\u015d\n\62")
        buf.write("\f\62\16\62\u0160\13\62\3\63\3\63\3\63\7\63\u0165\n\63")
        buf.write("\f\63\16\63\u0168\13\63\3\63\3\63\6\63\u016c\n\63\r\63")
        buf.write("\16\63\u016d\7\63\u0170\n\63\f\63\16\63\u0173\13\63\5")
        buf.write("\63\u0175\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u017e\n\64\3\64\3\64\3\64\3\64\3\64\5\64\u0185\n\64\3")
        buf.write("\64\3\64\3\65\3\65\3\65\7\65\u018c\n\65\f\65\16\65\u018f")
        buf.write("\13\65\3\65\3\65\6\65\u0193\n\65\r\65\16\65\u0194\7\65")
        buf.write("\u0197\n\65\f\65\16\65\u019a\13\65\5\65\u019c\n\65\3\66")
        buf.write("\3\66\7\66\u01a0\n\66\f\66\16\66\u01a3\13\66\3\67\3\67")
        buf.write("\5\67\u01a7\n\67\3\67\6\67\u01aa\n\67\r\67\16\67\u01ab")
        buf.write("\38\38\38\38\78\u01b2\n8\f8\168\u01b5\138\38\38\38\38")
        buf.write("\39\39\3:\3:\5:\u01bf\n:\3;\3;\3;\3<\3<\3<\3<\3<\5<\u01c9")
        buf.write("\n<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u01d6\n=\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\5>\u01e2\n>\3?\3?\3@\6@\u01e7")
        buf.write("\n@\r@\16@\u01e8\3@\3@\3A\3A\3A\3A\7A\u01f1\nA\fA\16A")
        buf.write("\u01f4\13A\3A\5A\u01f7\nA\3A\3A\3B\3B\3B\3B\7B\u01ff\n")
        buf.write("B\fB\16B\u0202\13B\3B\3B\3B\3B\3C\3C\3C\5C\u020b\nC\3")
        buf.write("D\3D\3D\4\u008f\u009c\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\2k\2m\2o\66q\2s\2u\2w\67y8{9}:\177;\u0081<\u0083")
        buf.write("=\u0085\2\u0087>\3\2\16\4\3\f\f\16\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17")
        buf.write("$$^^\t\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\4\3\f\f\17\17")
        buf.write("\n\2$$))^^ddhhppttvv\2\u0239\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2o\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2")
        buf.write("\2\5\u0097\3\2\2\2\7\u00a4\3\2\2\2\t\u00a9\3\2\2\2\13")
        buf.write("\u00af\3\2\2\2\r\u00b7\3\2\2\2\17\u00ba\3\2\2\2\21\u00bf")
        buf.write("\3\2\2\2\23\u00c5\3\2\2\2\25\u00c9\3\2\2\2\27\u00d2\3")
        buf.write("\2\2\2\31\u00d5\3\2\2\2\33\u00dd\3\2\2\2\35\u00e4\3\2")
        buf.write("\2\2\37\u00eb\3\2\2\2!\u00f1\3\2\2\2#\u00f6\3\2\2\2%\u00fa")
        buf.write("\3\2\2\2\'\u0103\3\2\2\2)\u0106\3\2\2\2+\u010e\3\2\2\2")
        buf.write("-\u0114\3\2\2\2/\u0116\3\2\2\2\61\u0118\3\2\2\2\63\u011a")
        buf.write("\3\2\2\2\65\u011c\3\2\2\2\67\u011e\3\2\2\29\u0120\3\2")
        buf.write("\2\2;\u0123\3\2\2\2=\u0126\3\2\2\2?\u0129\3\2\2\2A\u012c")
        buf.write("\3\2\2\2C\u012e\3\2\2\2E\u0131\3\2\2\2G\u0133\3\2\2\2")
        buf.write("I\u0136\3\2\2\2K\u0139\3\2\2\2M\u013b\3\2\2\2O\u013d\3")
        buf.write("\2\2\2Q\u013f\3\2\2\2S\u0141\3\2\2\2U\u0143\3\2\2\2W\u0145")
        buf.write("\3\2\2\2Y\u0147\3\2\2\2[\u0149\3\2\2\2]\u014b\3\2\2\2")
        buf.write("_\u014d\3\2\2\2a\u0158\3\2\2\2c\u015a\3\2\2\2e\u0174\3")
        buf.write("\2\2\2g\u0184\3\2\2\2i\u019b\3\2\2\2k\u019d\3\2\2\2m\u01a4")
        buf.write("\3\2\2\2o\u01ad\3\2\2\2q\u01ba\3\2\2\2s\u01be\3\2\2\2")
        buf.write("u\u01c0\3\2\2\2w\u01c8\3\2\2\2y\u01d5\3\2\2\2{\u01e1\3")
        buf.write("\2\2\2}\u01e3\3\2\2\2\177\u01e6\3\2\2\2\u0081\u01ec\3")
        buf.write("\2\2\2\u0083\u01fa\3\2\2\2\u0085\u020a\3\2\2\2\u0087\u020c")
        buf.write("\3\2\2\2\u0089\u008a\7\61\2\2\u008a\u008b\7,\2\2\u008b")
        buf.write("\u008f\3\2\2\2\u008c\u008e\13\2\2\2\u008d\u008c\3\2\2")
        buf.write("\2\u008e\u0091\3\2\2\2\u008f\u0090\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092")
        buf.write("\u0093\7,\2\2\u0093\u0094\7\61\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u0096\b\2\2\2\u0096\4\3\2\2\2\u0097\u0098\7\61")
        buf.write("\2\2\u0098\u009c\7\61\2\2\u0099\u009b\13\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009d\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a1\t\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\u00a3\b\3\2\2\u00a3\6\3\2\2\2\u00a4\u00a5")
        buf.write("\7c\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7m\2\2\u00ae\n\3\2\2\2\u00af\u00b0\7d\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7p\2\2\u00b6\f")
        buf.write("\3\2\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9\7q\2\2\u00b9\16")
        buf.write("\3\2\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7g\2\2\u00be\20\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\22\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7t\2\2\u00c8\24")
        buf.write("\3\2\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\26")
        buf.write("\3\2\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7h\2\2\u00d4\30")
        buf.write("\3\2\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7v\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7i\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7t\2\2\u00dc\32\3\2\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1")
        buf.write("\7w\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7p\2\2\u00e3\34")
        buf.write("\3\2\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7i\2\2\u00ea\36\3\2\2\2\u00eb\u00ec\7y\2\2\u00ec\u00ed")
        buf.write("\7j\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0 \3\2\2\2\u00f1\u00f2\7x\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7f\2\2\u00f5\"")
        buf.write("\3\2\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9$\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102&\3\2\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105(\3\2\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7j\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b\u010c\7k\2\2\u010c\u010d\7v\2\2\u010d*\3")
        buf.write("\2\2\2\u010e\u010f\7c\2\2\u010f\u0110\7t\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7c\2\2\u0112\u0113\7{\2\2\u0113,\3")
        buf.write("\2\2\2\u0114\u0115\7-\2\2\u0115.\3\2\2\2\u0116\u0117\7")
        buf.write("/\2\2\u0117\60\3\2\2\2\u0118\u0119\7,\2\2\u0119\62\3\2")
        buf.write("\2\2\u011a\u011b\7\61\2\2\u011b\64\3\2\2\2\u011c\u011d")
        buf.write("\7\'\2\2\u011d\66\3\2\2\2\u011e\u011f\7#\2\2\u011f8\3")
        buf.write("\2\2\2\u0120\u0121\7(\2\2\u0121\u0122\7(\2\2\u0122:\3")
        buf.write("\2\2\2\u0123\u0124\7~\2\2\u0124\u0125\7~\2\2\u0125<\3")
        buf.write("\2\2\2\u0126\u0127\7?\2\2\u0127\u0128\7?\2\2\u0128>\3")
        buf.write("\2\2\2\u0129\u012a\7#\2\2\u012a\u012b\7?\2\2\u012b@\3")
        buf.write("\2\2\2\u012c\u012d\7>\2\2\u012dB\3\2\2\2\u012e\u012f\7")
        buf.write(">\2\2\u012f\u0130\7?\2\2\u0130D\3\2\2\2\u0131\u0132\7")
        buf.write("@\2\2\u0132F\3\2\2\2\u0133\u0134\7@\2\2\u0134\u0135\7")
        buf.write("?\2\2\u0135H\3\2\2\2\u0136\u0137\7<\2\2\u0137\u0138\7")
        buf.write("<\2\2\u0138J\3\2\2\2\u0139\u013a\7*\2\2\u013aL\3\2\2\2")
        buf.write("\u013b\u013c\7+\2\2\u013cN\3\2\2\2\u013d\u013e\7]\2\2")
        buf.write("\u013eP\3\2\2\2\u013f\u0140\7_\2\2\u0140R\3\2\2\2\u0141")
        buf.write("\u0142\7\60\2\2\u0142T\3\2\2\2\u0143\u0144\7.\2\2\u0144")
        buf.write("V\3\2\2\2\u0145\u0146\7=\2\2\u0146X\3\2\2\2\u0147\u0148")
        buf.write("\7<\2\2\u0148Z\3\2\2\2\u0149\u014a\7}\2\2\u014a\\\3\2")
        buf.write("\2\2\u014b\u014c\7\177\2\2\u014c^\3\2\2\2\u014d\u014e")
        buf.write("\7?\2\2\u014e`\3\2\2\2\u014f\u0150\7v\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151\u0152\7w\2\2\u0152\u0159\7g\2\2\u0153\u0154")
        buf.write("\7h\2\2\u0154\u0155\7c\2\2\u0155\u0156\7n\2\2\u0156\u0157")
        buf.write("\7u\2\2\u0157\u0159\7g\2\2\u0158\u014f\3\2\2\2\u0158\u0153")
        buf.write("\3\2\2\2\u0159b\3\2\2\2\u015a\u015e\t\3\2\2\u015b\u015d")
        buf.write("\t\4\2\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015fd\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0161\u0175\7\62\2\2\u0162\u0166\t\5\2")
        buf.write("\2\u0163\u0165\t\6\2\2\u0164\u0163\3\2\2\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0171\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016b\7a\2\2")
        buf.write("\u016a\u016c\t\6\2\2\u016b\u016a\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170")
        buf.write("\3\2\2\2\u016f\u0169\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0174\u0161\3\2\2\2\u0174\u0162\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b\63\3\2\u0177")
        buf.write("f\3\2\2\2\u0178\u0179\5i\65\2\u0179\u017a\5k\66\2\u017a")
        buf.write("\u0185\3\2\2\2\u017b\u017d\5i\65\2\u017c\u017e\5k\66\2")
        buf.write("\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u0180\5m\67\2\u0180\u0185\3\2\2\2\u0181\u0182")
        buf.write("\5k\66\2\u0182\u0183\5m\67\2\u0183\u0185\3\2\2\2\u0184")
        buf.write("\u0178\3\2\2\2\u0184\u017b\3\2\2\2\u0184\u0181\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0187\b\64\4\2\u0187h\3\2\2")
        buf.write("\2\u0188\u019c\7\62\2\2\u0189\u018d\t\5\2\2\u018a\u018c")
        buf.write("\t\6\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0198\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u0190\u0192\7a\2\2\u0191\u0193\t")
        buf.write("\6\2\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196")
        buf.write("\u0190\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019b\u0188\3\2\2\2\u019b\u0189\3\2\2\2\u019cj")
        buf.write("\3\2\2\2\u019d\u01a1\5S*\2\u019e\u01a0\t\6\2\2\u019f\u019e")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2l\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4")
        buf.write("\u01a6\t\7\2\2\u01a5\u01a7\t\b\2\2\u01a6\u01a5\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01aa\t")
        buf.write("\6\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01acn\3\2\2\2\u01ad\u01b3")
        buf.write("\5q9\2\u01ae\u01b2\5s:\2\u01af\u01b0\7^\2\2\u01b0\u01b2")
        buf.write("\5q9\2\u01b1\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\5q9\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01b9\b8\5\2\u01b9p\3\2\2\2\u01ba")
        buf.write("\u01bb\7$\2\2\u01bbr\3\2\2\2\u01bc\u01bf\n\t\2\2\u01bd")
        buf.write("\u01bf\5u;\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("t\3\2\2\2\u01c0\u01c1\7^\2\2\u01c1\u01c2\t\n\2\2\u01c2")
        buf.write("v\3\2\2\2\u01c3\u01c9\5\67\34\2\u01c4\u01c9\59\35\2\u01c5")
        buf.write("\u01c9\5;\36\2\u01c6\u01c9\5=\37\2\u01c7\u01c9\5? \2\u01c8")
        buf.write("\u01c3\3\2\2\2\u01c8\u01c4\3\2\2\2\u01c8\u01c5\3\2\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9x\3\2\2")
        buf.write("\2\u01ca\u01d6\5-\27\2\u01cb\u01d6\5/\30\2\u01cc\u01d6")
        buf.write("\5\61\31\2\u01cd\u01d6\5\63\32\2\u01ce\u01d6\5\65\33\2")
        buf.write("\u01cf\u01d6\5=\37\2\u01d0\u01d6\5? \2\u01d1\u01d6\5E")
        buf.write("#\2\u01d2\u01d6\5G$\2\u01d3\u01d6\5A!\2\u01d4\u01d6\5")
        buf.write("C\"\2\u01d5\u01ca\3\2\2\2\u01d5\u01cb\3\2\2\2\u01d5\u01cc")
        buf.write("\3\2\2\2\u01d5\u01cd\3\2\2\2\u01d5\u01ce\3\2\2\2\u01d5")
        buf.write("\u01cf\3\2\2\2\u01d5\u01d0\3\2\2\2\u01d5\u01d1\3\2\2\2")
        buf.write("\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d4\3")
        buf.write("\2\2\2\u01d6z\3\2\2\2\u01d7\u01e2\5-\27\2\u01d8\u01e2")
        buf.write("\5/\30\2\u01d9\u01e2\5\61\31\2\u01da\u01e2\5\63\32\2\u01db")
        buf.write("\u01e2\5=\37\2\u01dc\u01e2\5? \2\u01dd\u01e2\5E#\2\u01de")
        buf.write("\u01e2\5G$\2\u01df\u01e2\5A!\2\u01e0\u01e2\5C\"\2\u01e1")
        buf.write("\u01d7\3\2\2\2\u01e1\u01d8\3\2\2\2\u01e1\u01d9\3\2\2\2")
        buf.write("\u01e1\u01da\3\2\2\2\u01e1\u01db\3\2\2\2\u01e1\u01dc\3")
        buf.write("\2\2\2\u01e1\u01dd\3\2\2\2\u01e1\u01de\3\2\2\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2|\3\2\2\2\u01e3\u01e4")
        buf.write("\5I%\2\u01e4~\3\2\2\2\u01e5\u01e7\t\13\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\b@\2\2")
        buf.write("\u01eb\u0080\3\2\2\2\u01ec\u01f2\5q9\2\u01ed\u01f1\5s")
        buf.write(":\2\u01ee\u01ef\7^\2\2\u01ef\u01f1\5q9\2\u01f0\u01ed\3")
        buf.write("\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f5\u01f7\t\f\2\2\u01f6\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01f9\bA\6\2\u01f9\u0082\3")
        buf.write("\2\2\2\u01fa\u0200\5q9\2\u01fb\u01ff\5s:\2\u01fc\u01fd")
        buf.write("\7^\2\2\u01fd\u01ff\5q9\2\u01fe\u01fb\3\2\2\2\u01fe\u01fc")
        buf.write("\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0203\u0204\5\u0085C\2\u0204\u0205\3\2\2\2\u0205\u0206")
        buf.write("\bB\7\2\u0206\u0084\3\2\2\2\u0207\u0208\7^\2\2\u0208\u020b")
        buf.write("\n\r\2\2\u0209\u020b\7^\2\2\u020a\u0207\3\2\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020b\u0086\3\2\2\2\u020c\u020d\13\2\2")
        buf.write("\2\u020d\u020e\bD\b\2\u020e\u0088\3\2\2\2\"\2\u008f\u009c")
        buf.write("\u00a0\u0158\u015e\u0166\u016d\u0171\u0174\u017d\u0184")
        buf.write("\u018d\u0194\u0198\u019b\u01a1\u01a6\u01ab\u01b1\u01b3")
        buf.write("\u01be\u01c8\u01d5\u01e1\u01e8\u01f0\u01f2\u01f6\u01fe")
        buf.write("\u0200\u020a\t\b\2\2\3\63\2\3\64\3\38\4\3A\5\3B\6\3D\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    C_CMT = 1
    Cpp_CMT = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FLOAT = 8
    FOR = 9
    FUNCTION = 10
    IF = 11
    INTEGER = 12
    RTURN = 13
    STRING = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    DIFF = 31
    LESS = 32
    LESSE = 33
    LARGER = 34
    LARGERE = 35
    DOUBLE_COLON = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    DOTS = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    LP = 45
    RP = 46
    ASSIGN = 47
    BOOLEANLIT = 48
    IDENTIFIER = 49
    INTLIT = 50
    FLOATLIT = 51
    STRINGLIT = 52
    BOOLEAN_OP = 53
    INT_OP = 54
    FLOAT_OP = 55
    STRING_OP = 56
    WS = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_TOKEN = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "C_CMT", "Cpp_CMT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
            "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RTURN", "STRING", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "DIFF", "LESS", "LESSE", "LARGER", "LARGERE", "DOUBLE_COLON", 
            "LB", "RB", "LSB", "RSB", "DOTS", "COMMA", "SEMI", "COLON", 
            "LP", "RP", "ASSIGN", "BOOLEANLIT", "IDENTIFIER", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "BOOLEAN_OP", "INT_OP", "FLOAT_OP", 
            "STRING_OP", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "C_CMT", "Cpp_CMT", "AUTO", "BREAK", "BOOLEAN", "DO", 
                  "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RTURN", 
                  "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "DIFF", "LESS", "LESSE", "LARGER", "LARGERE", 
                  "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", "DOTS", "COMMA", 
                  "SEMI", "COLON", "LP", "RP", "ASSIGN", "BOOLEANLIT", "IDENTIFIER", 
                  "INTLIT", "FLOATLIT", "INTPART", "DECPART", "EXPPART", 
                  "STRINGLIT", "DoubleQ", "CHAR_SET", "ESC_SEQ", "BOOLEAN_OP", 
                  "INT_OP", "FLOAT_OP", "STRING_OP", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "ERROR_TOKEN" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INTLIT_action 
            actions[50] = self.FLOATLIT_action 
            actions[54] = self.STRINGLIT_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            z = self.text
            if z[-1] in ['\r', '\n', '\f']:
            	raise UncloseString(z[1:-1])
            else:
                raise UncloseString(z[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


