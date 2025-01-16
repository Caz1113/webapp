# -*- coding: utf-8 -*-

import platform
import struct
import sys
from ctypes import (
    CFUNCTYPE,
    POINTER,
    ArgumentError,
    Structure,
    alignment,
    byref,
    c_bool,
    c_buffer,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_float,
    c_int,
    c_int8,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_longdouble,
    c_longlong,
    c_short,
    c_size_t,
    c_ubyte,
    c_uint,
    c_uint8,
    c_uint32,
    c_ulong,
    c_ulonglong,
    c_ushort,
    c_void_p,
    c_wchar,
    cast,
    cdll,
    py_object,
    sizeof,
    util,
)

# Based on Pyglet code

##############################################################################
# cocoatypes.py

__LP64__ = ...
__i386__ = ...

PyObjectEncoding: str = ...

def encoding_for_ctype(vartype): ...

NSIntegerEncoding = ...
NSUIntegerEncoding = ...
CGFloatEncoding = ...

CGImageEncoding: str = ...
NSZoneEncoding: str = ...

class NSPoint(Structure):
    _fields_: list = ...

CGPoint = NSPoint

class NSSize(Structure):
    _fields_: list = ...

CGSize = NSSize

class NSRect(Structure):
    _fields_: list = ...

CGRect = NSRect

NSTimeInterval = ...
CFIndex = ...
UniChar = ...
unichar = ...
CGGlyph = ...

class CFRange(Structure):
    _fields_: list = ...

class NSRange(Structure):
    _fields_: list = ...

CFTypeID = ...
CFNumberType = ...

##############################################################################
# runtime.py

__LP64__ = ...
__i386__ = ...

objc = ...

objc.class_addIvar.restype = ...
objc.class_addIvar.argtypes = ...

objc.class_addMethod.restype = ...

objc.class_addProtocol.restype = ...
objc.class_addProtocol.argtypes = ...

objc.class_conformsToProtocol.restype = ...
objc.class_conformsToProtocol.argtypes = ...

objc.class_copyIvarList.restype = ...
objc.class_copyIvarList.argtypes = ...

objc.class_copyMethodList.restype = ...
objc.class_copyMethodList.argtypes = ...

objc.class_copyPropertyList.restype = ...
objc.class_copyPropertyList.argtypes = ...

objc.class_copyProtocolList.restype = ...
objc.class_copyProtocolList.argtypes = ...

objc.class_createInstance.restype = ...
objc.class_createInstance.argtypes = ...

objc.class_getClassMethod.restype = ...
objc.class_getClassMethod.argtypes = ...

objc.class_getClassVariable.restype = ...
objc.class_getClassVariable.argtypes = ...

objc.class_getInstanceMethod.restype = ...
objc.class_getInstanceMethod.argtypes = ...

objc.class_getInstanceSize.restype = ...
objc.class_getInstanceSize.argtypes = ...

objc.class_getInstanceVariable.restype = ...
objc.class_getInstanceVariable.argtypes = ...

objc.class_getIvarLayout.restype = ...
objc.class_getIvarLayout.argtypes = ...

objc.class_getMethodImplementation.restype = ...
objc.class_getMethodImplementation.argtypes = ...

objc.class_getName.restype = ...
objc.class_getName.argtypes = ...

objc.class_getProperty.restype = ...
objc.class_getProperty.argtypes = ...

objc.class_getSuperclass.restype = ...
objc.class_getSuperclass.argtypes = ...

objc.class_getVersion.restype = ...
objc.class_getVersion.argtypes = ...

objc.class_getWeakIvarLayout.restype = ...
objc.class_getWeakIvarLayout.argtypes = ...

objc.class_isMetaClass.restype = ...
objc.class_isMetaClass.argtypes = ...

objc.class_replaceMethod.restype = ...
objc.class_replaceMethod.argtypes = ...

objc.class_respondsToSelector.restype = ...
objc.class_respondsToSelector.argtypes = ...

objc.class_setIvarLayout.restype = ...
objc.class_setIvarLayout.argtypes = ...

objc.class_setSuperclass.restype = ...
objc.class_setSuperclass.argtypes = ...

