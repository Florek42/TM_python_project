from ursina import Entity, Plane, load_texture

floor = Plane(texture=load_texture("graphics/textures/floor.jpg"))
floor.scale = 100, 100
player = Entity(model="graphics/models/character.obj", position=(0, 0, 0.5))
