# (C) 2024 by Rocky Bernstein
"""
Python Graal 3.10 bytecode opcodes

See com.oracle.graal.python/src/com/oracle/graal/python/compiler/OpCodes.java
"""

from xdis.opcodes.base import def_op, init_opdata

loc = locals()
init_opdata(loc, None, None)

# Instruction opcodes for compiled code
# Blank lines correspond to available opcodes

# If the POP field is -1 and the opcode is a var args operation
# then the operand holds the size.
#
# If the POP field is negative and the opcode is a nargs operation
# then pop the operand amount plus the negative of the POP amount.

# fmt: off

# Pop a single item from the stack
def_op("POP_TOP", 0, 0, 1, 0)

# Exchange two top stack items
def_op("ROT_TWO", 1, 0, 2, 2)

# Exchange three top stack items. [a, b, c] (a is top) becomes [b, c, a]
def_op("ROT_THREE", 2, 0, 3, 3)

# Exchange N top stack items. [a, b, c, ..., N] (a is top) becomes [b, c, ..., N, a]
def_op("ROT_N", 3, 1) #  (oparg, followingArgs, withJump) -> oparg, (oparg, followingArgs, withJump) -> oparg)

# Duplicates the top stack item
def_op("DUP_TOP", 4, 0, 1, 2)

# Does nothing. Might still be useful to maintain a line number#
def_op("NOP", 5, 0, 0, 0)

# Performs a unary operation specified by the immediate operand. It
# has to be the ordinal of one of {@link UnaryOps} constants.

# Pops: operand
 #Pushes: result

def_op("UNARY_OP", 6, 1, 1, 1)

# Performs a binary operation specified by the immediate operand. It has to be the ordinal of
# one of {@link BinaryOps} constants.
#
# Pops: right operand, then left operand
#
# Pushes: result
#
def_op("BINARY_OP", 7, 1, 2, 1)

# Performs subscript get operation - {@code a[b]}.
#
# Pops: {@code b}, then {@code a}
#
# Pushes: result
#
def_op("BINARY_SUBSCR", 8, 0, 2, 1)


# Performs subscript set operation - {@code a[b] = c}.
#
# Pops: {@code b}, then {@code a}, then {@code c}
#
def_op("STORE_SUBSCR", 9, 0, 3, 0)

# Performs subscript delete operation - {@code del a[b]}.
#Pops: {@code b}, then {@code a}
#
def_op("DELETE_SUBSCR", 10, 0, 2, 0)

# Gets an iterator of an object
#
# Pops: object
#
# Pushes: iterator
def_op("GET_ITER", 11, 0, 1, 1)

# Gets an iterator of an object, does nothing for a generator iterator or a coroutine
#
# Pops: object
#
# Pushes: iterator
def_op("GET_YIELD_FROM_ITER", 12, 0, 1, 1)

#Gets an awaitable of an object
#
# Pops: object
#
# Pushes: awaitable
#
def_op("GET_AWAITABLE", 13, 0, 1, 1)

# Gets the async iterator of an object - error if a coroutine is returned
#
# Pops: object
#
# Pushes: async iterator
def_op("GET_AITER", 14, 0, 1, 1)