objc.class_setVersion.restype = ...
objc.class_setVersion.argtypes = ...

objc.class_setWeakIvarLayout.restype = ...
objc.class_setWeakIvarLayout.argtypes = ...

objc.ivar_getName.restype = ...
objc.ivar_getName.argtypes = ...

objc.ivar_getOffset.restype = ...
objc.ivar_getOffset.argtypes = ...

objc.ivar_getTypeEncoding.restype = ...
objc.ivar_getTypeEncoding.argtypes = ...

objc.method_copyArgumentType.restype = ...
objc.method_copyArgumentType.argtypes = ...

objc.method_copyReturnType.restype = ...
objc.method_copyReturnType.argtypes = ...

objc.method_exchangeImplementations.restype = ...
objc.method_exchangeImplementations.argtypes = ...

objc.method_getArgumentType.restype = ...
objc.method_getArgumentType.argtypes = ...

objc.method_getImplementation.restype = ...
objc.method_getImplementation.argtypes = ...

objc.method_getName.restype = ...
objc.method_getName.argtypes = ...

objc.method_getNumberOfArguments.restype = ...
objc.method_getNumberOfArguments.argtypes = ...

objc.method_getReturnType.restype = ...
objc.method_getReturnType.argtypes = ...

objc.method_getTypeEncoding.restype = ...
objc.method_getTypeEncoding.argtypes = ...

objc.method_setImplementation.restype = ...
objc.method_setImplementation.argtypes = ...

objc.objc_allocateClassPair.restype = ...
objc.objc_allocateClassPair.argtypes = ...

objc.objc_copyProtocolList.restype = ...
objc.objc_copyProtocolList.argtypes = ...

objc.objc_getAssociatedObject.restype = ...
objc.objc_getAssociatedObject.argtypes = ...

objc.objc_getClass.restype = ...
objc.objc_getClass.argtypes = ...

objc.objc_getClassList.restype = ...
objc.objc_getClassList.argtypes = ...

objc.objc_getMetaClass.restype = ...
objc.objc_getMetaClass.argtypes = ...

objc.objc_getProtocol.restype = ...
objc.objc_getProtocol.argtypes = ...

objc.objc_registerClassPair.restype = ...
objc.objc_registerClassPair.argtypes = ...

objc.objc_removeAssociatedObjects.restype = ...
objc.objc_removeAssociatedObjects.argtypes = ...

objc.objc_setAssociatedObject.restype = ...
objc.objc_setAssociatedObject.argtypes = ...

objc.object_copy.restype = ...
objc.object_copy.argtypes = ...

objc.object_dispose.restype = ...
objc.object_dispose.argtypes = ...

objc.object_getClass.restype = ...
objc.object_getClass.argtypes = ...

objc.object_getClassName.restype = ...
objc.object_getClassName.argtypes = ...

objc.object_getInstanceVariable.restype = ...
objc.object_getInstanceVariable.argtypes = ...

objc.object_getIvar.restype = ...
objc.object_getIvar.argtypes = ...

objc.object_setClass.restype = ...
objc.object_setClass.argtypes = ...

objc.object_setInstanceVariable.restype = ...

objc.object_setIvar.restype = ...
objc.object_setIvar.argtypes = ...

objc.property_getAttributes.restype = ...
objc.property_getAttributes.argtypes = ...

objc.property_getName.restype = ...
objc.property_getName.argtypes = ...

objc.protocol_conformsToProtocol.restype = ...
objc.protocol_conformsToProtocol.argtypes = ...

class OBJC_METHOD_DESCRIPTION(Structure):
    _fields_ = ...

objc.protocol_copyMethodDescriptionList.restype = ...
objc.protocol_copyMethodDescriptionList.argtypes = ...

objc.protocol_copyPropertyList.restype = ...
objc.protocol_copyPropertyList.argtypes = ...

objc.protocol_copyProtocolList = ...
objc.protocol_copyProtocolList.argtypes = ...

objc.protocol_getMethodDescription.restype = OBJC_METHOD_DESCRIPTION
objc.protocol_getMethodDescription.argtypes = ...

objc.protocol_getName.restype = ...
objc.protocol_getName.argtypes = ...

