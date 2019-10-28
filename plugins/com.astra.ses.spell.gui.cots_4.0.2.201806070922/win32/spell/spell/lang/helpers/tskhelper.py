################################################################################

"""
(c) SES-ASTRA 2008

PACKAGE 
    spell.lang.helpers.tskhelper
FILE
    tmhelper.py
    
DESCRIPTION
    Helpers for task management wrapper functions. 
    
COPYRIGHT
    This software is the copyrighted work of SES ASTRA S.A.
    All rights reserved.
    
PROJECT
    UGCS/USL
    
AUTHOR
    Rafael Chinchilla Camara (GMV)
    
DATE
    04/12/2007
    
REVISION HISTORY
    04/12/2007    10:30    Creation
"""

################################################################################

#*******************************************************************************
# SPELL Imports
#*******************************************************************************
from spell.utils.log import *
from spell.lib.exception import *
from spell.lang.constants import *
from spell.lang.modifiers import *
from spell.lib.adapter.constants.core import *
from spell.lib.adapter.constants.notification import *
from spell.utils.ttime import TIME
from spell.lib.registry import *

#*******************************************************************************
# Local Imports
#*******************************************************************************
from basehelper import WrapperHelper

#*******************************************************************************
# System Imports
#*******************************************************************************


################################################################################
class StartTask_Helper(WrapperHelper):

    """
    DESCRIPTION:
        Helper for the StartTask wrapper.
    """    
    
    # Name of the process to be started
    _process = None
    _args = ""
    
    
    #===========================================================================
    def __init__(self):
        WrapperHelper.__init__(self, "TASK")
        self._process = None
        self._args = ""
        self._opName = "Start task" 

    #===========================================================================
    def _doStartTask(self):
        # Set in progress
        self._notifyValue( self._process, "", NOTIF_STATUS_PR, "Starting" )

        #TODO: merge with defaults

        result = REGISTRY['TASK'].startTask( self._process, self._args, self._config)

        if not result:        
            self._notifyValue( self._process, "", NOTIF_STATUS_FL, "Unable to start" )
        else:
            self._notifyValue( self._process, "", NOTIF_STATUS_OK, "Started" )
            
        return result
            
    #===========================================================================
    def _doOperation(self, *args, **kargs ):
        """
        DESCRIPTION:
            Start the given task with the given config
        
        ARGUMENTS:
            Expected arguments are:
                - Process name or command
                - Argument list
                
        RETURNS:
            True if success
            
        RAISES:
            DriverException if there is a problem in the driver layer
            SyntaxException if the process name is not given.
        """
        if len(args)==0:
            raise SyntaxException("No arguments given")
        
        # Get the process name
        self._process = args[0]
        if type(self._process)!=str:
            raise SyntaxException("Expected a string")
        
        if len(args)==2:
            # Get the process arguments
            self._args = args[1]
        else:
            self._args = ""
        
        result = self._doStartTask()
            
        return [False, result]

    #===========================================================================
    def _doRepeat(self):
        self._notifyValue( self._process, "", NOTIF_STATUS_FL, "Retrying")
        Display("Retry start " + self._process, level = WARNING )
        return [True, None]

    #===========================================================================
    def _doSkip(self):
        self._notifyValue( self.__process, "", NOTIF_STATUS_SP, "Skipped")
        Display("Skip start " + self._process, level = WARNING )
        return [False, None]
    
################################################################################
class StopTask_Helper(WrapperHelper):

    """
    DESCRIPTION:
        Helper for the StopTask wrapper.
    """    
    
    # Name of the process to be started
    _process = None
    
    #===========================================================================
    def __init__(self):
        WrapperHelper.__init__(self, "TASK")
        self._process = None
        self._opName = "Stop task" 
    
    #===========================================================================
    def _doOperation(self, *args, **kargs ):
        """
        DESCRIPTION:
            Start the given task with the given config
        
        ARGUMENTS:
            Expected arguments are:
                - Process name or command
                
        RETURNS:
            True if success
            
        RAISES:
            DriverException if there is a problem in the driver layer
            SyntaxException if the process name is not given.
        """
        
        if len(args)==0:
            raise SyntaxException("No arguments given")
        
        # Get the process name
        self._process = args[0]
        if type(self._process)!=str:
            raise SyntaxException("Expected a display name string")
        
        # Set in progress
        self._notifyValue( self._process, "", NOTIF_STATUS_PR, "Stopping" )

        result = REGISTRY['TASK'].stopTask( self._process, self._config)

        if not result:        
            self._notifyValue( self._process, "", NOTIF_STATUS_FL, "Cannot stop" )
        else:
            self._notifyValue( self._process, "", NOTIF_STATUS_OK, "Stopped" )
        
        return [False, True]

    #===========================================================================
    def _doRepeat(self):
        self._notifyValue( self._process, "", NOTIF_STATUS_FL, "Repeating")
        Display("Retry stop " + repr(self._process), WARNING )
        return [True, None]

    #===========================================================================
    def _doSkip(self):
        self._notifyValue( self._process, "", NOTIF_STATUS_SP, "Skipped")
        Display("Skip stop " + repr(self._process), WARNING )
        return [False, None]