# Get the awaitable that will return the next element of an async iterator
#
# Pops: object
# Pushes: awaitable
#
def_op("GET_ANEXT", 15, 0, 1, 1)
#
#Pushes: {@code __build_class__} builtin
#
def_op("LOAD_BUILD_CLASS", 16, 0, 0, 1)
#
#Pushes: {@code AssertionError} builtin exception type
#
def_op("LOAD_ASSERTION_ERROR", 17, 0, 0, 1)
#
#Returns the value to the caller. In generators, performs generator return.
#
#Pops: return value
#
def_op("RETURN_VALUE", 18, 0, 1, 0)
#
#Reads a name from locals dict, globals or builtins determined by the immediate operand which
#indexes the names array ({@code co_names}).
#
#Pushes: read object
#
def_op("LOAD_NAME", 19, 1, 0, 1)
#
#Writes the stack top into a name in locals dict or globals determined by the immediate
#operand which indexes the names array ({@code co_names}).
#
#Pops: object to be written
#
def_op("STORE_NAME", 20, 1, 1, 0)
#
#Deletes the name in locals dict or globals determined by the immediate operand which indexes
#the names array ({@code co_names}).
#
def_op("DELETE_NAME", 21, 1, 0, 0)
#
#Reads an attribute - {@code a.b}. {@code b} is determined by the immediate operand which
#indexes the names array ({@code co_names}).
#
#Pops: {@code a}
#
#Pushes: read attribute
#
def_op("LOAD_ATTR", 22, 1, 1, 1)
#
#Reads method on an object. The method name is determined by the first immediate operand which
#indexes the names array ({@code co_names}).
#
#Pushes: read method
#
def_op("LOAD_METHOD", 23, 1, 1, 2)
#
#Writes an attribute - {@code a.b = c}. {@code b} is determined by the immediate operand which
#indexes the names array ({@code co_names}).
#
#Pops: {@code c}, then {@code a}
#
def_op("STORE_ATTR", 24, 1, 2, 0)
#
#Deletes an attribute - {@code del a.b}. {@code b} is determined by the immediate operand
#which indexes the names array ({@code co_names}).
#
#Pops: {@code a}
#
def_op("DELETE_ATTR", 25, 1, 1, 0)
#
#Reads a global variable. The name is determined by the immediate operand which indexes the
#names array ({@code co_names}).
#
#Pushes: read object
#
def_op("LOAD_GLOBAL", 26, 1, 0, 1)
#
#Writes a global variable. The name is determined by the immediate operand which indexes the
#names array ({@code co_names}).
#
#Pops: value to be written
#
def_op("STORE_GLOBAL", 27, 1, 1, 0)
#
#Deletes a global variable. The name is determined by the immediate operand which indexes the
#names array ({@code co_names}).
#
def_op("DELETE_GLOBAL", 28, 1, 0, 0)
#
#Reads a constant object from constants array ({@code co_consts}). Performs no conversion.
#
#Pushes: read constant
#
def_op("LOAD_CONST", 29, 1, 0, 1)
#
#Reads a local variable determined by the immediate operand which indexes a stack slot and a
#variable name in varnames array ({@code co_varnames}).
#
#Pushes: read value
#
def_op("LOAD_FAST", 30, 1, 0, 1)
#
#Writes a local variable determined by the immediate operand which indexes a stack slot and a
#variable name in varnames array ({@code co_varnames}).
#
#Pops: value to be writen
#
def_op("STORE_FAST", 31, 1, 1, 0)
#
#Deletes a local variable determined by the immediate operand which indexes a stack slot and a
#variable name in varnames array ({@code co_varnames}).
#
def_op("DELETE_FAST", 32, 1, 0, 0)
#
#Reads a local cell variable determined by the immediate operand which indexes a stack slot
#after celloffset and a variable name in cellvars or freevars array ({@code co_cellvars},
#{@code co_freevars}).
#
#Pushes: cell contents
#
def_op("LOAD_DEREF", 33, 1, 0, 1)
#
#Writes a local cell variable determined by the immediate operand which indexes a stack slot
#after celloffset and a variable name in cellvars or freevars array ({@code co_cellvars},
#{@code co_freevars}).
#
#Pops: value to be written into the cell contents
#
def_op("STORE_DEREF", 34, 1, 1, 0)
#
#Deletes a local cell variable determined by the immediate operand which indexes a stack slot
#after celloffset and a variable name in cellvars or freevars array ({@code co_cellvars},
#{@code co_freevars}). Note that it doesn't delete the cell, just its contents.
#
def_op("DELETE_DEREF", 35, 1, 0, 0)
#
#TODO not implemented
#
def_op("LOAD_CLASSDEREF", 36, 1, 0, 1)
#
#Raises an exception. If the immediate operand is 0, it pops nothing and is equivalent to
#{@code raise} without arguments. If the immediate operand is 1, it is equivalent to
#{@code raise e} and it pops {@code e}. If the immediate operand is 2, it is equivalent to
#{@code raise e from c} and it pops {@code c}, then {@code e}. Other immediate operand values
#are illegal.
#
def_op("RAISE_VARARGS", 37, 1) #, (oparg, followingArgs, withJump) -> oparg, 0)
#
#Creates a slice object. If the immediate argument is 2, it is equivalent to a slice
#{@code a:b}. It pops {@code b}, then {@code a}. If the immediate argument is 3, it is
#equivalent to a slice {@code a:b:c}. It pops {@code c}, then {@code b}, then {@code a}. Other
#immediate operand values are illegal.
#
#Pushes: the created slice object
#
def_op("BUILD_SLICE", 38, 1) # (oparg, followingArgs, withJump) -> oparg, 1)
#
#Formats a value. If the immediate argument contains flag {@link FormatOptions#FVS_HAVE_SPEC},
#it is equivalent to {@code format(conv(v), spec)}. It pops {@code spec}, then {@code v}.
#Otherwise, it is equivalent to {@code format(conv(v), None)}. It pops {@code v}. {@code conv}
#is determined by the immediate operand which contains one of the {@code FVC} options in
#{@link FormatOptions}.
#
#Pushes: the formatted value
#
def_op("FORMAT_VALUE", 39, 1) # , (oparg, followingArgs, withJump) -> (oparg & FormatOptions.FVS_MASK) == FormatOptions.FVS_HAVE_SPEC ? 2 : 1, 1)

