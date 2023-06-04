# Performance-Test for Hash-Functions

import datetime as Dt
import bitmath as Bm
import hashlib as Hl
import random as Rand
import os as Os

import Dings_Lib_C

# Data-Size: 32 * 16 MiB = 512 MiB

LOOP_COUNT = 32
BUFFER_SIZE = Bm.MiB(16)

# Run Test for one Hasn-Function
def Runtime_Test(Hash_Function, Data):
	Data_Size_MiB = Bm.Byte(len(Data)).to_MiB()
	Delta_Sum = Dt.timedelta(0)
	Hash_Function_Name = Hash_Function.__name__.replace("openssl", "ssl").lower()

	for i in range(0, LOOP_COUNT):
		Start_Time = Dt.datetime.now()
		Hash = Hash_Function(Data)
		End_Time = Dt.datetime.now()
		Delta = End_Time - Start_Time
		Delta_Sum = Delta_Sum + Delta
	Delta_Sum_Us = Delta_Sum.seconds * 1000000 + Delta_Sum.microseconds
	MiB_Per_Second = int((Data_Size_MiB * LOOP_COUNT) / (Delta_Sum_Us / 1000000))
	if Hash_Function_Name == "ssl_shake_128" or Hash_Function_Name == "ssl_shake_256":
		Hash_Digest = Hash.hexdigest(32)
	else:
		Hash_Digest = Hash.hexdigest()
	if len(Hash_Digest) > 64:
		Hash_Digest = Hash_Digest[:64] + "..."
	print(f"{Hash_Function_Name:<13} | {Delta_Sum_Us:>10} | {MiB_Per_Second:>5} | {Hash_Digest}")
	return MiB_Per_Second

# Check-Sum Base-Class
class Csum_Class:
	def hexdigest(Self, Max_Byte = 0):
		Hex_String = hex(Self.Hash_Value)
		if Max_Byte == 0:
			return Hex_String[2:]
		else:
			return Hex_String[2:Max_Byte * 2]

# Digit-Sum in C
class Add_C(Csum_Class):
	def __init__(Self, Data):
		Self.Hash_Value = Dings_Lib_C.Adder_Csum(bytearray(Data))

# Digit-Sum in Python
class Add_Py(Csum_Class):
	def __init__(Self, Data):
		Data_Size = Bm.Byte(len(Data))
		Self.Hash_Value = 0
		for Byte_Nr in range(0, int(Data_Size.to_Byte())):
			Self.Hash_Value += int(Data[Byte_Nr])

# List of all Hash-Functions to test
Hash_Function_List = [
	Add_C,
	Add_Py,
	Hl.md5,
	Hl.sha1,
	Hl.sha224,
	Hl.sha256,
	Hl.sha384,
	Hl.sha512,
	Hl.sha3_224,
	Hl.sha3_256,
	Hl.sha3_384,
	Hl.sha3_512,
	Hl.shake_128,
	Hl.shake_256,
	Hl.blake2b,
	Hl.blake2s
]

# Run all Tests
def Hash_Functions_Test():
	Data = Rand.randbytes(int(BUFFER_SIZE.to_Byte()))
	Host = Os.uname()[1]
	Result_List_Ms = [Host]
	Heading_List = ["Computer"]

	Hdr_Hash_Function_Name ="Function"
	Hdr_Delta_Sum_Us ="us"
	Hdr_MiB_Per_Second ="MiB/s"
	Hdr_Hash ="Hash"

	print(f"{Hdr_Hash_Function_Name:<13} | {Hdr_Delta_Sum_Us:>10} | {Hdr_MiB_Per_Second:>5} | {Hdr_Hash}")
	print("--------------------------------------------------------------------------------------------------------")
	for Hash_Function in Hash_Function_List:
		Heading_List.append(Hash_Function.__name__.replace("openssl", "").lower())
		Result_List_Ms.append(str(Runtime_Test(Hash_Function, Data)))

	print("--------------------------------------------------------------------------------------------------------")
	print("CSV for Analyis")
	print("--------------------------------------------------------------------------------------------------------")
	print(";".join(Heading_List))
	print(";".join(Result_List_Ms))

Hash_Functions_Test()
