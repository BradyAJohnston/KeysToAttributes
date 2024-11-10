from bpy.types import Menu, Context


def draw_button(menu: Menu, context: Context) -> None:
    layout = menu.layout
    layout.operator("kta.bake_keys_to_attributes", text="Bake To Attributes")
