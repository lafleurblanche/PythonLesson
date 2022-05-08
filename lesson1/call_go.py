from ctypes import cdll

lib = cdll.LoadLibrary("./lesson1/export.so")
lib.cgo_hello()
