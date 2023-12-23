from ctypes import *

from generic_mash_data_ptrs import *
from resource_location import *
from tlresource_location import *

class mashable_vector(Structure):
    _fields_ = [("m_data", POINTER(c_int)),
               ("m_size", c_short),
               ("m_shared", c_bool),
               ("field_7", c_bool)
                ]

    def __repr__(self):
        return f'mashable_vector(m_size={self.m_size}, m_shared={self.m_shared}, ' \
                f'm_shared={self.from_mash()})'

    def from_mash(self) -> bool:
        return self.field_7

    def size(self):
        return self.m_size

    def empty(self) -> bool:
        return self.size() == 0

    def custom_un_mash(self, a4: generic_mash_data_ptrs, buffer_bytes) -> generic_mash_data_ptrs:
        print("custom_un_mash")

        a4.rebase(4)
        a4.rebase(4)

        offset = int(a4.field_0)
        a4.field_0 += 4 * self.m_size

        array_type = c_int * int(self.m_size)
        size = sizeof(array_type)
        array_data = array_type.from_buffer_copy(buffer_bytes[offset : offset + size])
        self.m_data = cast(array_data, POINTER(c_int))

        a4.rebase(4)

        return a4

    def un_mash(self, a4: generic_mash_data_ptrs, buffer_bytes) -> generic_mash_data_ptrs:
        assert(self.from_mash())
        return self.custom_un_mash(a4, buffer_bytes)

class mashable_vector__resource_location(Structure):
    _fields_ = [("m_data", POINTER(resource_location)),
               ("m_size", c_short),
               ("m_shared", c_bool),
               ("field_7", c_bool)
                ]

    def __repr__(self):
        return f'mashable_vector(m_size={self.m_size}, m_shared={self.m_shared}, ' \
                f'm_shared={self.from_mash()})'

    def from_mash(self) -> bool:
        return self.field_7

    def size(self):
        return self.m_size

    def empty(self) -> bool:
        return self.size() == 0

    def custom_un_mash(self, a4: generic_mash_data_ptrs, buffer_bytes) -> generic_mash_data_ptrs:
        print("custom_un_mash<resource_location>")

        a4.rebase(8)
        a4.rebase(4)

        print("0x%08X" % a4.field_0)

        offset = int(a4.field_0)
        a4.field_0 += sizeof(resource_location) * self.m_size

        array_type = resource_location * int(self.m_size)
        size = sizeof(array_type)
        array_data = array_type.from_buffer_copy(buffer_bytes[offset : offset + size])
        self.m_data = cast(array_data, POINTER(resource_location))

        a4.rebase(4)

        return a4


class mashable_vector__tlresource_location(Structure):
    _fields_ = [("m_data", POINTER(tlresource_location)),
               ("m_size", c_short),
               ("m_shared", c_bool),
               ("field_7", c_bool)
                ]

    def __repr__(self):
        return f'mashable_vector(m_size={self.m_size}, m_shared={self.m_shared}, ' \
                f'm_shared={self.from_mash()})'

    def from_mash(self) -> bool:
        return self.field_7

    def size(self):
        return self.m_size

    def empty(self) -> bool:
        return self.size() == 0

    def custom_un_mash(self, a4: generic_mash_data_ptrs, buffer_bytes) -> generic_mash_data_ptrs:
        print("custom_un_mash<tlresource_location>")

        a4.rebase(8)
        a4.rebase(4)

        offset = int(a4.field_0)
        a4.field_0 += sizeof(tlresource_location) * self.m_size

        array_type = tlresource_location * int(self.m_size)
        size = sizeof(array_type)
        array_data = array_type.from_buffer_copy(buffer_bytes[offset : offset + size])
        self.m_data = cast(array_data, POINTER(tlresource_location))

        a4.rebase(4)
        return a4

    def un_mash(self, a4: generic_mash_data_ptrs) -> generic_mash_data_ptrs:
        assert(self.from_mash())
        return self.custom_un_mash(a4)


print(sizeof(mashable_vector) == 8)
print(sizeof(mashable_vector__resource_location) == 8)
print(sizeof(mashable_vector__tlresource_location) == 8)
