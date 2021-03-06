# Creating a scene in blender

## Requirements
- A render pipeline installation
- A Blender installation
- Basic blender knowledge

In this tutorial we will cover how to properly create models and lights in blender
so they can be used in the render pipeline. We will also cover how to install
the bam exporter.

However, this is not a blender tutorial. If you are not familiar with blender,
I recommend checking out the <a href="https://www.blender.org/support/tutorials/">Blender Tutorials</a> first.

You can find the scene we will model in the this tutorial <a href="scene.blend">here</a>.

## Installing the BAM exporter

To be able to export our models, we need to install the bam exporter plugin for blender:

Head over to the <a href="https://github.com/tobspr/Panda3D-Bam-Exporter/releases/">Panda3D Bam Exporter Releases</a> page
and download the latest zip.

Next, open Blender, and select `File` > `User Preferences`. The preferences window
should open:


1. Go to the *Addons* tab, click `Install from file ...` and locate the zip file you just downloaded.
2. Type `BAM` in the search field. The extensions should now show up.
3. Ensure the extension is enabled, by checking its checkbox


<img src="install_bam_exporter.png" alt="Bam Exporter Install Instructions" />

If any issues occur, please fill out an issue <a href="https://github.com/tobspr/Panda3D-Bam-Exporter/issues">here</a> (Really, please!).


## Creating your scene

I will not focus in depth about how to model a scene, and we will really keep it simple
here. Assuming we already modeled this geometry (notice I deleted the standard light and camera):

<img src="scene_part1.png" />


### Adding lights

To make our objects shaded, we will add a rectangle area light. To do so, 
hit <kbd>Space</kbd> and enter `Add Lamp`, then select `Area`. An area light should be
created, and if you go to the object light data, you will see the light properties
(notice I already moved the light, and changed its size and color):

<img src="scene_light.png" />

### Exporting the scene

To export the scene, press <kbd>Space</kbd> and type `BAM`. You should see the
option `Export to Panda3D BAM`, which you can execute with <kbd>Enter</kbd>.

A screen similar to the one below will show up, for now we do not need to modify
the options, and can just press `Export to Panda3D BAM` in the top right corner:

<img src="export.png" />  

### Loading the scene
*(You can find the full source of this example <a href="main.py">here</a>.)*

To load or model, we have to add the following lines to our <a href="../Basic-Example/README.md">Basic Example</a>:

    model = self.loader.load_model("scene.bam")
    model.reparent_to(self.render)
    self.render_pipeline.prepare_scene(model)

Besides of the last line, this should be nothing new for you. The `prepare_scene`
method has to get called after you loaded a model, and it ensures the scene is properly
setup. In case you are interested what it does exactly, checkout the <a href="FIXME">Render Pipeline API</a>.

To make our camera point into the right direction, we also add the following:

    base.disable_mouse()
    base.camera.set_pos(-0.9, -24.8, 14.6)
    base.camera.look_at(model)
    base.camLens.set_fov(45)

If we now start our sample, we will see something similar to this (notice it may vary
depending on enabled plugins and render pipeline versions):

<img src="exported.png" alt="Exported Scene Result" />


If you think this looks boring, no worry: we will improve on this scene in the next tutorial, in which we will cover texturing.

