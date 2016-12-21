"""
Check the tutorial for comments on the code.
"""

import sys
from direct.showbase.ShowBase import ShowBase

from panda3d.core import Vec3


class Application(ShowBase):

    def __init__(self):
        sys.path.insert(0, "render_pipeline")

        from rpcore import RenderPipeline
        from rpcore.util.movement_controller import MovementController

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(self)

        model = self.loader.load_model("scene.bam")
        model.reparent_to(self.render)
        self.render_pipeline.prepare_scene(model)

        self.controller = MovementController(self)
        self.controller.set_initial_position(Vec3(10, -10, 10), Vec3(0, 0, 0))
        self.controller.setup()

Application().run()