################################################################################
class OpenDisplay_Helper(WrapperHelper):

    """
    DESCRIPTION:
        Helper for the OpenDisplay wrapper.
    """    
    __display = None
    
    #===========================================================================
    def __init__(self):
        WrapperHelper.__init__(self, "TASK")
        self.__display = None
        self._opName = "Open display" 
    
    #===========================================================================
    def _doOpenDisplay(self):
        # Set in progress
        self._notifyValue( self.__display, "", NOTIF_STATUS_PR, "Opening" )

        #TODO: merge with defaults

        result = REGISTRY['TASK'].openDisplay( self.__display, self._config)

        if not result:        
            self._notifyValue( self.__display, "", NOTIF_STATUS_FL, "Unable to open" )
        else:
            self._notifyValue( self.__display, "", NOTIF_STATUS_OK, "Open" )
            
        return result
    
    #===========================================================================
    def _doOperation(self, *args, **kargs ):
        # Parse arguments
        
        if len(args)==0:
            raise SyntaxException("No arguments given")
        elif len(args)==1:
            self.__display = args[0]
        else:
            raise SyntaxException("Bad number of arguments")

        if type(self.__display)!=str:
            raise SyntaxException("Expected a display name string")

        #TODO: more processing, this is demo only !!!
        
        result = self._doOpenDisplay()
        
        return [False,result]

################################################################################
class CloseDisplay_Helper(WrapperHelper):

    """
    DESCRIPTION:
        Helper for the CloseDisplay wrapper.
    """    
    __display = None
    
    #===========================================================================
    def __init__(self):
        WrapperHelper.__init__(self, "TASK")
        self.__display = None
        self._opName = "Close display" 
    
    #===========================================================================
    def _doCloseDisplay(self):
        # Set in progress
        self._notifyValue( self.__display, "", NOTIF_STATUS_PR, "Closing" )

        #TODO: merge with defaults

        result = REGISTRY['TASK'].closeDisplay( self.__display, self._config)

        if not result:
            self._notifyValue( self.__display, "", NOTIF_STATUS_FL, "Unable to start the task to close the display" )
            raise DriverException("Could not start the task to close the display")
        else:
            self._notifyValue( self.__display, "", NOTIF_STATUS_OK, "Close" )
            
        return result
    
    #===========================================================================
    def _doOperation(self, *args, **kargs ):
        # Parse arguments
        
        if len(args)==0:
            raise SyntaxException("No arguments given")
        elif len(args)==1:
            self.__display = args[0]
        else:
            raise SyntaxException("Bad number of arguments")

        if type(self.__display)!=str:
            raise SyntaxException("Expected a display name string")

        #TODO: more processing, this is demo only !!!
        
        result = self._doCloseDisplay()
        
        return [False,result]

    #===========================================================================
    def _doRepeat(self):
        self._write("Retry CloseDisplay", {Severity:WARNING} )
        return [True, True]

    #===========================================================================
    def _doSkip(self):
        self._write("CloseDisplay SKIPPED", {Severity:WARNING} )
        return [False, True]

