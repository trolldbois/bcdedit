# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 Loic Jaquemet loic.jaquemet+python@gmail.com
#

import haystack
from haystack.model import LoadableMembersStructure,RangeValue,NotNull,CString
import ctypes


ULONG = ctypes.c_uint

class BcdElementType(LoadableMembersStructure):
  _fields_ = [
    ('SubType', ULONG, 24),
    ('Format', ULONG, 4),
    ('Class', ULONG, 4),
]


BcdElementType.expectedValues = {
  'Format': RangeValue(1,7),
  'Class': [1,2,3,5]
  }


#class BcdElementType(LoadableMembersStructure):
#  _fields_ = [
#    ('SubType', ULONG, 24),
#    ('Format', ULONG, 4),
#    ('Class', ULONG, 4),
#]


#http://msdn.microsoft.com/en-us/library/windows/desktop/aa362641(v=vs.85).aspx
ELEMENT_TYPES_BOOT = {
  0x24000001: 'DisplayOrder',
  0x24000002: 'BootSequence',
  0x23000003: 'DefaultObject', 
  0x25000004: 'Timeout',
  0x26000005: 'AttemptResume',
  0x23000006: 'ResumeObject',
  0x24000010: 'ToolsDisplayOrder',
  0x21000022: 'BcdDevice',
  0x22000023: 'BcdFilePath', 
}

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa362645(v=vs.85).aspx
ELEMENT_TYPES_DEVICE = {
  0x35000001: 'RamdiskImageOffset',
  0x35000002: 'TftpClientPort',
  0x31000003: 'SdiDevice',
  0x32000004: 'SdiPath',
  0x35000005: 'RamdiskImageLength',
}

#http://msdn.microsoft.com/en-us/library/windows/desktop/aa362652(v=vs.85).aspx
ELEMENT_TYPES_LIBRARY = {
  0x11000001: 'ApplicationDevice',
  0x12000002: 'ApplicationPath',
  0x12000004: 'Description',
  0x12000005: 'PreferredLocale',
  0x14000006: 'InheritedObjects',
  0x15000007: 'TruncatePhysicalMemory',
  0x14000008: 'RecoverySequence',
  0x16000009: 'AutoRecoveryEnabled',
  0x1700000a: 'BadMemoryList',
  0x1600000b: 'AllowBadMemoryAccess',
  0x1500000c: 'FirstMegabytePolicy',
  0x16000010: 'DebuggerEnabled',
  0x15000011: 'DebuggerType',
  0x15000012: 'SerialDebuggerPortAddress',
  0x15000013: 'SerialDebuggerPort',
  0x15000014: 'SerialDebuggerBaudRate',
  0x15000015: '1394DebuggerChannel',
  0x12000016: 'UsbDebuggerTargetName',
  0x16000017: 'DebuggerIgnoreUsermodeExceptions',
  0x15000018: 'DebuggerStartPolicy',
  0x16000020: 'EmsEnabled',
  0x15000022: 'EmsPort',
  0x15000023: 'EmsBaudRate',
  0x12000030: 'LoadOptionsString',
  0x16000040: 'DisplayAdvancedOptions',
  0x16000041: 'DisplayOptionsEdit',
  0x16000046: 'GraphicsModeDisabled',
  0x15000047: 'ConfigAccessPolicy',
  0x16000049: 'AllowPrereleaseSignatures', 
}

#http://msdn.microsoft.com/en-us/library/windows/desktop/aa362659(v=vs.85).aspx
ELEMENT_TYPES_MEMDIAG = {
  0x25000001: 'PassCount',
  0x25000003: 'FailureCount', 
}


#http://msdn.microsoft.com/en-us/library/windows/desktop/aa362670%28v=vs.85%29.aspx
ELEMENT_TYPES_LOADER = {
  0x21000001: 'OSDevice',
  0x22000002: 'SystemRoot',
  0x23000003: 'AssociatedResumeObject',
  0x26000010: 'DetectKernelAndHal',
  0x22000011: 'KernelPath',
  0x22000012: 'HalPath',
  0x22000013: 'DbgTransportPath',
  0x25000020: 'NxPolicy',
  0x25000021: 'PAEPolicy',
  0x26000022: 'WinPEMode',
  0x26000024: 'DisableCrashAutoReboot',
  0x26000025: 'UseLastGoodSettings',
  0x26000027: 'AllowPrereleaseSignatures',
  0x26000030: 'NoLowMemory',
  0x25000031: 'RemoveMemory',
  0x25000032: 'IncreaseUserVa',
  0x26000040: 'UseVgaDriver',
  0x26000041: 'DisableBootDisplay',
  0x26000042: 'DisableVesaBios',
  0x25000050: 'ClusterModeAddressing',
  0x26000051: 'UsePhysicalDestination',
  0x25000052: 'RestrictApicCluster',
  0x26000060: 'UseBootProcessorOnly',
  0x25000061: 'NumberOfProcessors',
  0x26000062: 'ForceMaximumProcessors',
  0x25000063: 'ProcessorConfigurationFlags',
  0x26000070: 'UseFirmwarePciSettings',
  0x26000071: 'MsiPolicy',
  0x25000080: 'SafeBoot',
  0x26000081: 'SafeBootAlternateShell',
  0x26000090: 'BootLogInitialization',
  0x26000091: 'VerboseObjectLoadMode',
  0x260000a0: 'KernelDebuggerEnabled',
  0x260000a1: 'DebuggerHalBreakpoint',
  0x260000b0: 'EmsEnabled',
  0x250000c1: 'DriverLoadFailurePolicy',
  0x250000E0: 'BootStatusPolicy', 
}


ELEMENT_TYPES = dict()
ELEMENT_TYPES.update(ELEMENT_TYPES_BOOT)
ELEMENT_TYPES.update(ELEMENT_TYPES_DEVICE)
ELEMENT_TYPES.update(ELEMENT_TYPES_LIBRARY)
ELEMENT_TYPES.update(ELEMENT_TYPES_MEMDIAG)
ELEMENT_TYPES.update(ELEMENT_TYPES_LOADER)

def type_desc(x):
  if x in ELEMENT_TYPES:
    return ELEMENT_TYPES[x]
  else:
    return 'Unknown Type'

def object_code(i):
  return int('{:0>32b}'.format(i)[:4],2)

# BCD.docx , page 7: BCD Objects
_EL_OBJECT_CODE = {
  0x1: 'Application',
  0x2: 'Inheritable',
  0x3: 'Device',
}

def object_code_desc(i):
  return _EL_OBJECT_CODE[object_code(i)]
    
  
# BCD.docx , page 9: Standard application Objects
GUIDS = {
  '9dea862c-5cdd-4e70-acc1-f32b344d4795': ['Windows Boot Manager','{bootmgr}'],
  'a5a30fa2-3d06-4e9f-b5f4-a01df9d1fcba': ['Firmware Boot Manager','{fwbootmgr}'],
  'b2721d73-1db4-4c62-bf78-c548a880142d': ['Windows Memory Tester','{memdiag}'],
  '147aa509-0358-4473-b83b-d950dda00615': ['Windows Resume Application','No alias'],
  '466f5a88-0af2-4f76-9038-095b170dc21c': ['Legacy Windows Loader','{ntldr}'],
  'fa926493-6f1c-4193-a414-58f0b2456d1e': ['Current boot entry','{current}'],
  '': ['Default boot entry','{default}'],
}

def guid_desc(g):
  if g in GUIDS:
    return GUIDS[g]
  else:
    return 'Unknown GUID'


