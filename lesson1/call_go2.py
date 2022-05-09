from ctypes import cdll
import time

start_time = time.perf_counter()

lib = cdll.LoadLibrary("./lesson1/export.so")
lib.cgo_hello()

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(elapsed_time)
