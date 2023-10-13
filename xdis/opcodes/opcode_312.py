"""
CPython 3.12 bytecode opcodes

This is like Python 3.12's opcode.py  with some classification
of stack usage and information for formatting instructions.
"""

import xdis.opcodes.opcode_311 as opcode_311
from xdis.opcodes.opcode_311 import opcode_arg_fmt311, opcode_extended_fmt311
from xdis.opcodes.base import (
    binary_op,
    def_op,
    finalize_opcodes,
    init_opdata,
    jrel_op,
    rm_op,
    update_pj3,
)

version_tuple = (3, 12)
python_implementation = "CPython"

loc = locals()

init_opdata(loc, opcode_311, version_tuple)


# extend opcodes to cover psuedo ops
loc["opname"].extend([f"<{i}>" for i in range(256, 267)])
loc["oppop"].extend([0] * 11)
loc["oppush"].extend([0] * 11)

# fmt: off
## These are removed / replaced since 3.11...
#           OP NAME                      OPCODE
#----------------------------------------------
rm_op(loc, "UNARY_POSITIVE"               , 10)
rm_op(loc, "PRINT_EXPR"                   , 70)

rm_op(loc, "LIST_TO_TUPLE"                , 82)
rm_op(loc, "IMPORT_STAR"                  , 84)
rm_op(loc, "ASYNC_GEN_WRAP"               , 87)
rm_op(loc, "PREP_RERAISE_STAR"            , 88)

rm_op(loc, "JUMP_IF_FALSE_OR_POP"         , 111)
rm_op(loc, "JUMP_IF_TRUE_OR_POP"          , 112)
rm_op(loc, "POP_JUMP_FORWARD_IF_FALSE"    , 114)
rm_op(loc, "POP_JUMP_FORWARD_IF_TRUE"     , 115)

rm_op(loc, "POP_JUMP_FORWARD_IF_NONE"     , 129)
rm_op(loc, "POP_JUMP_FORWARD_IF_NOT_NONE" , 128)
rm_op(loc, "LOAD_CLASSDEREF"              , 148)

rm_op(loc, "PRECALL"                      , 166)
rm_op(loc, "POP_JUMP_BACKWARD_IF_NOT_NONE", 173)
rm_op(loc, "POP_JUMP_BACKWARD_IF_NONE"    , 174)
rm_op(loc, "POP_JUMP_BACKWARD_IF_FALSE"   , 175)
rm_op(loc, "POP_JUMP_BACKWARD_IF_TRUE"    , 176)

## These are new since 3.11...
#            OP NAME                           OPCODE  POP PUSH
#---------------------------------------------------------
def_op(loc    , "INTERPRETER_EXIT"                 , 3  ,  1, 0)
def_op(loc    , "END_FOR"                          , 4  ,  0, 1)
def_op(loc    , "END_SEND"                         , 5  ,  1, 0)
def_op(loc    , "RESERVED"                         , 17 ,  0, 1)

binary_op(loc , "BINARY_SLICE"                     , 26 ,  2, 0)
binary_op(loc , "STORE_SLICE"                      , 27 ,  0, 1)

def_op(loc    , "CLEANUP_THROW"                    , 55 ,  0, 1)
def_op(loc    , "LOAD_LOCALS"                      , 87 ,  0, 1)
def_op(loc    , "RETURN_CONST"                     , 121,  0, 1)
def_op(loc    , "LOAD_FAST_CHECK"                  , 127,  0, 1)

jrel_op(loc   , "POP_JUMP_IF_FALSE"                , 114,  1, 0)
jrel_op(loc   , "POP_JUMP_IF_TRUE"                 , 115,  1, 0)
jrel_op(loc   , "POP_JUMP_IF_NOT_NONE"             , 128,  0, 1)
jrel_op(loc   , "POP_JUMP_IF_NONE"                 , 129,  1, 0)

def_op(loc    , "LOAD_SUPER_ATTR"                  , 141,  0, 1)
def_op(loc    , "LOAD_FAST_AND_CLEAR"              , 143,  0, 1)
def_op(loc    , "YIELD_VALUE"                      , 150,  0, 1)
def_op(loc    , "CALL_INTRINSIC_1"                 , 173,  0, 1)
def_op(loc    , "CALL_INTRINSIC_2"                 , 174,  0, 1)
def_op(loc    , "LOAD_FROM_DICT_OR_GLOBALS"        , 175,  0, 1)
def_op(loc    , "LOAD_FROM_DICT_OR_DEREF"          , 176,  0, 1)

