# automatically generated, do not modify

# namespace: NamespaceB

import flatbuffers

class TableInNestedNS(object):
    __slots__ = ['_tab']

    # TableInNestedNS
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TableInNestedNS
    def Foo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def TableInNestedNSStart(builder): builder.StartObject(1)
def TableInNestedNSAddFoo(builder, foo): builder.PrependInt32Slot(0, foo, 0)
def TableInNestedNSEnd(builder): return builder.EndObject()