objc.sel_getName.restype = ...
objc.sel_getName.argtypes = ...

objc.sel_isEqual.restype = ...
objc.sel_isEqual.argtypes = ...

objc.sel_registerName.restype = ...
objc.sel_registerName.argtypes = ...

def ensure_bytes(x): ...
def get_selector(name): ...
def get_class(name): ...
def get_object_class(obj): ...
def get_metaclass(name): ...
def get_superclass_of_object(obj): ...
def x86_should_use_stret(restype): ...
def should_use_fpret(restype): ...
def send_message(receiver, selName, *args, **kwargs): ...

class OBJC_SUPER(Structure):
    _fields_: list = ...

OBJC_SUPER_PTR = ...

def send_super(receiver, selName, *args, **kwargs): ...

cfunctype_table: dict = ...

def parse_type_encoding(encoding): ...
def cfunctype_for_encoding(encoding): ...
def create_subclass(superclass, name): ...
def register_subclass(subclass): ...
def add_method(cls, selName, method, types): ...
def add_ivar(cls, name, vartype): ...
def set_instance_variable(obj, varname, value, vartype): ...
def get_instance_variable(obj, varname, vartype): ...

class ObjCMethod(object):
    typecodes: dict = ...
    cfunctype_table: dict = ...

    def __init__(self, method): ...
    def ctype_for_encoding(self, encoding): ...
    def get_prototype(self): ...
    def __repr__(self): ...
    def get_callable(self): ...
    def __call__(self, objc_id, *args): ...

class ObjCBoundMethod(object):
    def __init__(self, method, objc_id): ...
    def __repr__(self): ...
    def __call__(self, *args): ...

class ObjCClass(object):
    _registered_classes: dict = ...

    def __new__(cls, class_name_or_ptr): ...
    def __repr__(self): ...
    def cache_instance_methods(self): ...
    def cache_class_methods(self): ...
    def get_instance_method(self, name): ...
    def get_class_method(self, name): ...
    def __getattr__(self, name): ...

class ObjCInstance(object):
    _cached_objects: dict = ...

    def __new__(cls, object_ptr): ...
    def __repr__(self): ...
    def __getattr__(self, name): ...

def convert_method_arguments(encoding, args): ...

class ObjCSubclass(object):
    def __init__(self, superclass, name, register=True): ...
    def register(self): ...
    def add_ivar(self, varname, vartype): ...
    def add_method(self, method, name, encoding): ...
    def add_class_method(self, method, name, encoding): ...
    def rawmethod(self, encoding): ...
    def method(self, encoding): ...
    def classmethod(self, encoding): ...

# XXX This causes segfaults in all backends (yikes!), and makes it so that
# pyglet can't even be loaded. We'll just have to live with leaks for now,
# which is probably alright since we only use the
# NSFontManager.sharedFontManager class currently.

# class DeallocationObserver_Implementation(object):
#    DeallocationObserver = ObjCSubclass('NSObject', 'DeallocationObserver',
#                                        register=False)
#    DeallocationObserver.add_ivar('observed_object', c_void_p)
#    DeallocationObserver.register()
#
#    @DeallocationObserver.rawmethod('@@')
#    def initWithObject_(self, cmd, anObject):
#        self = send_super(self, 'init')
#        self = self.value
#        set_instance_variable(self, 'observed_object', anObject, c_void_p)
#        return self
#
#    @DeallocationObserver.rawmethod('v')
#    def dealloc(self, cmd):
#        anObject = get_instance_variable(self, 'observed_object', c_void_p)
#        ObjCInstance._cached_objects.pop(anObject, None)
#        send_super(self, 'dealloc')
#
#    @DeallocationObserver.rawmethod('v')
#    def finalize(self, cmd):
#        anObject = get_instance_variable(self, 'observed_object', c_void_p)
#        ObjCInstance._cached_objects.pop(anObject, None)
#        send_super(self, 'finalize')

##############################################################################
# cocoalibs.py

cf = ...

kCFStringEncodingUTF8: int = ...

CFAllocatorRef = ...
CFStringEncoding = ...

