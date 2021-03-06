# Python stubs generated by omniidl from IMIB_PRO.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)

# #include "IBASE.idl"
import spell.lib.hifly.interface.IBASE_idl
_0_IBASE = omniORB.openModule("spell.lib.hifly.interface.IBASE")
_0_IBASE__POA = omniORB.openModule("spell.lib.hifly.interface.IBASE__POA")
# #include "IMIB.idl"
import spell.lib.hifly.interface.IMIB_idl
_0_IMIB = omniORB.openModule("spell.lib.hifly.interface.IMIB")
_0_IMIB__POA = omniORB.openModule("spell.lib.hifly.interface.IMIB__POA")

#
# Start of module "IMIB_PRO"
#
__name__ = "spell.lib.hifly.interface.IMIB_PRO"
_0_IMIB_PRO = omniORB.openModule("spell.lib.hifly.interface.IMIB_PRO", r"IMIB_PRO.idl")
_0_IMIB_PRO__POA = omniORB.openModule("spell.lib.hifly.interface.IMIB_PRO__POA", r"IMIB_PRO.idl")


# interface DefIterator
_0_IMIB_PRO._d_DefIterator = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/DefIterator:1.0", "DefIterator")
omniORB.typeMapping["IDL:IMIB_PRO/DefIterator:1.0"] = _0_IMIB_PRO._d_DefIterator
_0_IMIB_PRO.DefIterator = omniORB.newEmptyClass()
class DefIterator :
    _NP_RepositoryId = _0_IMIB_PRO._d_DefIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_IMIB_PRO.DefIterator = DefIterator
_0_IMIB_PRO._tc_DefIterator = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_DefIterator)
omniORB.registerType(DefIterator._NP_RepositoryId, _0_IMIB_PRO._d_DefIterator, _0_IMIB_PRO._tc_DefIterator)

# DefIterator operations and attributes
DefIterator._d_getLastChanges = ((), (omniORB.typeMapping["IDL:IBASE/Time:1.0"], ), None)
DefIterator._d_getCount = ((), (omniORB.tcInternal.tv_long, ), None)
DefIterator._d_getNames = ((), (omniORB.typeMapping["IDL:IBASE/Strings:1.0"], ), None)
DefIterator._d_getDefsAsTable = ((omniORB.typeMapping["IDL:IBASE/Strings:1.0"], omniORB.typeMapping["IDL:IMIB/AttributeType:1.0"]), (omniORB.typeMapping["IDL:IMIB/DataTable:1.0"], ), None)

# DefIterator object reference
class _objref_DefIterator (CORBA.Object):
    _NP_RepositoryId = DefIterator._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def getLastChanges(self, *args):
        return _omnipy.invoke(self, "getLastChanges", _0_IMIB_PRO.DefIterator._d_getLastChanges, args)

    def getCount(self, *args):
        return _omnipy.invoke(self, "getCount", _0_IMIB_PRO.DefIterator._d_getCount, args)

    def getNames(self, *args):
        return _omnipy.invoke(self, "getNames", _0_IMIB_PRO.DefIterator._d_getNames, args)

    def getDefsAsTable(self, *args):
        return _omnipy.invoke(self, "getDefsAsTable", _0_IMIB_PRO.DefIterator._d_getDefsAsTable, args)

    __methods__ = ["getLastChanges", "getCount", "getNames", "getDefsAsTable"] + CORBA.Object.__methods__

omniORB.registerObjref(DefIterator._NP_RepositoryId, _objref_DefIterator)
_0_IMIB_PRO._objref_DefIterator = _objref_DefIterator
del DefIterator, _objref_DefIterator

# DefIterator skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class DefIterator (PortableServer.Servant):
    _NP_RepositoryId = _0_IMIB_PRO.DefIterator._NP_RepositoryId


    _omni_op_d = {"getLastChanges": _0_IMIB_PRO.DefIterator._d_getLastChanges, "getCount": _0_IMIB_PRO.DefIterator._d_getCount, "getNames": _0_IMIB_PRO.DefIterator._d_getNames, "getDefsAsTable": _0_IMIB_PRO.DefIterator._d_getDefsAsTable}

