import bpy

from . import leader_key


bl_info = {
    'name'        : 'Leader Key',
    'location'    : ('Add shortcut to ui.leaderkey '
                     'or access through search menu.'),
    'description' : 'Vim like <leader> key functionality for blender',
    'author'      : 'Adam Wolski(miniukof@gmail.com)',
    'wiki_url'    : 'https://github.com/miniukof/bl-leader_key',
    'version'     : (0, 0, 1),
    'blender'     : (2, 76, 11),
    'category'    : 'User Interface',
}


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
