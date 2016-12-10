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

Application().run()