################################################################################
class StartProc_Helper(WrapperHelper):

    """
    DESCRIPTION:
        Helper for the StartProc wrapper.
    """    
    __procId = None
    __arguments = {}
    __result = False
    __status = None
    
    #===========================================================================
    def __init__(self):
        WrapperHelper.__init__(self, "TASK")
        self.__procId = None
        self.__arguments = {}
        self.__result = False
        self.__status = None

    #===========================================================================
    def _doPreOperation(self, *args, **kargs ):
        if len(args)!=1:
            raise SyntaxException("Bad arguments, should provide procedure identifier")

        self.__procId = args[0]

        if type(self.__procId)!=str:
            raise SyntaxException("Expected a procedure identifier")

        # Parse arguments for the procedure
        self.__arguments = {}
        if 'args' in kargs:
            defs = kargs['args']
            if type(defs) != list:
                raise SyntaxException("Expected a list of arguments")
            for argument in defs:
                if type(argument)!=list or len(argument)!=2:
                    raise SyntaxException("Wrong argument format, expected a list of 2 elements")
                argName = argument[0]
                argValue = argument[1]
                self.__arguments[argName] = argValue 
    
    #===========================================================================
    def _doOperation(self, *args, **kargs ):
        
        automatic = self.getConfig(Automatic)
        blocking = self.getConfig(Blocking)
        visible = self.getConfig(Visible)
        
        msg = "Starting procedure " + self.__procId + " (Automatic:"\
              + str(automatic) + ", Blocking:" + str(blocking) \
              + ", Visible: " + str(visible) + ")"
        self._write(msg)
        
        self._notifyValue("Procedure", self.__procId, NOTIF_STATUS_PR, "Loading procedure")
        
        # Open the procedure (will raise exception on failure)    
        self.__result = REGISTRY['EXEC'].openSubProcedure(self.__procId,
                                          self.__arguments, 
                                          config = self.getConfig() )

        self.__status = REGISTRY['EXEC'].getChildStatus()

        if REGISTRY['EXEC'].isChildError():
            error,reason = REGISTRY['EXEC'].getChildError()
            raise DriverException(error,reason)
        
        self._notifyValue("Procedure", self.__procId, self.__status, "Procedure loaded")

        # If the child procedure is started in blocking mode we shall monitor
        # it until it reaches the status ERROR/ABORTED/FINISHED. Otherwise,
        # we finish right away.
        if blocking == True:
            # Start the time condition wait
            self._startWait( self.monitor_callback )
            # Wait the procedure to finish
            self._wait()

        if self.__result == True:
            if blocking:
                self._notifyValue("Procedure", self.__procId, NOTIF_STATUS_OK, "Execution finished")
            else:
                self._notifyValue("Procedure", self.__procId, NOTIF_STATUS_OK, "Procedure started")
        else:
            self._notifyValue("Procedure", self.__procId, NOTIF_STATUS_FL, "Execution failed")
            error,reason = REGISTRY['EXEC'].getChildError()
            raise DriverException(error,reason)
                  
        return [False,self.__result]

    #===========================================================================
    def _doPostOperation(self, *args, **kargs):
        REGISTRY['EXEC'].killSubProcedure()

    #===========================================================================
    def monitor_callback(self):
        self.__status = REGISTRY['EXEC'].getChildStatus()
        if REGISTRY['EXEC'].isChildFinished(): 
            self.__result = True
            return True
        elif REGISTRY['EXEC'].isChildError(): 
            self.__result = False
            return True
        self._notifyValue("Procedure", self.__procId, str(self.__status), "Execution ongoing")
        return False
        
    #===========================================================================
    def _doRepeat(self):
        self._notifyValue( "Procedure", self.__procId, NOTIF_STATUS_PR, "Reloading")
        REGISTRY['EXEC'].killSubProcedure()
        return [True, None]

    #===========================================================================
    def _doSkip(self):
        self._notifyValue( "Procedure", self.__procId, NOTIF_STATUS_SP, "Skipped")
        REGISTRY['EXEC'].killSubProcedure()
        return [False, None]

    #===========================================================================
    def _doCancel(self):
        self._notifyValue( "Procedure", self.__procId, NOTIF_STATUS_SP, "Cancelled")
        REGISTRY['EXEC'].killSubProcedure()
        return [False, None]
        
################################################################################
class PrintDisplay_Helper(WrapperHelper):

    """
    DESCRIPTION:
        Helper for the PrintDisplay wrapper.
    """    
    __display = None
    
    #===========================================================================
    def __init__(self):
        WrapperHelper.__init__(self)
        self.__display = None
        self._opName = "Print display" 
    
    #===========================================================================
    def _doPrintDisplay(self):
        # Set in progress
        self._notifyValue( self.__display, "", NOTIF_STATUS_PR, "Printing" )

        #TODO: merge with defaults

        result = REGISTRY['TASK'].printDisplay( self.__display, self._config)

        if not result:        
            self._notifyValue( self.__display, "", NOTIF_STATUS_FL, "Unable to print" )
        else:
            self._notifyValue( self.__display, "", NOTIF_STATUS_OK, "Printed" )
            
        return result
    
    #===========================================================================
    def _doOperation(self, *args, **kargs ):
        # Parse arguments
        
        if len(args)==0:
            raise SyntaxException("No arguments given")
        elif len(args)==1:
            self.__display = args[0]
        else:
            raise SyntaxException("Bad number of arguments")

        if type(self.__display)!=str:
            raise SyntaxException("Expected a display name string")

        #TODO: more processing, this is demo only !!!
        
        result = self._doPrintDisplay()
        
        return [False,result]
