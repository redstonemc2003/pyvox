from settings import *
from meshes.quad_mesh import QuadMesh

class Scene(QuadMesh):
    def __init__(self, app):
        self.app = app
        self.quad_mesh = QuadMesh(self.app)

    def update(self):
        pass

    def render(self):
        self.quad_mesh.render()