def_op(loc    , "INSTRUMENTED_LOAD_SUPER_ATTR"     , 237,  0, 1)
def_op(loc    , "INSTRUMENTED_POP_JUMP_IF_NONE"    , 238,  0, 1)
def_op(loc    , "INSTRUMENTED_POP_JUMP_IF_NOT_NONE", 239,  0, 1)
def_op(loc    , "INSTRUMENTED_RESUME"              , 240,  0, 1)
def_op(loc    , "INSTRUMENTED_CALL"                , 241,  0, 1)
def_op(loc    , "INSTRUMENTED_RETURN_VALUE"        , 242,  0, 1)
def_op(loc    , "INSTRUMENTED_YIELD_VALUE"         , 243,  0, 1)
def_op(loc    , "INSTRUMENTED_CALL_FUNCTION_EX"    , 244,  0, 1)
def_op(loc    , "INSTRUMENTED_JUMP_FORWARD"        , 245,  0, 1)
def_op(loc    , "INSTRUMENTED_JUMP_BACKWARD"       , 246,  0, 1)
def_op(loc    , "INSTRUMENTED_RETURN_CONST"        , 247,  0, 1)
def_op(loc    , "INSTRUMENTED_FOR_ITER"            , 248,  0, 1)
def_op(loc    , "INSTRUMENTED_POP_JUMP_IF_FALSE"   , 249,  0, 1)
def_op(loc    , "INSTRUMENTED_POP_JUMP_IF_TRUE"    , 250,  0, 1)
def_op(loc    , "INSTRUMENTED_END_FOR"             , 251,  0, 1)
def_op(loc    , "INSTRUMENTED_END_SEND"            , 252,  0, 1)
def_op(loc    , "INSTRUMENTED_INSTRUCTION"         , 253,  0, 1)
def_op(loc    , "INSTRUMENTED_LINE"                , 254,  0, 1)

def_op(loc    , "SETUP_FINALLY"                    , 256,  0, 1)
def_op(loc    , "SETUP_CLEANUP"                    , 257,  0, 1)
def_op(loc    , "SETUP_WITH"                       , 258,  0, 1)
def_op(loc    , "POP_BLOCK"                        , 259,  0, 1)

jrel_op(loc   , "JUMP"                             , 260,  0, 0)
jrel_op(loc   , "JUMP_NO_INTERRUPT"                , 261,  0, 0)

def_op(loc    , "LOAD_METHOD"                      , 262,  0, 1)
def_op(loc    , "LOAD_SUPER_METHOD"                , 263,  0, 1)
def_op(loc    , "LOAD_ZERO_SUPER_METHOD"           , 264,  0, 1)
def_op(loc    , "LOAD_ZERO_SUPER_ATTR"             , 265,  0, 1)
def_op(loc    , "STORE_FAST_MAYBE_NULL"            , 266,  0, 1)

### update opinfo tables
loc["hasconst"].append(121)
loc["hasfree"].extend([148, 176])
# hasjrel removed 111 112 173 174 175 176 and added 260 261
loc["hasjrel"] = [93, 110, 114, 115, 123, 128, 129, 134, 140, 260, 261]
loc["haslocal"].extend([127, 143, 266])
# hasname removed 160 and added 141 175 262 234 264 265
loc["hasname"] = [90, 91, 95, 96, 97, 98, 101, 106, 108, 109, 116, 141, 175, 262, 263, 264, 265]


### add new arg formats
_intrinsic_1_descs = [
    "INTRINSIC_1_INVALID",
    "INTRINSIC_PRINT",
    "INTRINSIC_IMPORT_STAR",
    "INTRINSIC_STOPITERATION_ERROR",
    "INTRINSIC_ASYNC_GEN_WRAP",
    "INTRINSIC_UNARY_POSITIVE",
    "INTRINSIC_LIST_TO_TUPLE",
    "INTRINSIC_TYPEVAR",
    "INTRINSIC_PARAMSPEC",
    "INTRINSIC_TYPEVARTUPLE",
    "INTRINSIC_SUBSCRIPT_GENERIC",
    "INTRINSIC_TYPEALIAS",
]

_intrinsic_2_descs = [
    "INTRINSIC_2_INVALID",
    "INTRINSIC_PREP_RERAISE_STAR",
    "INTRINSIC_TYPEVAR_WITH_BOUND",
    "INTRINSIC_TYPEVAR_WITH_CONSTRAINTS",
    "INTRINSIC_SET_FUNCTION_TYPE_PARAMS",
]

def format_CALL_INTRINSIC_1(arg) -> str:
    return _intrinsic_1_descs[arg]

def format_CALL_INTRINSIC_2(arg) -> str:
    return _intrinsic_2_descs[arg]

### update arg formatting
opcode_arg_fmt = opcode_arg_fmt312 = {
    **opcode_arg_fmt311,
    **{
        "CALL_INTRINSIC_1": format_CALL_INTRINSIC_1,
        "CALL_INTRINSIC_2": format_CALL_INTRINSIC_2,
    },
}
opcode_extended_fmt = opcode_extended_fmt312 = opcode_extended_fmt311.copy()

# overwrite legacy findlinestarts with the 3.11 version that uses the location_table syntax
from xdis.opcodes.opcode_311 import parse_location_entries, findlinestarts

update_pj3(globals(), loc)
finalize_opcodes(loc)