#
#Extends the immediate operand of the following instruction by its own operand shifted left by
#a byte.
#
def_op("EXTENDED_ARG", 40, 1, 0, 0)

#### Continue addin opcode numbers here...

#
#Imports a module by name determined by the immediate operand which indexes the names array
#({@code co_names}).
#
#Pops: fromlist (must be a constant {@code TruffleString[]}), then level (must be {@code int})
#
#Pushes: imported module
#
def_op("IMPORT_NAME", 1, 2, 1)
#
#Imports a name from a module. The name determined by the immediate operand which indexes the
#names array ({@code co_names}).
#
#Pops: module object
#
#Pushes: module object, imported object
#
def_op("IMPORT_FROM", 1, 1, 2)
#
#Imports all names from a module of name determined by the immediate operand which indexes the
#names array ({@code co_names}). The imported names are written to locals dict (can only be
#invoked on module level).
#
#Pops: level (must be {@code int})
#
def_op("IMPORT_STAR", 1, 1, 0)
#
#Prints the top of the stack. Used by "single" parsing mode to echo expressions.
#
#Pops: the value to print
#
def_op("PRINT_EXPR", 0, 1, 0)
#
#Creates annotations dict in locals
#
def_op("SETUP_ANNOTATIONS", 0, 0, 0)

#
#Determines if a python object is a sequence.
#
def_op("MATCH_SEQUENCE", 0, 0, 1)

#
#Determines if a python object is a mapping.
#
def_op("MATCH_MAPPING", 0, 0, 1)

#
#Determines if a python object is of a particular type.
#
def_op("MATCH_CLASS", 1, 3, 2)

#
#Matches the keys (stack top) in a dict (stack second). On successful match pushes the values
#and True, otherwise None and False.
#
def_op("MATCH_KEYS", 0, 2, 4)

#
#Creates a copy of a dict (stack second) without elements matching a tuple of keys (stack
#top).
#
def_op("COPY_DICT_WITHOUT_KEYS", 0, 1, 1)

#
#Retrieves the length of a python object and stores it on top.
#
def_op("GET_LEN", 0, 0, 1)

#  load bytecodes for special constants
def_op("LOAD_NONE", 0, 0, 1)
def_op("LOAD_ELLIPSIS", 0, 0, 1)
def_op("LOAD_TRUE", 0, 0, 1)
def_op("LOAD_FALSE", 0, 0, 1)
#
#Loads signed byte from immediate operand.
#
def_op("LOAD_BYTE", 1, 0, 1)
#
#Loads {@code int} from primitiveConstants array indexed by the immediate operand.
#
def_op("LOAD_INT", 1, 0, 1)
#
#Loads {@code long} from primitiveConstants array indexed by the immediate operand.
#
def_op("LOAD_LONG", 1, 0, 1)
#
#Loads {@code double} from primitiveConstants array indexed by the immediate operand
#(converted from long).
#
def_op("LOAD_DOUBLE", 1, 0, 1)
#
#Creates a {@link PInt} from a {@link BigInteger} in constants array indexed by the immediate
#operand.
#
def_op("LOAD_BIGINT", 1, 0, 1)
#
#Currently the same as {@link #LOAD_CONST}.
#
def_op("LOAD_STRING", 1, 0, 1)
#
#Creates python {@code bytes} from a {@code byte[]} array in constants array indexed by the
#immediate operand.
#
def_op("LOAD_BYTES", 1, 0, 1)
#
#Creates python {@code complex} from a {@code double[]} array of size 2 in constants array
#indexed by the immediate operand.
#
def_op("LOAD_COMPLEX", 1, 0, 1)

