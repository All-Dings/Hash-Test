#include <Python.h>

static PyObject* Adder_Csum(PyObject* self, PyObject *args)
{
	unsigned long Csum = 0;
	unsigned char *Buf;
	Py_buffer Buffer;
	PyObject *Bytes;
	int i;

	if (!PyArg_ParseTuple(args, "O|b", &Bytes))
		return NULL;

	if (PyObject_GetBuffer(Bytes, &Buffer, PyBUF_WRITABLE) < 0)
		return NULL;

	Buf = Buffer.buf;
	for(i=0; i < Buffer.len; i++) {
		Csum += Buf[i];
	}
	PyBuffer_Release(&Buffer);
	return Py_BuildValue("l", Csum);
}

static char Adder_Csum_Docs[] = "usage: Adder_Csum(bytes)\n";

static PyMethodDef module_methods[] = {
    {"Adder_Csum", (PyCFunction) Adder_Csum, METH_VARARGS, Adder_Csum_Docs},
    {NULL}
};

static struct PyModuleDef Dings_Lib_C =
{
    PyModuleDef_HEAD_INIT,
    "Dings_Lib_C",
    "Usage: Dings_Lib_C.Adder_Csum()\n",
    -1,
    module_methods
};

PyMODINIT_FUNC PyInit_Dings_Lib_C(void)
{
    return PyModule_Create(&Dings_Lib_C);
}