cf.CFStringCreateWithCString.restype = ...
cf.CFStringCreateWithCString.argtypes = ...

cf.CFRelease.restype = ...
cf.CFRelease.argtypes = ...

cf.CFStringGetLength.restype = ...
cf.CFStringGetLength.argtypes = ...

cf.CFStringGetMaximumSizeForEncoding.restype = ...
cf.CFStringGetMaximumSizeForEncoding.argtypes = ...

cf.CFStringGetCString.restype = ...
cf.CFStringGetCString.argtypes = ...

cf.CFStringGetTypeID.restype = ...
cf.CFStringGetTypeID.argtypes = ...

cf.CFAttributedStringCreate.restype = ...
cf.CFAttributedStringCreate.argtypes = ...

cf.CFURLCreateWithFileSystemPath.restype = ...
cf.CFURLCreateWithFileSystemPath.argtypes = ...

def CFSTR(string): ...
def get_NSString(string): ...
def cfstring_to_string(cfstring): ...

cf.CFDataCreate.restype = ...
cf.CFDataCreate.argtypes = ...

cf.CFDataGetBytes.restype = ...
cf.CFDataGetBytes.argtypes = ...

cf.CFDataGetLength.restype = ...
cf.CFDataGetLength.argtypes = ...

cf.CFDictionaryGetValue.restype = ...
cf.CFDictionaryGetValue.argtypes = ...

cf.CFDictionaryAddValue.restype = ...
cf.CFDictionaryAddValue.argtypes = ...

cf.CFDictionaryCreateMutable.restype = ...
cf.CFDictionaryCreateMutable.argtypes = ...

cf.CFNumberCreate.restype = ...
cf.CFNumberCreate.argtypes = ...

cf.CFNumberGetType.restype = ...
cf.CFNumberGetType.argtypes = ...

cf.CFNumberGetValue.restype = ...
cf.CFNumberGetValue.argtypes = ...

cf.CFNumberGetTypeID.restype = ...
cf.CFNumberGetTypeID.argtypes = ...

cf.CFGetTypeID.restype = ...
cf.CFGetTypeID.argtypes = ...

# CFNumber.h
kCFNumberSInt8Type: int = ...
kCFNumberSInt16Type: int = ...
kCFNumberSInt32Type: int = ...
kCFNumberSInt64Type: int = ...
kCFNumberFloat32Type: int = ...
kCFNumberFloat64Type: int = ...
kCFNumberCharType: int = ...
kCFNumberShortType: int = ...
kCFNumberIntType: int = ...
kCFNumberLongType: int = ...
kCFNumberLongLongType: int = ...
kCFNumberFloatType: int = ...
kCFNumberDoubleType: int = ...
kCFNumberCFIndexType: int = ...
kCFNumberNSIntegerType: int = ...
kCFNumberCGFloatType: int = ...
kCFNumberMaxType: int = ...

def cfnumber_to_number(cfnumber): ...

# Dictionary of cftypes matched to the method converting them to python values.
known_cftypes: dict = ...

def cftype_to_value(cftype): ...

cf.CFSetGetCount.restype = ...
cf.CFSetGetCount.argtypes = ...

cf.CFSetGetValues.restype = ...
# PyPy 1.7 is fine with 2nd arg as POINTER(c_void_p),
# but CPython ctypes 1.1.0 complains, so just use c_void_p.
cf.CFSetGetValues.argtypes = ...

def cfset_to_set(cfset): ...

cf.CFArrayGetCount.restype = ...
cf.CFArrayGetCount.argtypes = ...

cf.CFArrayGetValueAtIndex.restype = ...
cf.CFArrayGetValueAtIndex.argtypes = ...

def cfarray_to_list(cfarray): ...

kCFRunLoopDefaultMode = ...

cf.CFRunLoopGetCurrent.restype = ...
cf.CFRunLoopGetCurrent.argtypes = ...

cf.CFRunLoopGetMain.restype = ...
cf.CFRunLoopGetMain.argtypes = ...

cf.CFShow.restype = ...
cf.CFShow.argtypes = ...

######################################################################

# APPLICATION KIT

# Even though we don't use this directly, it must be loaded so that
# we can find the NSApplication, NSWindow, and NSView classes.
appkit = ...

