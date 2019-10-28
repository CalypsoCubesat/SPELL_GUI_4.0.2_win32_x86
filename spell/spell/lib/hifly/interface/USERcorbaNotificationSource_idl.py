# Python stubs generated by omniidl from USERcorbaNotificationSource.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface._GlobalIDL"
_0__GlobalIDL = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL", r"USERcorbaNotificationSource.idl")
_0__GlobalIDL__POA = omniORB.openModule("spell.lib.hifly.interface._GlobalIDL__POA", r"USERcorbaNotificationSource.idl")

# #include "USER/USERcorbaTypes.idl"
import spell.lib.hifly.interface.USERcorbaTypes_idl

# interface USERcorbaNotificationSource;
_0__GlobalIDL._d_USERcorbaNotificationSource = (omniORB.tcInternal.tv_objref, "IDL:USERcorbaNotificationSource:1.0", "USERcorbaNotificationSource")
omniORB.typeMapping["IDL:USERcorbaNotificationSource:1.0"] = _0__GlobalIDL._d_USERcorbaNotificationSource

# enum UserEventType
_0__GlobalIDL.EV_MESSAGE = omniORB.EnumItem("EV_MESSAGE", 0)
_0__GlobalIDL.EV_LOGIN = omniORB.EnumItem("EV_LOGIN", 1)
_0__GlobalIDL.EV_LOGOUT = omniORB.EnumItem("EV_LOGOUT", 2)
_0__GlobalIDL.EV_ROLE_CHANGE = omniORB.EnumItem("EV_ROLE_CHANGE", 3)
_0__GlobalIDL.EV_PRIVILEGE_CHANGE = omniORB.EnumItem("EV_PRIVILEGE_CHANGE", 4)
_0__GlobalIDL.EV_PROFILE_CHANGE = omniORB.EnumItem("EV_PROFILE_CHANGE", 5)
_0__GlobalIDL.EV_ANY = omniORB.EnumItem("EV_ANY", 6)
_0__GlobalIDL.EV_USER_STARTUP = omniORB.EnumItem("EV_USER_STARTUP", 7)
_0__GlobalIDL.UserEventType = omniORB.Enum("IDL:UserEventType:1.0", (_0__GlobalIDL.EV_MESSAGE, _0__GlobalIDL.EV_LOGIN, _0__GlobalIDL.EV_LOGOUT, _0__GlobalIDL.EV_ROLE_CHANGE, _0__GlobalIDL.EV_PRIVILEGE_CHANGE, _0__GlobalIDL.EV_PROFILE_CHANGE, _0__GlobalIDL.EV_ANY, _0__GlobalIDL.EV_USER_STARTUP,))

_0__GlobalIDL._d_UserEventType  = (omniORB.tcInternal.tv_enum, _0__GlobalIDL.UserEventType._NP_RepositoryId, "UserEventType", _0__GlobalIDL.UserEventType._items)
_0__GlobalIDL._tc_UserEventType = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_UserEventType)
omniORB.registerType(_0__GlobalIDL.UserEventType._NP_RepositoryId, _0__GlobalIDL._d_UserEventType, _0__GlobalIDL._tc_UserEventType)

# interface USERcorbaNotifier
_0__GlobalIDL._d_USERcorbaNotifier = (omniORB.tcInternal.tv_objref, "IDL:USERcorbaNotifier:1.0", "USERcorbaNotifier")
omniORB.typeMapping["IDL:USERcorbaNotifier:1.0"] = _0__GlobalIDL._d_USERcorbaNotifier
_0__GlobalIDL.USERcorbaNotifier = omniORB.newEmptyClass()
class USERcorbaNotifier :
    _NP_RepositoryId = _0__GlobalIDL._d_USERcorbaNotifier[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.USERcorbaNotifier = USERcorbaNotifier
_0__GlobalIDL._tc_USERcorbaNotifier = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaNotifier)
omniORB.registerType(USERcorbaNotifier._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaNotifier, _0__GlobalIDL._tc_USERcorbaNotifier)

# USERcorbaNotifier operations and attributes
USERcorbaNotifier._d_trigger = ((omniORB.typeMapping["IDL:USERcorbaNotificationSource:1.0"], omniORB.typeMapping["IDL:UserEventType:1.0"], (omniORB.tcInternal.tv_string,0)), None, None)
USERcorbaNotifier._d_sendMessage = (((omniORB.tcInternal.tv_string,0), ), None, None)
USERcorbaNotifier._d_id = ((), ((omniORB.tcInternal.tv_string,0), ), None)
USERcorbaNotifier._d_deactivate = ((), None, None)
USERcorbaNotifier._d_getEventType = ((), (omniORB.typeMapping["IDL:UserEventType:1.0"], ), None)

# USERcorbaNotifier object reference
class _objref_USERcorbaNotifier (CORBA.Object):
    _NP_RepositoryId = USERcorbaNotifier._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def trigger(self, *args):
        return _omnipy.invoke(self, "trigger", _0__GlobalIDL.USERcorbaNotifier._d_trigger, args)

    def sendMessage(self, *args):
        return _omnipy.invoke(self, "sendMessage", _0__GlobalIDL.USERcorbaNotifier._d_sendMessage, args)

    def id(self, *args):
        return _omnipy.invoke(self, "id", _0__GlobalIDL.USERcorbaNotifier._d_id, args)

    def deactivate(self, *args):
        return _omnipy.invoke(self, "deactivate", _0__GlobalIDL.USERcorbaNotifier._d_deactivate, args)

    def getEventType(self, *args):
        return _omnipy.invoke(self, "getEventType", _0__GlobalIDL.USERcorbaNotifier._d_getEventType, args)

    __methods__ = ["trigger", "sendMessage", "id", "deactivate", "getEventType"] + CORBA.Object.__methods__