# Creates a collection out of a Java array in constants array indexed by the immediate operand.
# The second immediate operand determines the array type and kind, using values from {@link
# CollectionBits}. The only allowed kinds are list and tuple.
#
def_op("LOAD_CONST_COLLECTION", 2, 0, 1)

# -------
# calling
# -------

#
#Calls method on an object using an array as args. The receiver is taken from the first
#element of the array. The method name is determined by the immediate operand which indexes
#the names array ({@code co_names}).
#
#Pops: args ({@code Object[]} of size >= 1)
#
#Pushes: call result
#
def_op("CALL_METHOD_VARARGS", 1, 1, 1)
#
#Calls method on an object using a number of stack args determined by the first immediate
#operand.
#
#Pops: multiple arguments depending on the first immediate operand, then the method and the
#receiver
#
#Pushes: call result
#
def_op("CALL_METHOD", 1) # , (oparg, followingArgs, withJump) -> oparg + 2, 1)
#
#Calls a callable using a number of stack args determined by the immediate operand.
#
#Pops: multiple arguments depending on the immediate operand (0 - 4), then the callable
#
#Pushes: call result
#
def_op("CALL_FUNCTION", 1) # , (oparg, followingArgs, withJump) -> oparg + 1, 1)
#
#Calls a comprehension function with a single iterator argument. Comprehension functions have
#to always have the same call target at given calls site. The instruction makes use of this
#fact and bypasses function object inline caching which would otherwise slow down warmup since
#comprehensions functions are always created anew and thus the cache would always miss.
#
#Pops: iterator, then the function
#
#Pushes: call result
#
def_op("CALL_COMPREHENSION", 0, 2, 1)
#
#Calls a callable using an arguments array and keywords array.
#
#Pops: keyword args ({@code PKeyword[]}), then args ({@code Object[]}), then callable
#
#Pushes: call result
#
def_op("CALL_FUNCTION_KW", 0, 3, 1)
#
#Calls a callable using an arguments array. No keywords are passed.
#
#Pops: args ({@code Object[]}), then callable
#
#Pushes: call result
#
def_op("CALL_FUNCTION_VARARGS", 0, 2, 1)

# ----------------------
# destructuring bytecodes
# ----------------------

# Unpacks an iterable into multiple stack items.
#
# Pops: iterable
#
# Pushed: unpacked items, the count is determined by the immediate operand
#
def_op("UNPACK_SEQUENCE", 1, 1) # , (oparg, followingArgs, withJump) -> oparg)

# Unpacks an iterable into multiple stack items with a star item that gets the rest. The first
# immediate operand determines the count before the star item, the second determines the count
# after.
#
# Pops: iterable
#
# Pushed: unpacked items (count = first operand), star item, unpacked items (count = second
# operand)
#
def_op("UNPACK_EX", 2, 1) #  (oparg, followingArgs, withJump) -> oparg + 1 + Byte.toUnsignedInt(followingArgs[0]))

# jumps

#
# Get next value from an iterator. If the iterable is exhausted, jump forward by the offset in
# the immediate argument.
#
# Pops: iterator
#
# Pushes (only if not jumping): the iterator, then the next value
#
def_op("FOR_ITER", 1, 1) # (, (oparg, followingArgs, withJump) -> withJump ? 0 : 2)
#
# Jump forward by the offset in the immediate operand.
#
def_op("JUMP_FORWARD", 1, 0, 0)

#Jump backward by the offset in the immediate operand. May trigger OSR compilation.
#
def_op("JUMP_BACKWARD", 1, 0, 0)

#Jump forward by the offset in the immediate operand if the top of the stack is false (in
#Python sense).
#
#Pops (if not jumping): top of the stack
def_op("JUMP_IF_FALSE_OR_POP", 3) #, (oparg, followingArgs, withJump) -> withJump ? 0 : 1, 0)

#Jump forward by the offset in the immediate operand if the top of the stack is true (in
#Python sense).
#
#Pops (if not jumping): top of the stack
#
def_op("JUMP_IF_TRUE_OR_POP", 3) # , (oparg, followingArgs, withJump) -> withJump ? 0 : 1, 0)
#
#Jump forward by the offset in the immediate operand if the top of the stack is false (in
#Python sense).
#
#Pops: top of the stack
#
def_op("POP_AND_JUMP_IF_FALSE", 3, 1, 0)
#
#Jump forward by the offset in the immediate operand if the top of the stack is true (in
#Python sense).
#
#Pops: top of the stack
#
def_op("POP_AND_JUMP_IF_TRUE", 3, 1, 0)