DefIterator._omni_skeleton = DefIterator
_0_IMIB_PRO__POA.DefIterator = DefIterator
omniORB.registerSkeleton(DefIterator._NP_RepositoryId, DefIterator)
del DefIterator
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

# interface ParamDefIterator
_0_IMIB_PRO._d_ParamDefIterator = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/ParamDefIterator:1.0", "ParamDefIterator")
omniORB.typeMapping["IDL:IMIB_PRO/ParamDefIterator:1.0"] = _0_IMIB_PRO._d_ParamDefIterator
_0_IMIB_PRO.ParamDefIterator = omniORB.newEmptyClass()
class ParamDefIterator (_0_IMIB_PRO.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO._d_ParamDefIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_IMIB_PRO.ParamDefIterator = ParamDefIterator
_0_IMIB_PRO._tc_ParamDefIterator = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_ParamDefIterator)
omniORB.registerType(ParamDefIterator._NP_RepositoryId, _0_IMIB_PRO._d_ParamDefIterator, _0_IMIB_PRO._tc_ParamDefIterator)

# ParamDefIterator operations and attributes
ParamDefIterator._d_getDef = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:IMIB/ParamDef:1.0"], ), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound})
ParamDefIterator._d_getDefs = ((omniORB.typeMapping["IDL:IBASE/Strings:1.0"], ), (omniORB.typeMapping["IDL:IMIB/ParamDefs:1.0"], ), None)

# ParamDefIterator object reference
class _objref_ParamDefIterator (_0_IMIB_PRO._objref_DefIterator):
    _NP_RepositoryId = ParamDefIterator._NP_RepositoryId

    def __init__(self):
        _0_IMIB_PRO._objref_DefIterator.__init__(self)

    def getDef(self, *args):
        return _omnipy.invoke(self, "getDef", _0_IMIB_PRO.ParamDefIterator._d_getDef, args)

    def getDefs(self, *args):
        return _omnipy.invoke(self, "getDefs", _0_IMIB_PRO.ParamDefIterator._d_getDefs, args)

    __methods__ = ["getDef", "getDefs"] + _0_IMIB_PRO._objref_DefIterator.__methods__

omniORB.registerObjref(ParamDefIterator._NP_RepositoryId, _objref_ParamDefIterator)
_0_IMIB_PRO._objref_ParamDefIterator = _objref_ParamDefIterator
del ParamDefIterator, _objref_ParamDefIterator

# ParamDefIterator skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class ParamDefIterator (_0_IMIB_PRO__POA.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO.ParamDefIterator._NP_RepositoryId


    _omni_op_d = {"getDef": _0_IMIB_PRO.ParamDefIterator._d_getDef, "getDefs": _0_IMIB_PRO.ParamDefIterator._d_getDefs}
    _omni_op_d.update(_0_IMIB_PRO__POA.DefIterator._omni_op_d)

ParamDefIterator._omni_skeleton = ParamDefIterator
_0_IMIB_PRO__POA.ParamDefIterator = ParamDefIterator
omniORB.registerSkeleton(ParamDefIterator._NP_RepositoryId, ParamDefIterator)
del ParamDefIterator
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

# interface CommandDefIterator
_0_IMIB_PRO._d_CommandDefIterator = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/CommandDefIterator:1.0", "CommandDefIterator")
omniORB.typeMapping["IDL:IMIB_PRO/CommandDefIterator:1.0"] = _0_IMIB_PRO._d_CommandDefIterator
_0_IMIB_PRO.CommandDefIterator = omniORB.newEmptyClass()
class CommandDefIterator (_0_IMIB_PRO.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO._d_CommandDefIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_IMIB_PRO.CommandDefIterator = CommandDefIterator
_0_IMIB_PRO._tc_CommandDefIterator = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_CommandDefIterator)
omniORB.registerType(CommandDefIterator._NP_RepositoryId, _0_IMIB_PRO._d_CommandDefIterator, _0_IMIB_PRO._tc_CommandDefIterator)