NSDefaultRunLoopMode = ...
NSEventTrackingRunLoopMode = ...
NSApplicationDidHideNotification = ...
NSApplicationDidUnhideNotification = ...

# /System/Library/Frameworks/AppKit.framework/Headers/NSEvent.h
# NSAnyEventMask = 0xFFFFFFFFL     # NSUIntegerMax
# Commented out b/c not Py3k compatible

NSKeyDown: int = ...
NSKeyUp: int = ...
NSFlagsChanged: int = ...
NSApplicationDefined: int = ...

NSAlphaShiftKeyMask = ...
NSShiftKeyMask = ...
NSControlKeyMask = ...
NSAlternateKeyMask = ...
NSCommandKeyMask = ...
NSNumericPadKeyMask = ...
NSHelpKeyMask = ...
NSFunctionKeyMask = ...

NSInsertFunctionKey: int = ...
NSDeleteFunctionKey: int = ...
NSHomeFunctionKey: int = ...
NSBeginFunctionKey: int = ...
NSEndFunctionKey: int = ...
NSPageUpFunctionKey: int = ...
NSPageDownFunctionKey: int = ...

# /System/Library/Frameworks/AppKit.framework/Headers/NSWindow.h
NSBorderlessWindowMask: int = ...
NSTitledWindowMask = ...
NSClosableWindowMask = ...
NSMiniaturizableWindowMask = ...
NSResizableWindowMask = ...

# /System/Library/Frameworks/AppKit.framework/Headers/NSPanel.h
NSUtilityWindowMask = ...

# /System/Library/Frameworks/AppKit.framework/Headers/NSGraphics.h
NSBackingStoreRetained: int = ...
NSBackingStoreNonretained: int = ...
NSBackingStoreBuffered: int = ...

# /System/Library/Frameworks/AppKit.framework/Headers/NSTrackingArea.h
NSTrackingMouseEnteredAndExited: int = ...
NSTrackingMouseMoved: int = ...
NSTrackingCursorUpdate: int = ...
NSTrackingActiveInActiveApp: int = ...

# /System/Library/Frameworks/AppKit.framework/Headers/NSOpenGL.h
NSOpenGLPFAAllRenderers: int = ...  # choose from all available renderers
NSOpenGLPFADoubleBuffer: int = ...  # choose a double buffered pixel format
NSOpenGLPFAStereo: int = ...  # stereo buffering supported
NSOpenGLPFAAuxBuffers: int = ...  # number of aux buffers
NSOpenGLPFAColorSize: int = ...  # number of color buffer bits
NSOpenGLPFAAlphaSize: int = ...  # number of alpha component bits
NSOpenGLPFADepthSize: int = ...  # number of depth buffer bits
NSOpenGLPFAStencilSize: int = ...  # number of stencil buffer bits
NSOpenGLPFAAccumSize: int = ...  # number of accum buffer bits
NSOpenGLPFAMinimumPolicy: int = ...  # never choose smaller buffers than requested
NSOpenGLPFAMaximumPolicy: int = ...  # choose largest buffers of type requested
NSOpenGLPFAOffScreen: int = ...  # choose an off-screen capable renderer
NSOpenGLPFAFullScreen: int = ...  # choose a full-screen capable renderer
NSOpenGLPFASampleBuffers: int = ...  # number of multi sample buffers
NSOpenGLPFASamples: int = ...  # number of samples per multi sample buffer
NSOpenGLPFAAuxDepthStencil: int = ...  # each aux buffer has its own depth stencil
NSOpenGLPFAColorFloat: int = ...  # color buffers store floating point pixels
NSOpenGLPFAMultisample: int = ...  # choose multisampling
NSOpenGLPFASupersample: int = ...  # choose supersampling
NSOpenGLPFASampleAlpha: int = ...  # request alpha filtering
NSOpenGLPFARendererID: int = ...  # request renderer by ID
NSOpenGLPFASingleRenderer: int = ...  # choose a single renderer for all screens
NSOpenGLPFANoRecovery: int = ...  # disable all failure recovery systems
NSOpenGLPFAAccelerated: int = ...  # choose a hardware accelerated renderer
NSOpenGLPFAClosestPolicy: int = ...  # choose the closest color buffer to request
NSOpenGLPFARobust: int = ...  # renderer does not need failure recovery
NSOpenGLPFABackingStore: int = ...  # back buffer contents are valid after swap
NSOpenGLPFAMPSafe: int = ...  # renderer is multi-processor safe
NSOpenGLPFAWindow: int = ...  # can be used to render to an onscreen window
NSOpenGLPFAMultiScreen: int = ...  # single window can span multiple screens
NSOpenGLPFACompliant: int = ...  # renderer is opengl compliant
NSOpenGLPFAScreenMask: int = ...  # bit mask of supported physical screens
NSOpenGLPFAPixelBuffer: int = ...  # can be used to render to a pbuffer
# can be used to render offline to a pbuffer
NSOpenGLPFARemotePixelBuffer: int = ...
NSOpenGLPFAAllowOfflineRenderers: int = ...  # allow use of offline renderers
# choose a hardware accelerated compute device
NSOpenGLPFAAcceleratedCompute: int = ...
# number of virtual screens in this format
NSOpenGLPFAVirtualScreenCount: int = ...