# ----------------
# making callables
# ----------------

#
#Like {@link #LOAD_DEREF}, but loads the cell itself, not the contents.
#
#Pushes: the cell object
#
def_op("LOAD_CLOSURE", 1, 0, 1)
#
#Reduces multiple stack items into an array of cell objects.
#
#Pops: multiple cells (count = immediate argument)
#
#Pushes: cell object array ({@code PCell[]})
#
def_op("CLOSURE_FROM_STACK", 1) #, (oparg, followingArgs, withJump) -> oparg, 1)
#
#Creates a function object. The first immediate argument is an index to the constants array
#that determines the {@link CodeUnit} object that will provide the function's code.
#
#Pops: The second immediate arguments contains flags (defined in {@link CodeUnit}) that
#determine whether it will need to pop (in this order): closure, annotations, keyword only
#defaults, defaults.
#
#Pushes: created function
#
def_op("MAKE_FUNCTION", 2) # , (oparg, followingArgs, withJump) -> Integer.bitCount(followingArgs[0]), 1)

# -------------------
# collection literals
# -------------------

#
#Creates a collection from multiple elements from the stack. Collection type is determined by
#{@link CollectionBits} in immediate operand.
#
#Pops: items for the collection (count = immediate argument)
#
#Pushes: new collection
#
def_op("COLLECTION_FROM_STACK", 1) # , (oparg, followingArgs, withJump) -> CollectionBits.elementCount(oparg), 1)
#
#Add multiple elements from the stack to the collection below them. Collection type is
#determined by {@link CollectionBits} in immediate operand. Tuple is not supported.
#
#Pops: items to be added (count = immediate argument)
#
def_op("COLLECTION_ADD_STACK", 1) # , (oparg, followingArgs, withJump) -> CollectionBits.elementCount(oparg) + 1, 1)
#
#Concatenates two collection of the same type. Collection type is determined by
#{@link CollectionBits} in immediate operand. Tuple is not supported.
#
#Pops: second collection, first collection
#
#Pushes: concatenated collection
#
def_op("COLLECTION_ADD_COLLECTION", 1, 2, 1)
#
#Converts collection to another type determined by {@link CollectionBits} in immediate
#operand. The converted collection is expected to be an independent copy (they don't share
#storage).
#
#Pops: original collection
#
#Pushes: converted collection
#
def_op("COLLECTION_FROM_COLLECTION", 1, 1, 1)
#
#Converts list to tuple by reusing the underlying storage.
#
#Pops: list
#
#Pushes: tuple
#
def_op("TUPLE_FROM_LIST", 0, 1, 1)
#
#Converts list to frozenset.
#
#Pops: list
#
#Pushes: frozenset
#
def_op("FROZENSET_FROM_LIST", 0, 1, 1)
#
#Adds an item to a collection that is multiple items deep under the top of the stack,
#determined by the immediate argument.
#
#Pops: item to be added
#
def_op("ADD_TO_COLLECTION", 1) #  (oparg, followingArgs, withJump) -> CollectionBits.collectionKind(oparg) == CollectionBits.KIND_DICT ? 2 : 1, 0)
#
#Like {@link #COLLECTION_ADD_COLLECTION} for dicts, but with checks for duplicate keys
#necessary for keyword arguments merge. Note it works with dicts. Keyword arrays need to be
#converted to dicts first.
#
def_op("KWARGS_DICT_MERGE", 0, 2, 1)
#
#Create a single {@link PKeyword} object. The name is determined by the immediate operand
#which indexes the names array ({@code co_names})
#
#Pops: keyword value
#
#Pushes: keyword object
#
def_op("MAKE_KEYWORD", 1, 1, 1)

#-----------
# exceptions
#-----------

#
#Jump forward by the offset in the immediate argument if the exception doesn't match the
#expected type. The exception object is {@link PException}, not a python exception.
#
#Pops: expected type, then exception
#
#Pushes (if jumping): the exception
#
def_op("MATCH_EXC_OR_JUMP", 3, 2, 1)
#
#Save the current exception state on the stack and set it to the exception on the stack. The
#exception object is {@link PException}, not a python exception. The exception is pushed back
#to the top.
#
#Pops: the exception
#
#Pushes: the saved exception state, the exception
#
def_op("PUSH_EXC_INFO", 0, 0, 1)

