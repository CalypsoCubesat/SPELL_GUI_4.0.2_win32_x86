# Python stubs generated by omniidl from USERcorbaSession.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface._GlobalIDL"
_0__GlobalIDL = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL", r"USERcorbaSession.idl")
_0__GlobalIDL__POA = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL__POA", r"USERcorbaSession.idl")

# #include "USER/USERcorbaTypes.idl"
import spell.lib.hifly.interface.USERcorbaTypes_idl
# #include "USER/USERcorbaNotificationSource.idl"
import spell.lib.hifly.interface.USERcorbaNotificationSource_idl

# interface USERcorbaSession
_0__GlobalIDL._d_USERcorbaSession = (omniORB.tcInternal.tv_objref, "IDL:USERcorbaSession:1.0", "USERcorbaSession")
omniORB.typeMapping["IDL:USERcorbaSession:1.0"] = _0__GlobalIDL._d_USERcorbaSession
_0__GlobalIDL.USERcorbaSession = omniORB.newEmptyClass()
class USERcorbaSession (_0__GlobalIDL.USERcorbaNotificationSource):
    _NP_RepositoryId = _0__GlobalIDL._d_USERcorbaSession[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.USERcorbaSession = USERcorbaSession
_0__GlobalIDL._tc_USERcorbaSession = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaSession)
omniORB.registerType(USERcorbaSession._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaSession, _0__GlobalIDL._tc_USERcorbaSession)

# USERcorbaSession operations and attributes
USERcorbaSession._d_getHostName = ((), ((omniORB.tcInternal.tv_string,0), ), None)
USERcorbaSession._d_getUserName = ((), ((omniORB.tcInternal.tv_string,0), ), None)
USERcorbaSession._d_isLoggedOn = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_short, ), None)
USERcorbaSession._d_getRoleName = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
USERcorbaSession._d_hasPrivilege = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_short, ), None)
USERcorbaSession._d_hasRole = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_short, ), None)
USERcorbaSession._d_getLoginTime = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), None)
USERcorbaSession._d_getSessionData = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaSessionData:1.0"], ), None)
USERcorbaSession._d_getRegisteredDomains = ((), (omniORB.typeMapping["IDL:USERcorbaStringMap:1.0"], ), None)
USERcorbaSession._d_getPrivilegeNames = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaStringSequence:1.0"], ), None)
USERcorbaSession._d_getOriginalPrivilegeNames = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaStringSequence:1.0"], ), None)
USERcorbaSession._d_getOrgPrivNamesWithDescr = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaStringMap:1.0"], ), None)
USERcorbaSession._d_getDonatedPrivileges = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaPrivDataSequence:1.0"], ), None)
USERcorbaSession._d_getReceivedPrivileges = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaPrivDataSequence:1.0"], ), None)
USERcorbaSession._d_getAllPrivileges = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:USERcorbaPrivDataSequence:1.0"], ), None)

# USERcorbaSession object reference
class _objref_USERcorbaSession (_0__GlobalIDL._objref_USERcorbaNotificationSource):
    _NP_RepositoryId = USERcorbaSession._NP_RepositoryId

    def __init__(self):
        _0__GlobalIDL._objref_USERcorbaNotificationSource.__init__(self)

    def getHostName(self, *args):
        return _omnipy.invoke(self, "getHostName", _0__GlobalIDL.USERcorbaSession._d_getHostName, args)

    def getUserName(self, *args):
        return _omnipy.invoke(self, "getUserName", _0__GlobalIDL.USERcorbaSession._d_getUserName, args)

    def isLoggedOn(self, *args):
        return _omnipy.invoke(self, "isLoggedOn", _0__GlobalIDL.USERcorbaSession._d_isLoggedOn, args)

    def getRoleName(self, *args):
        return _omnipy.invoke(self, "getRoleName", _0__GlobalIDL.USERcorbaSession._d_getRoleName, args)

    def hasPrivilege(self, *args):
        return _omnipy.invoke(self, "hasPrivilege", _0__GlobalIDL.USERcorbaSession._d_hasPrivilege, args)

    def hasRole(self, *args):
        return _omnipy.invoke(self, "hasRole", _0__GlobalIDL.USERcorbaSession._d_hasRole, args)

    def getLoginTime(self, *args):
        return _omnipy.invoke(self, "getLoginTime", _0__GlobalIDL.USERcorbaSession._d_getLoginTime, args)

    def getSessionData(self, *args):
        return _omnipy.invoke(self, "getSessionData", _0__GlobalIDL.USERcorbaSession._d_getSessionData, args)

    def getRegisteredDomains(self, *args):
        return _omnipy.invoke(self, "getRegisteredDomains", _0__GlobalIDL.USERcorbaSession._d_getRegisteredDomains, args)

    def getPrivilegeNames(self, *args):
        return _omnipy.invoke(self, "getPrivilegeNames", _0__GlobalIDL.USERcorbaSession._d_getPrivilegeNames, args)

    def getOriginalPrivilegeNames(self, *args):
        return _omnipy.invoke(self, "getOriginalPrivilegeNames", _0__GlobalIDL.USERcorbaSession._d_getOriginalPrivilegeNames, args)

    def getOrgPrivNamesWithDescr(self, *args):
        return _omnipy.invoke(self, "getOrgPrivNamesWithDescr", _0__GlobalIDL.USERcorbaSession._d_getOrgPrivNamesWithDescr, args)

    def getDonatedPrivileges(self, *args):
        return _omnipy.invoke(self, "getDonatedPrivileges", _0__GlobalIDL.USERcorbaSession._d_getDonatedPrivileges, args)

    def getReceivedPrivileges(self, *args):
        return _omnipy.invoke(self, "getReceivedPrivileges", _0__GlobalIDL.USERcorbaSession._d_getReceivedPrivileges, args)

    def getAllPrivileges(self, *args):
        return _omnipy.invoke(self, "getAllPrivileges", _0__GlobalIDL.USERcorbaSession._d_getAllPrivileges, args)

    __methods__ = ["getHostName", "getUserName", "isLoggedOn", "getRoleName", "hasPrivilege", "hasRole", "getLoginTime", "getSessionData", "getRegisteredDomains", "getPrivilegeNames", "getOriginalPrivilegeNames", "getOrgPrivNamesWithDescr", "getDonatedPrivileges", "getReceivedPrivileges", "getAllPrivileges"] + _0__GlobalIDL._objref_USERcorbaNotificationSource.__methods__