# CommandDefIterator operations and attributes
CommandDefIterator._d_getDef = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:IMIB/CommandDef:1.0"], ), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound})
CommandDefIterator._d_getDefs = ((omniORB.typeMapping["IDL:IBASE/Strings:1.0"], ), (omniORB.typeMapping["IDL:IMIB/CommandDefs:1.0"], ), None)

# CommandDefIterator object reference
class _objref_CommandDefIterator (_0_IMIB_PRO._objref_DefIterator):
    _NP_RepositoryId = CommandDefIterator._NP_RepositoryId

    def __init__(self):
        _0_IMIB_PRO._objref_DefIterator.__init__(self)

    def getDef(self, *args):
        return _omnipy.invoke(self, "getDef", _0_IMIB_PRO.CommandDefIterator._d_getDef, args)

    def getDefs(self, *args):
        return _omnipy.invoke(self, "getDefs", _0_IMIB_PRO.CommandDefIterator._d_getDefs, args)

    __methods__ = ["getDef", "getDefs"] + _0_IMIB_PRO._objref_DefIterator.__methods__

omniORB.registerObjref(CommandDefIterator._NP_RepositoryId, _objref_CommandDefIterator)
_0_IMIB_PRO._objref_CommandDefIterator = _objref_CommandDefIterator
del CommandDefIterator, _objref_CommandDefIterator

# CommandDefIterator skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class CommandDefIterator (_0_IMIB_PRO__POA.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO.CommandDefIterator._NP_RepositoryId


    _omni_op_d = {"getDef": _0_IMIB_PRO.CommandDefIterator._d_getDef, "getDefs": _0_IMIB_PRO.CommandDefIterator._d_getDefs}
    _omni_op_d.update(_0_IMIB_PRO__POA.DefIterator._omni_op_d)

CommandDefIterator._omni_skeleton = CommandDefIterator
_0_IMIB_PRO__POA.CommandDefIterator = CommandDefIterator
omniORB.registerSkeleton(CommandDefIterator._NP_RepositoryId, CommandDefIterator)
del CommandDefIterator
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

# interface ANDdefIterator
_0_IMIB_PRO._d_ANDdefIterator = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/ANDdefIterator:1.0", "ANDdefIterator")
omniORB.typeMapping["IDL:IMIB_PRO/ANDdefIterator:1.0"] = _0_IMIB_PRO._d_ANDdefIterator
_0_IMIB_PRO.ANDdefIterator = omniORB.newEmptyClass()
class ANDdefIterator (_0_IMIB_PRO.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO._d_ANDdefIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_IMIB_PRO.ANDdefIterator = ANDdefIterator
_0_IMIB_PRO._tc_ANDdefIterator = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_ANDdefIterator)
omniORB.registerType(ANDdefIterator._NP_RepositoryId, _0_IMIB_PRO._d_ANDdefIterator, _0_IMIB_PRO._tc_ANDdefIterator)

# ANDdefIterator operations and attributes
ANDdefIterator._d_getDef = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:IMIB/ANDdef:1.0"], ), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound})
ANDdefIterator._d_getDefs = ((omniORB.typeMapping["IDL:IBASE/Strings:1.0"], ), (omniORB.typeMapping["IDL:IMIB/ANDdefs:1.0"], ), None)

# ANDdefIterator object reference
class _objref_ANDdefIterator (_0_IMIB_PRO._objref_DefIterator):
    _NP_RepositoryId = ANDdefIterator._NP_RepositoryId

    def __init__(self):
        _0_IMIB_PRO._objref_DefIterator.__init__(self)

    def getDef(self, *args):
        return _omnipy.invoke(self, "getDef", _0_IMIB_PRO.ANDdefIterator._d_getDef, args)

    def getDefs(self, *args):
        return _omnipy.invoke(self, "getDefs", _0_IMIB_PRO.ANDdefIterator._d_getDefs, args)

    __methods__ = ["getDef", "getDefs"] + _0_IMIB_PRO._objref_DefIterator.__methods__

