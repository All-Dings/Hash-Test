all: Dings_Lib_C.egg-info
	python3 Hash-Test.py

install: Dings_Lib_C.egg-info

Dings_Lib_C.egg-info: Dings_Lib_C.c
	python3 setup.py build
	python3 setup.py install


clean:
	rm -rf build/ dist/ Dings_Lib_C.egg-info/

.PHONY: all clean Dings_Lib_C
