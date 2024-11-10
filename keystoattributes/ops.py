from bpy.types import Operator, Context
from .object import BlenderObject


class KTA_OT_Keys_To_Attributes(Operator):
    bl_idname = "kta.bake_keys_to_attributes"
    bl_label = "Shape Keys to Attributes"
    bl_description = (
        "Bake all shape keys to mesh attributes, that are accesible via Geometry Nodes"
    )

    @classmethod
    def poll(cls, context: Context):
        try:
            context.active_object.data.shape_keys.key_blocks
            return True
        except AttributeError:
            return False

    def execute(self, context):
        bob = BlenderObject(context.active_object)
        try:
            bob.keys_to_attributes()
            self.report(
                {"INFO"}, f"Added {len(bob.key_names)} shape keys as attributes"
            )
        except AttributeError as e:
            print(e)
            self.report({"ERROR"}, "Object contains no shape keys")
            return {"CANCELLED"}

        return {"FINISHED"}


CLASSES = [KTA_OT_Keys_To_Attributes]
