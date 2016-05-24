import io
import mathutils
import struct

class BinaryReader:
    def __init__(self, raw):
        self.raw = raw
        self.endianness = "<" # Little-endian

    def __enter__(self):
        self.reader = io.BufferedReader(self.raw)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.reader.close()

    def seek(self, offset, whence=io.SEEK_SET):
        self.reader.seek(offset, whence)

    def tell(self):
        return self.reader.tell()

    def read_byte(self):
        return self.reader.read(1)[0]

    def read_bytes(self, count):
        return self.reader.read(count)

    def read_int32(self):
        return struct.unpack(self.endianness + "i", self.reader.read(4))[0]

    def read_sbyte(self):
        return struct.unpack(self.endianness + "b", self.reader.read(1))[0]

    def read_single(self):
        return struct.unpack(self.endianness + "f", self.reader.read(4))[0]

    def read_uint16(self):
        return struct.unpack(self.endianness + "H", self.reader.read(2))[0]

    def read_uint16s(self, count):
        return struct.unpack(self.endianness + str(int(count)) + "H", self.reader.read(int(2 * count)))

    def read_uint32(self):
        return struct.unpack(self.endianness + "I", self.reader.read(4))[0]

    def read_uint32s(self, count):
        return struct.unpack(self.endianness + str(int(count)) + "I", self.reader.read(4 * count))

    def read_matrix4x3(self):
        matrix = mathutils.Matrix()
        matrix[0][0] = self.read_single()
        matrix[0][1] = self.read_single()
        matrix[0][2] = self.read_single()
        matrix[1][0] = self.read_single()
        matrix[1][1] = self.read_single()
        matrix[1][2] = self.read_single()
        matrix[2][0] = self.read_single()
        matrix[2][1] = self.read_single()
        matrix[2][2] = self.read_single()
        matrix[3][0] = self.read_single()
        matrix[3][1] = self.read_single()
        matrix[3][2] = self.read_single()
        return matrix

    def read_raw_string(self, length, encoding="ascii"):
        return self.reader.read(length).decode(encoding)

    def read_0_string(self):
        text = ""
        i = self.read_byte()
        while i != 0:
            text += chr(i)
            i = self.read_byte()
        return text

    def read_vector2f(self):
        return self.read_single(), self.read_single()

    def read_vector3f(self):
        return self.read_single(), self.read_single(), self.read_single()

    def read_quaternion(self):
        return mathutils.Quaternion((self.read_single(), self.read_single(), self.read_single(), self.read_single()))
