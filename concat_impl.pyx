# cython_example.pyx
""" Example cython interface definition """

cdef extern from "concatenate.c":
    char* concatenate_strings(const char* str1, const char* str2)

def pyconcat( str1, str2 ):
    result_in_bytes = concatenate_strings( str.encode(str1), str.encode(str2) )
    return result_in_bytes.decode()