"""
Check the tutorial for comments on the code.
"""

import sys
from direct.showbase.ShowBase import ShowBase


class Application(ShowBase):

    def __init__(self):
        sys.path.insert(0, "render_pipeline")

        from rpcore import RenderPipeline

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)

        model = self.loader.load_model("scene.bam")
        model.reparent_to(self.render)
        self.render_pipeline.prepare_scene(model)

        base.disable_mouse()
        base.camera.set_pos(-0.9, -24.8, 14.6)
        base.camera.look_at(model)
        base.camLens.set_fov(45)


Application().run()
