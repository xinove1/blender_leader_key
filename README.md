# Vim like 'leader' key functionality for blender.

In my workflow I use a lot of shortcuts, so much in fact that now I can't really find empty slots for new bindings. So I looked to other software that I love and use a lot of hotkeys in: Vim. In Vim shortcuts can be specified as list of keys for ex: 
```vim 
nnoremap <leader>cf :call_function()<CR>
```
would mean that after pressing 'leader' key followed by 'c' and 'f' key in normal mode it would call 'call_function()'. Reading sequence of characters as shortcut means that we get like... a lot of new possible shortcuts. Thats the functionality I tried to replicate in this add-on.

# Installation

In User Preferences window go to the Add-ons tab, in lower left corner select "Install from File" button and point it to the "leader_key.py" file.

# Configuration

## Leading Key (add-on key-binding)

I personally am not a fun of add-on that register keyboard shortcuts for themselves. So I left that for user choice. Function call for starting add-on is "ui.leaderkey", which if you are familiar of how to create blender keyboard shortcuts should be enough information and can skip to next section.

Otherwise quick instructions on how to create keyboard bindings in blender.

Go to the Input tab in User Preferences select context in which that shortcut is to be bound to. In case of this add-on it's best to select something pretty high like Screen so you can call it whether you are in 3D View or Node Editor.

Go through context options till you get to the "Add New" button. Click it. It will create new shortcut with most of the options pretty self-explanatory. Type "ui.leaderkey" in the "Identifier of operator to call on input event" field, and you're done.

## Rest of Configuration

All the configuration options for add-on are available in Add-ons tab of User Preferences window.

"Bindings number" - Tells how many bindings you want to show up in options and be used when calling the "ui.leaderkey" function.

"Timeout" - Amount of time to wait if no function call was found for typed sequence. (In seconds)

"Wait For Next" - Amount of time you have to type next key if there's already function call for current sequence. (In seconds)

"Key String" - String of Keys for sequence. Can be almost any of the types in event.type from blender and needs to be separated by one space. [Blender event.type](https://www.blender.org/api/blender_python_api_2_77_0/bpy.types.Event.html?highlight=event.type#bpy.types.Event.type)

"Function" - Function to be called after sequenced is matched. Can be anything python script could call so you can type either something blender specific like: "bpy.ops.mesh.primitive_torus_add()" or just something in python like: "print("Hello World")". In fact you could write whole python script in that input field. Those familiar with python probably already guessed that it's just call to the exec() function with whatever you typed in here, which means that you can break or make anything with those calls.

"Context area type" - Context area in which to use this binding. Select 'All' to not bind it to any of the specific types of window.

"Context mode" - Same as above just for mode of the window.

# Usage

Call the "ui.leaderkey" function and start typing you sequence, after you're done function you specified will be called.