omniORB.registerObjref(USERcorbaSession._NP_RepositoryId, _objref_USERcorbaSession)
_0__GlobalIDL._objref_USERcorbaSession = _objref_USERcorbaSession
del USERcorbaSession, _objref_USERcorbaSession

# USERcorbaSession skeleton
__name__ = "spell.lib.hifly.interface._GlobalIDL__POA"
class USERcorbaSession (_0__GlobalIDL__POA.USERcorbaNotificationSource):
    _NP_RepositoryId = _0__GlobalIDL.USERcorbaSession._NP_RepositoryId


    _omni_op_d = {"getHostName": _0__GlobalIDL.USERcorbaSession._d_getHostName, "getUserName": _0__GlobalIDL.USERcorbaSession._d_getUserName, "isLoggedOn": _0__GlobalIDL.USERcorbaSession._d_isLoggedOn, "getRoleName": _0__GlobalIDL.USERcorbaSession._d_getRoleName, "hasPrivilege": _0__GlobalIDL.USERcorbaSession._d_hasPrivilege, "hasRole": _0__GlobalIDL.USERcorbaSession._d_hasRole, "getLoginTime": _0__GlobalIDL.USERcorbaSession._d_getLoginTime, "getSessionData": _0__GlobalIDL.USERcorbaSession._d_getSessionData, "getRegisteredDomains": _0__GlobalIDL.USERcorbaSession._d_getRegisteredDomains, "getPrivilegeNames": _0__GlobalIDL.USERcorbaSession._d_getPrivilegeNames, "getOriginalPrivilegeNames": _0__GlobalIDL.USERcorbaSession._d_getOriginalPrivilegeNames, "getOrgPrivNamesWithDescr": _0__GlobalIDL.USERcorbaSession._d_getOrgPrivNamesWithDescr, "getDonatedPrivileges": _0__GlobalIDL.USERcorbaSession._d_getDonatedPrivileges, "getReceivedPrivileges": _0__GlobalIDL.USERcorbaSession._d_getReceivedPrivileges, "getAllPrivileges": _0__GlobalIDL.USERcorbaSession._d_getAllPrivileges}
    _omni_op_d.update(_0__GlobalIDL__POA.USERcorbaNotificationSource._omni_op_d)

USERcorbaSession._omni_skeleton = USERcorbaSession
_0__GlobalIDL__POA.USERcorbaSession = USERcorbaSession
omniORB.registerSkeleton(USERcorbaSession._NP_RepositoryId, USERcorbaSession)
del USERcorbaSession
__name__ = "spell.lib.hifly.interface._GlobalIDL"

# typedef ... USERcorbaSessionSequence
class USERcorbaSessionSequence:
    _NP_RepositoryId = "IDL:USERcorbaSessionSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.USERcorbaSessionSequence = USERcorbaSessionSequence
_0__GlobalIDL._d_USERcorbaSessionSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaSession:1.0"], 0)
_0__GlobalIDL._ad_USERcorbaSessionSequence = (omniORB.tcInternal.tv_alias, USERcorbaSessionSequence._NP_RepositoryId, "USERcorbaSessionSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:USERcorbaSession:1.0"], 0))
_0__GlobalIDL._tc_USERcorbaSessionSequence = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_USERcorbaSessionSequence)
omniORB.registerType(USERcorbaSessionSequence._NP_RepositoryId, _0__GlobalIDL._ad_USERcorbaSessionSequence, _0__GlobalIDL._tc_USERcorbaSessionSequence)
del USERcorbaSessionSequence

#
# End of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface.USERcorbaSession_idl"

_exported_modules = ( "spell.lib.hifly.interface._GlobalIDL", )

# The end.