omniORB.registerObjref(USERcorbaNotifier._NP_RepositoryId, _objref_USERcorbaNotifier)
_0__GlobalIDL._objref_USERcorbaNotifier = _objref_USERcorbaNotifier
del USERcorbaNotifier, _objref_USERcorbaNotifier

# USERcorbaNotifier skeleton
__name__ = "spell.lib.hifly.interface._GlobalIDL__POA"
class USERcorbaNotifier (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.USERcorbaNotifier._NP_RepositoryId


    _omni_op_d = {"trigger": _0__GlobalIDL.USERcorbaNotifier._d_trigger, "sendMessage": _0__GlobalIDL.USERcorbaNotifier._d_sendMessage, "id": _0__GlobalIDL.USERcorbaNotifier._d_id, "deactivate": _0__GlobalIDL.USERcorbaNotifier._d_deactivate, "getEventType": _0__GlobalIDL.USERcorbaNotifier._d_getEventType}

USERcorbaNotifier._omni_skeleton = USERcorbaNotifier
_0__GlobalIDL__POA.USERcorbaNotifier = USERcorbaNotifier
omniORB.registerSkeleton(USERcorbaNotifier._NP_RepositoryId, USERcorbaNotifier)
del USERcorbaNotifier
__name__ = "spell.lib.hifly.interface._GlobalIDL"

# interface USERcorbaNotificationSource
_0__GlobalIDL._d_USERcorbaNotificationSource = (omniORB.tcInternal.tv_objref, "IDL:USERcorbaNotificationSource:1.0", "USERcorbaNotificationSource")
omniORB.typeMapping["IDL:USERcorbaNotificationSource:1.0"] = _0__GlobalIDL._d_USERcorbaNotificationSource
_0__GlobalIDL.USERcorbaNotificationSource = omniORB.newEmptyClass()
class USERcorbaNotificationSource :
    _NP_RepositoryId = _0__GlobalIDL._d_USERcorbaNotificationSource[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.USERcorbaNotificationSource = USERcorbaNotificationSource
_0__GlobalIDL._tc_USERcorbaNotificationSource = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_USERcorbaNotificationSource)
omniORB.registerType(USERcorbaNotificationSource._NP_RepositoryId, _0__GlobalIDL._d_USERcorbaNotificationSource, _0__GlobalIDL._tc_USERcorbaNotificationSource)

# USERcorbaNotificationSource operations and attributes
USERcorbaNotificationSource._d_addNotifier = ((omniORB.typeMapping["IDL:USERcorbaNotifier:1.0"], (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:UserEventType:1.0"]), (), None)
USERcorbaNotificationSource._d_removeNotifier = (((omniORB.tcInternal.tv_string,0), ), None, None)
USERcorbaNotificationSource._d_id = ((), ((omniORB.tcInternal.tv_string,0), ), None)
USERcorbaNotificationSource._d_putTextMessage = (((omniORB.tcInternal.tv_string,0), ), None, None)

# USERcorbaNotificationSource object reference
class _objref_USERcorbaNotificationSource (CORBA.Object):
    _NP_RepositoryId = USERcorbaNotificationSource._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def addNotifier(self, *args):
        return _omnipy.invoke(self, "addNotifier", _0__GlobalIDL.USERcorbaNotificationSource._d_addNotifier, args)

    def removeNotifier(self, *args):
        return _omnipy.invoke(self, "removeNotifier", _0__GlobalIDL.USERcorbaNotificationSource._d_removeNotifier, args)

    def id(self, *args):
        return _omnipy.invoke(self, "id", _0__GlobalIDL.USERcorbaNotificationSource._d_id, args)

    def putTextMessage(self, *args):
        return _omnipy.invoke(self, "putTextMessage", _0__GlobalIDL.USERcorbaNotificationSource._d_putTextMessage, args)

    __methods__ = ["addNotifier", "removeNotifier", "id", "putTextMessage"] + CORBA.Object.__methods__

omniORB.registerObjref(USERcorbaNotificationSource._NP_RepositoryId, _objref_USERcorbaNotificationSource)
_0__GlobalIDL._objref_USERcorbaNotificationSource = _objref_USERcorbaNotificationSource
del USERcorbaNotificationSource, _objref_USERcorbaNotificationSource

# USERcorbaNotificationSource skeleton
__name__ = "spell.lib.hifly.interface._GlobalIDL__POA"
class USERcorbaNotificationSource (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.USERcorbaNotificationSource._NP_RepositoryId


    _omni_op_d = {"addNotifier": _0__GlobalIDL.USERcorbaNotificationSource._d_addNotifier, "removeNotifier": _0__GlobalIDL.USERcorbaNotificationSource._d_removeNotifier, "id": _0__GlobalIDL.USERcorbaNotificationSource._d_id, "putTextMessage": _0__GlobalIDL.USERcorbaNotificationSource._d_putTextMessage}

USERcorbaNotificationSource._omni_skeleton = USERcorbaNotificationSource
_0__GlobalIDL__POA.USERcorbaNotificationSource = USERcorbaNotificationSource
omniORB.registerSkeleton(USERcorbaNotificationSource._NP_RepositoryId, USERcorbaNotificationSource)
del USERcorbaNotificationSource
__name__ = "spell.lib.hifly.interface._GlobalIDL"

#
# End of module "_GlobalIDL"
#
__name__ = "spell.lib.hifly.interface.USERcorbaNotificationSource_idl"

_exported_modules = ( "spell.lib.hifly.interface._GlobalIDL", )

# The end.