omniORB.registerObjref(ANDdefIterator._NP_RepositoryId, _objref_ANDdefIterator)
_0_IMIB_PRO._objref_ANDdefIterator = _objref_ANDdefIterator
del ANDdefIterator, _objref_ANDdefIterator

# ANDdefIterator skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class ANDdefIterator (_0_IMIB_PRO__POA.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO.ANDdefIterator._NP_RepositoryId


    _omni_op_d = {"getDef": _0_IMIB_PRO.ANDdefIterator._d_getDef, "getDefs": _0_IMIB_PRO.ANDdefIterator._d_getDefs}
    _omni_op_d.update(_0_IMIB_PRO__POA.DefIterator._omni_op_d)

ANDdefIterator._omni_skeleton = ANDdefIterator
_0_IMIB_PRO__POA.ANDdefIterator = ANDdefIterator
omniORB.registerSkeleton(ANDdefIterator._NP_RepositoryId, ANDdefIterator)
del ANDdefIterator
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

# interface GRDdefIterator
_0_IMIB_PRO._d_GRDdefIterator = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/GRDdefIterator:1.0", "GRDdefIterator")
omniORB.typeMapping["IDL:IMIB_PRO/GRDdefIterator:1.0"] = _0_IMIB_PRO._d_GRDdefIterator
_0_IMIB_PRO.GRDdefIterator = omniORB.newEmptyClass()
class GRDdefIterator (_0_IMIB_PRO.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO._d_GRDdefIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_IMIB_PRO.GRDdefIterator = GRDdefIterator
_0_IMIB_PRO._tc_GRDdefIterator = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_GRDdefIterator)
omniORB.registerType(GRDdefIterator._NP_RepositoryId, _0_IMIB_PRO._d_GRDdefIterator, _0_IMIB_PRO._tc_GRDdefIterator)

# GRDdefIterator operations and attributes
GRDdefIterator._d_getDef = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:IMIB/GRDdef:1.0"], ), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound})
GRDdefIterator._d_getDefs = ((omniORB.typeMapping["IDL:IBASE/Strings:1.0"], ), (omniORB.typeMapping["IDL:IMIB/GRDdefs:1.0"], ), None)

# GRDdefIterator object reference
class _objref_GRDdefIterator (_0_IMIB_PRO._objref_DefIterator):
    _NP_RepositoryId = GRDdefIterator._NP_RepositoryId

    def __init__(self):
        _0_IMIB_PRO._objref_DefIterator.__init__(self)

    def getDef(self, *args):
        return _omnipy.invoke(self, "getDef", _0_IMIB_PRO.GRDdefIterator._d_getDef, args)

    def getDefs(self, *args):
        return _omnipy.invoke(self, "getDefs", _0_IMIB_PRO.GRDdefIterator._d_getDefs, args)

    __methods__ = ["getDef", "getDefs"] + _0_IMIB_PRO._objref_DefIterator.__methods__

omniORB.registerObjref(GRDdefIterator._NP_RepositoryId, _objref_GRDdefIterator)
_0_IMIB_PRO._objref_GRDdefIterator = _objref_GRDdefIterator
del GRDdefIterator, _objref_GRDdefIterator

# GRDdefIterator skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class GRDdefIterator (_0_IMIB_PRO__POA.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO.GRDdefIterator._NP_RepositoryId


    _omni_op_d = {"getDef": _0_IMIB_PRO.GRDdefIterator._d_getDef, "getDefs": _0_IMIB_PRO.GRDdefIterator._d_getDefs}
    _omni_op_d.update(_0_IMIB_PRO__POA.DefIterator._omni_op_d)

