[fake-bpy-module-4.2](https://github.com/nutti/fake-bpy-module?tab=readme-ov-file), but add the "fake" prefix to the name of all submodules.

Blender provide its official [blender python module](https://docs.blender.org/api/current/info_advanced_blender_as_bpy.html), however IntelliSense doesn't work for it. [fake-bpy-module](https://github.com/nutti/fake-bpy-module?tab=readme-ov-file) can be parsed by IntelliSense, but it's fake. Both are imported using name `bpy`, so there might be ambiguity if they are installed in the same environment.  

As a rude solution, I add the "fake" prefix to the name of all submodules of fake-bpy-module. Though I believe there are smarter solutions...  

To use, just download/clone, and then `python setup.py install`. `import fakebpy as bpy` to use fake-bpy-module for IntelliSense, `import bpy` for executing.