# Sets the current exception state to the saved state (by {@link #PUSH_EXC_INFO}) on the stack
# and pop it.
#
# Pops: save exception state
def_op("POP_EXCEPT", 0, 1, 0)

# Restore exception state and reraise exception.
#
# Pops: exception to reraise, then saved exception state
def_op("END_EXC_HANDLER", 0, 2, 0)

# Gets the python-level exception object from a {@link PException}.
#
# Pops: a {@link PException} Pushes: python exception
#
def_op("UNWRAP_EXC", 0, 1, 1)

# ----------
# generators
# ----------
#
#Yield value from the stack to the caller. Saves execution state. The generator will resume at
#the next instruction.
#
#Pops: yielded value
#
def_op("YIELD_VALUE", 0, 1, 0)
#
#Wrap value from the stack in a {@link PAsyncGenWrappedValue}. CPython 3.11 opcode, used here
#to avoid a runtime check
#
#Pops: an object Pushes: async_generator_wrapped_value
#
def_op("ASYNCGEN_WRAP", 0, 1, 1)
#
#Resume after yield. Will raise exception passed by {@code throw} if any.
#
#Pushes: value received from {@code send} or {@code None}.
#
def_op("RESUME_YIELD", 0, 0, 1)
#
#Send value into a generator. Jumps forward by the offset in the immediate argument if the
#generator is exhausted. Used to implement {@code yield from}.
#
#Pops: value to be sent, then generator
#
#Pushes (if not jumping): the generator, then the yielded value
#
#Pushes (if jumping): the generator return value
#
def_op("SEND", 1, 2) #, (oparg, followingArgs, withJump) -> withJump ? 1 : 2)

# Exception handler for forwarding {@code throw} calls into {@code yield from}.
#
# Pops: exception, then the generator
#
# Pushes (if not jumping): the generator, then the yielded value
#
# Pushes (if jumping): the generator return value
def_op("THROW", 1, 2) #, (oparg, followingArgs, withJump) -> withJump ? 1 : 2)

# Exception handler for async for loops. If the current exception is StopAsyncIteration, handle
# it, otherwise, reraise.
#
# Pops: exception, then the anext coroutine, then the async iterator
def_op("END_ASYNC_FOR", 0, 3, 0)

# with statements
#
#Enter a context manager and save data for its exit.
#
#Pops: the context manager
#
# Pushes: the context manager, then maybe-bound {@code __exit__}, then the result of
# {@code __enter__}
def_op("SETUP_WITH", 0, 1, 3)

# Run the exit handler of a context manager and reraise if necessary.
#
#Pops: exception or {@code None}, then maybe-bound {@code __exit__}, then the context manager

def_op("EXIT_WITH", 0, 3, 0)

# Enter a context manager and save data for its exit
#
# Pops: the context manager
#
#Pushes: the context manager, then the maybe-bound async function {@code __aexit__}, then the
#awaitable returned by {@code __aenter__}
#
def_op("SETUP_AWITH", 0, 1, 3)

# Run the exit handler of a context manager
#
# Pops: exception or {@code None}, then maybe-bound {@code __aexit__}, then the context manager
#
# Pushes: the exception or {@code None}, then the awaitable returned by {@code __aexit__}
def_op("GET_AEXIT_CORO", 0, 3, 2)

#Reraise the exception passed to {@code __aexit__} if appropriate
#
#!Pops: The result of awaiting {@code __aexit__}, then the exception

def_op("EXIT_AWITH", 0, 2, 0)
# Pop a single item from the stack#

def_op(loc,   "POP_TOP",                  1,  1,  0)
def_op(loc,   "ROT_TWO",                  2,  2,  2)
def_op(loc,   "ROT_THREE",                3,  3,  3)
def_op(loc,   "DUP_TOP",                  4,  0,  1)
def_op(loc,   "ROT_N",                    5,  0,  0)
def_op(loc,   "DUP_TOP",                  6,  0,  2)
def_op(loc,   "NOP",                      7,  0,  2)
def_op(loc,   "UNARY_OP",                 8,  0,  2)
def_op(loc,   "BINARY_OP",                9,  0,  2)
def_op(loc,   "BINARY_SUBSCR",           10,  0,  2)
def_op(loc,   "STORE_SUBSCR",            10,  0,  2)
def_op(loc,   "DELETE_SUBSCR",           10,  0,  2)
# fmt: on
