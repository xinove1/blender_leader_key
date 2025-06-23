import bpy

if "leader_key" in locals():
    import importlib
    importlib.reload(leader_key)
    print("leadker_key: reloaded")
else:
    from . import leader_key

def register():
    leader_key.register()
    print("leadker_key: registred")

def unregister():
    leader_key.unregister()
    print("leadker_key: unregistred")