NSOpenGLCPSwapInterval: int = ...

# /System/Library/Frameworks/ApplicationServices.framework/Frameworks/...
#     CoreGraphics.framework/Headers/CGImage.h
kCGImageAlphaNone: int = ...
kCGImageAlphaPremultipliedLast: int = ...
kCGImageAlphaPremultipliedFirst: int = ...
kCGImageAlphaLast: int = ...
kCGImageAlphaFirst: int = ...
kCGImageAlphaNoneSkipLast: int = ...
kCGImageAlphaNoneSkipFirst: int = ...
kCGImageAlphaOnly: int = ...

kCGImageAlphaPremultipliedLast: int = ...

kCGBitmapAlphaInfoMask: int = ...
kCGBitmapFloatComponents = ...

kCGBitmapByteOrderMask: int = ...
kCGBitmapByteOrderDefault = ...
kCGBitmapByteOrder16Little = ...
kCGBitmapByteOrder32Little = ...
kCGBitmapByteOrder16Big = ...
kCGBitmapByteOrder32Big = ...

# NSApplication.h
NSApplicationPresentationDefault: int = ...
NSApplicationPresentationHideDock = ...
NSApplicationPresentationHideMenuBar = ...
NSApplicationPresentationDisableProcessSwitching = ...
NSApplicationPresentationDisableHideApplication = ...

# NSRunningApplication.h
NSApplicationActivationPolicyRegular: int = ...
NSApplicationActivationPolicyAccessory: int = ...
NSApplicationActivationPolicyProhibited: int = ...

######################################################################

# QUARTZ / COREGRAPHICS

quartz = ...

CGDirectDisplayID = ...  # CGDirectDisplay.h
CGError = ...  # CGError.h
CGBitmapInfo = ...  # CGImage.h

# /System/Library/Frameworks/ApplicationServices.framework/Frameworks/...
#     ImageIO.framework/Headers/CGImageProperties.h
kCGImagePropertyGIFDictionary = ...
kCGImagePropertyGIFDelayTime = ...

# /System/Library/Frameworks/ApplicationServices.framework/Frameworks/...
#     CoreGraphics.framework/Headers/CGColorSpace.h
kCGRenderingIntentDefault: int = ...

quartz.CGDisplayIDToOpenGLDisplayMask.restype = ...
quartz.CGDisplayIDToOpenGLDisplayMask.argtypes = ...

quartz.CGMainDisplayID.restype = ...
quartz.CGMainDisplayID.argtypes = ...

quartz.CGShieldingWindowLevel.restype = ...
quartz.CGShieldingWindowLevel.argtypes = ...

quartz.CGCursorIsVisible.restype = ...

quartz.CGDisplayCopyAllDisplayModes.restype = ...
quartz.CGDisplayCopyAllDisplayModes.argtypes = ...

quartz.CGDisplaySetDisplayMode.restype = ...
quartz.CGDisplaySetDisplayMode.argtypes = ...