GRDdefIterator._omni_skeleton = GRDdefIterator
_0_IMIB_PRO__POA.GRDdefIterator = GRDdefIterator
omniORB.registerSkeleton(GRDdefIterator._NP_RepositoryId, GRDdefIterator)
del GRDdefIterator
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

# interface SCRdefIterator
_0_IMIB_PRO._d_SCRdefIterator = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/SCRdefIterator:1.0", "SCRdefIterator")
omniORB.typeMapping["IDL:IMIB_PRO/SCRdefIterator:1.0"] = _0_IMIB_PRO._d_SCRdefIterator
_0_IMIB_PRO.SCRdefIterator = omniORB.newEmptyClass()
class SCRdefIterator (_0_IMIB_PRO.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO._d_SCRdefIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_IMIB_PRO.SCRdefIterator = SCRdefIterator
_0_IMIB_PRO._tc_SCRdefIterator = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_SCRdefIterator)
omniORB.registerType(SCRdefIterator._NP_RepositoryId, _0_IMIB_PRO._d_SCRdefIterator, _0_IMIB_PRO._tc_SCRdefIterator)

# SCRdefIterator operations and attributes
SCRdefIterator._d_getDef = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:IMIB/SCRdef:1.0"], ), {_0_IBASE.NotFound._NP_RepositoryId: _0_IBASE._d_NotFound})
SCRdefIterator._d_getDefs = ((omniORB.typeMapping["IDL:IBASE/Strings:1.0"], ), (omniORB.typeMapping["IDL:IMIB/SCRdefs:1.0"], ), None)

# SCRdefIterator object reference
class _objref_SCRdefIterator (_0_IMIB_PRO._objref_DefIterator):
    _NP_RepositoryId = SCRdefIterator._NP_RepositoryId

    def __init__(self):
        _0_IMIB_PRO._objref_DefIterator.__init__(self)

    def getDef(self, *args):
        return _omnipy.invoke(self, "getDef", _0_IMIB_PRO.SCRdefIterator._d_getDef, args)

    def getDefs(self, *args):
        return _omnipy.invoke(self, "getDefs", _0_IMIB_PRO.SCRdefIterator._d_getDefs, args)

    __methods__ = ["getDef", "getDefs"] + _0_IMIB_PRO._objref_DefIterator.__methods__

omniORB.registerObjref(SCRdefIterator._NP_RepositoryId, _objref_SCRdefIterator)
_0_IMIB_PRO._objref_SCRdefIterator = _objref_SCRdefIterator
del SCRdefIterator, _objref_SCRdefIterator

# SCRdefIterator skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class SCRdefIterator (_0_IMIB_PRO__POA.DefIterator):
    _NP_RepositoryId = _0_IMIB_PRO.SCRdefIterator._NP_RepositoryId


    _omni_op_d = {"getDef": _0_IMIB_PRO.SCRdefIterator._d_getDef, "getDefs": _0_IMIB_PRO.SCRdefIterator._d_getDefs}
    _omni_op_d.update(_0_IMIB_PRO__POA.DefIterator._omni_op_d)

SCRdefIterator._omni_skeleton = SCRdefIterator
_0_IMIB_PRO__POA.SCRdefIterator = SCRdefIterator
omniORB.registerSkeleton(SCRdefIterator._NP_RepositoryId, SCRdefIterator)
del SCRdefIterator
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

