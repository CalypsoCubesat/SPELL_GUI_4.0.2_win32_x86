# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _ITC
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


LIST = _ITC.LIST
SINGLE = _ITC.SINGLE
PARAMETERS = _ITC.PARAMETERS
NOERROR = _ITC.NOERROR
ERROR = _ITC.ERROR
NOK = _ITC.NOK
OK = _ITC.OK
SKIP = _ITC.SKIP
SERVER_DOWN = _ITC.SERVER_DOWN
CHSERVER_DOWN = _ITC.CHSERVER_DOWN
class Callback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Callback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Callback, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _ITC.delete_Callback
    __del__ = lambda self : None;
    def report(*args): return _ITC.Callback_report(*args)
    def userInput(*args): return _ITC.Callback_userInput(*args)
    def FillCmdsFromList(*args): return _ITC.Callback_FillCmdsFromList(*args)
    def __init__(self, *args): 
        if self.__class__ == Callback:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _ITC.new_Callback(*args)
        try: self.this.append(this)
        except: self.this = this
    def __disown__(self):
        self.this.disown()
        _ITC.disown_Callback(self)
        return weakref_proxy(self)
Callback_swigregister = _ITC.Callback_swigregister
Callback_swigregister(Callback)

class STC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, STC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, STC, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cmdlistname"] = _ITC.STC_cmdlistname_set
    __swig_getmethods__["cmdlistname"] = _ITC.STC_cmdlistname_get
    if _newclass:cmdlistname = _swig_property(_ITC.STC_cmdlistname_get, _ITC.STC_cmdlistname_set)
    __swig_setmethods__["cmdMnemonic"] = _ITC.STC_cmdMnemonic_set
    __swig_getmethods__["cmdMnemonic"] = _ITC.STC_cmdMnemonic_get
    if _newclass:cmdMnemonic = _swig_property(_ITC.STC_cmdMnemonic_get, _ITC.STC_cmdMnemonic_set)
    __swig_setmethods__["scname"] = _ITC.STC_scname_set
    __swig_getmethods__["scname"] = _ITC.STC_scname_get
    if _newclass:scname = _swig_property(_ITC.STC_scname_get, _ITC.STC_scname_set)
    __swig_setmethods__["display"] = _ITC.STC_display_set
    __swig_getmethods__["display"] = _ITC.STC_display_get
    if _newclass:display = _swig_property(_ITC.STC_display_get, _ITC.STC_display_set)
    __swig_setmethods__["cmdlist"] = _ITC.STC_cmdlist_set
    __swig_getmethods__["cmdlist"] = _ITC.STC_cmdlist_get
    if _newclass:cmdlist = _swig_property(_ITC.STC_cmdlist_get, _ITC.STC_cmdlist_set)
    __swig_setmethods__["cmdlistcnt"] = _ITC.STC_cmdlistcnt_set
    __swig_getmethods__["cmdlistcnt"] = _ITC.STC_cmdlistcnt_get
    if _newclass:cmdlistcnt = _swig_property(_ITC.STC_cmdlistcnt_get, _ITC.STC_cmdlistcnt_set)
    __swig_setmethods__["nitems"] = _ITC.STC_nitems_set
    __swig_getmethods__["nitems"] = _ITC.STC_nitems_get
    if _newclass:nitems = _swig_property(_ITC.STC_nitems_get, _ITC.STC_nitems_set)
    __swig_setmethods__["list_or_single"] = _ITC.STC_list_or_single_set
    __swig_getmethods__["list_or_single"] = _ITC.STC_list_or_single_get
    if _newclass:list_or_single = _swig_property(_ITC.STC_list_or_single_get, _ITC.STC_list_or_single_set)
    __swig_setmethods__["retCode"] = _ITC.STC_retCode_set
    __swig_getmethods__["retCode"] = _ITC.STC_retCode_get
    if _newclass:retCode = _swig_property(_ITC.STC_retCode_get, _ITC.STC_retCode_set)
    __swig_setmethods__["mc"] = _ITC.STC_mc_set
    __swig_getmethods__["mc"] = _ITC.STC_mc_get
    if _newclass:mc = _swig_property(_ITC.STC_mc_get, _ITC.STC_mc_set)
    __swig_setmethods__["client"] = _ITC.STC_client_set
    __swig_getmethods__["client"] = _ITC.STC_client_get
    if _newclass:client = _swig_property(_ITC.STC_client_get, _ITC.STC_client_set)
    __swig_setmethods__["chs"] = _ITC.STC_chs_set
    __swig_getmethods__["chs"] = _ITC.STC_chs_get
    if _newclass:chs = _swig_property(_ITC.STC_chs_get, _ITC.STC_chs_set)
    def __init__(self, *args): 
        this = _ITC.new_STC(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ITC.delete_STC
    __del__ = lambda self : None;
    def Initialize(*args): return _ITC.STC_Initialize(*args)
    def Release(*args): return _ITC.STC_Release(*args)
    def Reset(*args): return _ITC.STC_Reset(*args)
    def SendCommand(*args): return _ITC.STC_SendCommand(*args)
    def Send(*args): return _ITC.STC_Send(*args)
    def SendM(*args): return _ITC.STC_SendM(*args)
    def SendP(*args): return _ITC.STC_SendP(*args)
    def SendDP(*args): return _ITC.STC_SendDP(*args)
    def sendPing(*args): return _ITC.STC_sendPing(*args)
    def connect(*args): return _ITC.STC_connect(*args)
    def connectCHServer(*args): return _ITC.STC_connectCHServer(*args)
    def clearUp(*args): return _ITC.STC_clearUp(*args)
    def delCallback(*args): return _ITC.STC_delCallback(*args)
    __swig_getmethods__["setCallback"] = lambda x: _ITC.STC_setCallback
    if _newclass:setCallback = staticmethod(_ITC.STC_setCallback)
STC_swigregister = _ITC.STC_swigregister
STC_swigregister(STC)
cvar = _ITC.cvar
STC_setCallback = _ITC.STC_setCallback

class STAR2_TC(STC):
    __swig_setmethods__ = {}
    for _s in [STC]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, STAR2_TC, name, value)
    __swig_getmethods__ = {}
    for _s in [STC]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, STAR2_TC, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ITC.new_STAR2_TC(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ITC.delete_STAR2_TC
    __del__ = lambda self : None;
    def Send(*args): return _ITC.STAR2_TC_Send(*args)
    def SendP(*args): return _ITC.STAR2_TC_SendP(*args)
    def SendDP(*args): return _ITC.STAR2_TC_SendDP(*args)
STAR2_TC_swigregister = _ITC.STAR2_TC_swigregister
STAR2_TC_swigregister(STAR2_TC)

class A2100_TC(STC):
    __swig_setmethods__ = {}
    for _s in [STC]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, A2100_TC, name, value)
    __swig_getmethods__ = {}
    for _s in [STC]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, A2100_TC, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ITC.new_A2100_TC(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ITC.delete_A2100_TC
    __del__ = lambda self : None;
    def Send(*args): return _ITC.A2100_TC_Send(*args)
    def SendDWL(*args): return _ITC.A2100_TC_SendDWL(*args)
    def SendM(*args): return _ITC.A2100_TC_SendM(*args)
    def SendP(*args): return _ITC.A2100_TC_SendP(*args)
    def SendDP(*args): return _ITC.A2100_TC_SendDP(*args)
A2100_TC_swigregister = _ITC.A2100_TC_swigregister
A2100_TC_swigregister(A2100_TC)

class TMCallback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TMCallback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TMCallback, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _ITC.delete_TMCallback
    __del__ = lambda self : None;
    def report(*args): return _ITC.TMCallback_report(*args)
    def __init__(self, *args): 
        this = _ITC.new_TMCallback(*args)
        try: self.this.append(this)
        except: self.this = this
TMCallback_swigregister = _ITC.TMCallback_swigregister
TMCallback_swigregister(TMCallback)

class Limit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Limit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Limit, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ITC.new_Limit(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ITC.delete_Limit
    __del__ = lambda self : None;
    def Initialize(*args): return _ITC.Limit_Initialize(*args)
    def CheckTPU(*args): return _ITC.Limit_CheckTPU(*args)
    def Analog(*args): return _ITC.Limit_Analog(*args)
    def Discrete(*args): return _ITC.Limit_Discrete(*args)
    def TempFile(*args): return _ITC.Limit_TempFile(*args)
    def Normal(*args): return _ITC.Limit_Normal(*args)
    def CleanUp(*args): return _ITC.Limit_CleanUp(*args)
    def delCallback(*args): return _ITC.Limit_delCallback(*args)
    def setCallback(*args): return _ITC.Limit_setCallback(*args)
Limit_swigregister = _ITC.Limit_swigregister
Limit_swigregister(Limit)