quartz.CGDisplayCapture.restype = ...
quartz.CGDisplayCapture.argtypes = ...

quartz.CGDisplayRelease.restype = ...
quartz.CGDisplayRelease.argtypes = ...

quartz.CGDisplayCopyDisplayMode.restype = ...
quartz.CGDisplayCopyDisplayMode.argtypes = ...

quartz.CGDisplayModeGetRefreshRate.restype = ...
quartz.CGDisplayModeGetRefreshRate.argtypes = ...

quartz.CGDisplayModeRetain.restype = ...
quartz.CGDisplayModeRetain.argtypes = ...

quartz.CGDisplayModeRelease.restype = ...
quartz.CGDisplayModeRelease.argtypes = ...

quartz.CGDisplayModeGetWidth.restype = ...
quartz.CGDisplayModeGetWidth.argtypes = ...

quartz.CGDisplayModeGetHeight.restype = ...
quartz.CGDisplayModeGetHeight.argtypes = ...

quartz.CGDisplayModeCopyPixelEncoding.restype = ...
quartz.CGDisplayModeCopyPixelEncoding.argtypes = ...

quartz.CGGetActiveDisplayList.restype = ...
quartz.CGGetActiveDisplayList.argtypes = ...

quartz.CGDisplayBounds.restype = ...
quartz.CGDisplayBounds.argtypes = ...

quartz.CGImageSourceCreateWithData.restype = ...
quartz.CGImageSourceCreateWithData.argtypes = ...

quartz.CGImageSourceCreateImageAtIndex.restype = ...
quartz.CGImageSourceCreateImageAtIndex.argtypes = ...

quartz.CGImageSourceCopyPropertiesAtIndex.restype = ...
quartz.CGImageSourceCopyPropertiesAtIndex.argtypes = ...

quartz.CGImageGetDataProvider.restype = ...
quartz.CGImageGetDataProvider.argtypes = ...

quartz.CGDataProviderCopyData.restype = ...
quartz.CGDataProviderCopyData.argtypes = ...

quartz.CGDataProviderCreateWithCFData.restype = ...
quartz.CGDataProviderCreateWithCFData.argtypes = ...

quartz.CGImageCreate.restype = ...
quartz.CGImageCreate.argtypes = ...

quartz.CGImageRelease.restype = ...
quartz.CGImageRelease.argtypes = ...

quartz.CGImageGetBytesPerRow.restype = ...
quartz.CGImageGetBytesPerRow.argtypes = ...

quartz.CGImageGetWidth.restype = ...
quartz.CGImageGetWidth.argtypes = ...

quartz.CGImageGetHeight.restype = ...
quartz.CGImageGetHeight.argtypes = ...

quartz.CGImageGetBitsPerPixel.restype = ...
quartz.CGImageGetBitsPerPixel.argtypes = ...

quartz.CGImageGetBitmapInfo.restype = ...
quartz.CGImageGetBitmapInfo.argtypes = ...

quartz.CGColorSpaceCreateDeviceRGB.restype = ...
quartz.CGColorSpaceCreateDeviceRGB.argtypes = ...

quartz.CGDataProviderRelease.restype = ...
quartz.CGDataProviderRelease.argtypes = ...

quartz.CGColorSpaceRelease.restype = ...
quartz.CGColorSpaceRelease.argtypes = ...

quartz.CGWarpMouseCursorPosition.restype = ...
quartz.CGWarpMouseCursorPosition.argtypes = ...

quartz.CGDisplayMoveCursorToPoint.restype = ...
quartz.CGDisplayMoveCursorToPoint.argtypes = ...

quartz.CGAssociateMouseAndMouseCursorPosition.restype = ...
quartz.CGAssociateMouseAndMouseCursorPosition.argtypes = ...

quartz.CGBitmapContextCreate.restype = ...
quartz.CGBitmapContextCreate.argtypes = ...

quartz.CGBitmapContextCreateImage.restype = ...
quartz.CGBitmapContextCreateImage.argtypes = ...

quartz.CGFontCreateWithDataProvider.restype = ...
quartz.CGFontCreateWithDataProvider.argtypes = ...

