import bpy
from typing import List
import numpy as np


class BlenderObject:
    def __init__(self, obj: bpy.types.Object):
        self.obj = obj

    def store_float_vector(
        self, array: np.ndarray, name: str = "NewFloatVector"
    ) -> None:
        try:
            attr = self.obj.data.attributes[name]
        except KeyError:
            attr = self.obj.data.attributes.new(
                name=name, type="FLOAT_VECTOR", domain="POINT"
            )

        attr.data.foreach_set("vector", array.reshape(-1))

    def key_to_array(self, name: str) -> np.ndarray:
        points = self.obj.data.shape_keys.key_blocks[name].points
        array = np.zeros(len(points) * 3, float)
        points.foreach_get("co", array)
        return array.reshape((-1, 3))

    @property
    def key_names(self) -> List[str]:
        return self.obj.data.shape_keys.key_blocks.keys()

    def keys_to_attributes(self) -> None:
        for name in self.key_names:
            self.store_float_vector(self.key_to_array(name), name)
