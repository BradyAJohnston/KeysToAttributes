# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Keys to Attributes",
    "description": "Bake shape keys as attributes for access in Geometry Nodes",
    "author": "Brady Johnston",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    # "location": "Data > Shape Keys",
    # "doc_url": "http://archive.blender.org/wiki/2015/index.php/Extensions:2.6/Py/Scripts/My_Script",
    # "tracker_url": "https://developer.blender.org/maniphest/task/edit/form/2/",
    # "support": "COMMUNITY",
}

from bpy.utils import register_class, unregister_class
from bpy.types import DATA_PT_shape_keys

from .ops import CLASSES
from .menu import draw_button


def register():
    for cls in CLASSES:
        register_class(cls)
    DATA_PT_shape_keys.prepend(draw_button)


def unregister():
    for cls in reversed(CLASSES):
        unregister_class(cls)
    DATA_PT_shape_keys.remove(draw_button)
