import numpy as np

class BaseMesh:
    def __init__(self):
        # OpenGl Context
        self.ctx = None
        # Shader Program
        self.shader_program = None
        # Vertext Buffer Data Type 3f 3f
        self.vbo_format = None
        # attribute names according to format ["test", "test"]
        self.attrs :  tuple[str, ...] = None
        # Vertext Array Object
        self.vao = None
    
    def get_vertex_data(self) -> np.array : ...
    
    def get_vao(self):
        vertext_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertext_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors= True
        )
        return vao
    
    def render(self):
        self.vao.render()