# interface MIBmngr
_0_IMIB_PRO._d_MIBmngr = (omniORB.tcInternal.tv_objref, "IDL:IMIB_PRO/MIBmngr:1.0", "MIBmngr")
omniORB.typeMapping["IDL:IMIB_PRO/MIBmngr:1.0"] = _0_IMIB_PRO._d_MIBmngr
_0_IMIB_PRO.MIBmngr = omniORB.newEmptyClass()
class MIBmngr :
    _NP_RepositoryId = _0_IMIB_PRO._d_MIBmngr[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    ServiceName = "MIB_PRO"


_0_IMIB_PRO.MIBmngr = MIBmngr
_0_IMIB_PRO._tc_MIBmngr = omniORB.tcInternal.createTypeCode(_0_IMIB_PRO._d_MIBmngr)
omniORB.registerType(MIBmngr._NP_RepositoryId, _0_IMIB_PRO._d_MIBmngr, _0_IMIB_PRO._tc_MIBmngr)

# MIBmngr operations and attributes
MIBmngr._d_getParamDefIterator = ((), (omniORB.typeMapping["IDL:IMIB_PRO/ParamDefIterator:1.0"], ), None)
MIBmngr._d_getCommandDefIterator = ((), (omniORB.typeMapping["IDL:IMIB_PRO/CommandDefIterator:1.0"], ), None)
MIBmngr._d_getANDdefIterator = ((), (omniORB.typeMapping["IDL:IMIB_PRO/ANDdefIterator:1.0"], ), None)
MIBmngr._d_getGRDdefIterator = ((), (omniORB.typeMapping["IDL:IMIB_PRO/GRDdefIterator:1.0"], ), None)
MIBmngr._d_getSCRdefIterator = ((), (omniORB.typeMapping["IDL:IMIB_PRO/SCRdefIterator:1.0"], ), None)

# MIBmngr object reference
class _objref_MIBmngr (CORBA.Object):
    _NP_RepositoryId = MIBmngr._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def getParamDefIterator(self, *args):
        return _omnipy.invoke(self, "getParamDefIterator", _0_IMIB_PRO.MIBmngr._d_getParamDefIterator, args)

    def getCommandDefIterator(self, *args):
        return _omnipy.invoke(self, "getCommandDefIterator", _0_IMIB_PRO.MIBmngr._d_getCommandDefIterator, args)

    def getANDdefIterator(self, *args):
        return _omnipy.invoke(self, "getANDdefIterator", _0_IMIB_PRO.MIBmngr._d_getANDdefIterator, args)

    def getGRDdefIterator(self, *args):
        return _omnipy.invoke(self, "getGRDdefIterator", _0_IMIB_PRO.MIBmngr._d_getGRDdefIterator, args)

    def getSCRdefIterator(self, *args):
        return _omnipy.invoke(self, "getSCRdefIterator", _0_IMIB_PRO.MIBmngr._d_getSCRdefIterator, args)

    __methods__ = ["getParamDefIterator", "getCommandDefIterator", "getANDdefIterator", "getGRDdefIterator", "getSCRdefIterator"] + CORBA.Object.__methods__

omniORB.registerObjref(MIBmngr._NP_RepositoryId, _objref_MIBmngr)
_0_IMIB_PRO._objref_MIBmngr = _objref_MIBmngr
del MIBmngr, _objref_MIBmngr

# MIBmngr skeleton
__name__ = "spell.lib.hifly.interface.IMIB_PRO__POA"
class MIBmngr (PortableServer.Servant):
    _NP_RepositoryId = _0_IMIB_PRO.MIBmngr._NP_RepositoryId


    _omni_op_d = {"getParamDefIterator": _0_IMIB_PRO.MIBmngr._d_getParamDefIterator, "getCommandDefIterator": _0_IMIB_PRO.MIBmngr._d_getCommandDefIterator, "getANDdefIterator": _0_IMIB_PRO.MIBmngr._d_getANDdefIterator, "getGRDdefIterator": _0_IMIB_PRO.MIBmngr._d_getGRDdefIterator, "getSCRdefIterator": _0_IMIB_PRO.MIBmngr._d_getSCRdefIterator}

MIBmngr._omni_skeleton = MIBmngr
_0_IMIB_PRO__POA.MIBmngr = MIBmngr
omniORB.registerSkeleton(MIBmngr._NP_RepositoryId, MIBmngr)
del MIBmngr
__name__ = "spell.lib.hifly.interface.IMIB_PRO"

#
# End of module "IMIB_PRO"
#
__name__ = "spell.lib.hifly.interface.IMIB_PRO_idl"

_exported_modules = ( "spell.lib.hifly.interface.IMIB_PRO", )

# The end.
