import bpy

from . import leader_key

def register():
    leader_key.register()
    #bpy.utils.register_module(__name__)

def unregister():
    leader_key.unregister()
    #bpy.utils.unregister_module(__name__)