quartz.CGFontCreateWithFontName.restype = ...
quartz.CGFontCreateWithFontName.argtypes = ...

quartz.CGContextDrawImage.restype = ...
quartz.CGContextDrawImage.argtypes = ...

quartz.CGContextRelease.restype = ...
quartz.CGContextRelease.argtypes = ...

quartz.CGContextSetTextPosition.restype = ...
quartz.CGContextSetTextPosition.argtypes = ...

quartz.CGContextSetShouldAntialias.restype = ...
quartz.CGContextSetShouldAntialias.argtypes = ...

quartz.CGDataProviderCreateWithURL.restype = ...
quartz.CGDataProviderCreateWithURL.argtypes = ...

quartz.CGFontCreateWithDataProvider.restype = ...
quartz.CGFontCreateWithDataProvider.argtypes = ...

quartz.CGDisplayScreenSize.argtypes = ...
quartz.CGDisplayScreenSize.restype = ...

quartz.CGDisplayBounds.argtypes = ...
quartz.CGDisplayBounds.restype = ...

######################################################################

# CORETEXT
ct = ...

# Types
CTFontOrientation = ...  # CTFontDescriptor.h
CTFontSymbolicTraits = ...  # CTFontTraits.h

# CoreText constants
kCTFontAttributeName = ...
kCTFontFamilyNameAttribute = ...
kCTFontSymbolicTrait = ...
kCTFontWeightTrait = ...
kCTFontTraitsAttribute = ...

# constants from CTFontTraits.h
kCTFontItalicTrait = ...
kCTFontBoldTrait = ...

ct.CTLineCreateWithAttributedString.restype = ...
ct.CTLineCreateWithAttributedString.argtypes = ...

ct.CTLineDraw.restype = ...
ct.CTLineDraw.argtypes = ...

ct.CTFontGetBoundingRectsForGlyphs.restype = ...
ct.CTFontGetBoundingRectsForGlyphs.argtypes = ...

ct.CTFontGetAdvancesForGlyphs.restype = ...
ct.CTFontGetAdvancesForGlyphs.argtypes = ...

ct.CTFontGetAscent.restype = ...
ct.CTFontGetAscent.argtypes = ...

ct.CTFontGetDescent.restype = ...
ct.CTFontGetDescent.argtypes = ...

ct.CTFontGetSymbolicTraits.restype = ...
ct.CTFontGetSymbolicTraits.argtypes = ...

ct.CTFontGetGlyphsForCharacters.restype = ...
ct.CTFontGetGlyphsForCharacters.argtypes = ...

ct.CTFontCreateWithGraphicsFont.restype = ...
ct.CTFontCreateWithGraphicsFont.argtypes = ...

ct.CTFontCopyFamilyName.restype = ...
ct.CTFontCopyFamilyName.argtypes = ...

ct.CTFontCopyFullName.restype = ...
ct.CTFontCopyFullName.argtypes = ...

ct.CTFontCreateWithFontDescriptor.restype = ...
ct.CTFontCreateWithFontDescriptor.argtypes = ...

ct.CTFontCreateCopyWithAttributes.restype = ...
ct.CTFontCreateCopyWithAttributes.argtypes = ...

ct.CTFontDescriptorCreateWithAttributes.restype = ...
ct.CTFontDescriptorCreateWithAttributes.argtypes = ...

ct.CTTypesetterCreateWithAttributedString.restype = ...
ct.CTTypesetterCreateWithAttributedString.argtypes = ...

ct.CTTypesetterCreateLine.restype = ...
ct.CTTypesetterCreateLine.argtypes = ...

ct.CTLineGetOffsetForStringIndex.restype = ...
ct.CTLineGetOffsetForStringIndex.argtypes = ...

ct.CTFontManagerCreateFontDescriptorsFromURL.restype = ...
ct.CTFontManagerCreateFontDescriptorsFromURL.argtypes = ...

######################################################################

# FOUNDATION

# foundation = cdll.LoadLibrary(util.find_library('Foundation'))

# foundation.NSMouseInRect.restype = c_bool
# foundation.NSMouseInRect.argtypes = [NSPoint, NSRect, c_bool]
