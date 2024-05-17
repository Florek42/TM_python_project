from ursina import Entity, Vec3, Ursina, KeyCode

class Player(Entity):
  def __init__(self):
    super().__init__()
    self.speed = 6
    self.gravity = -0.05

  def update(self):
    
    if held_keys[KeyCode.w]:
      self.position += self.forward * self.speed * dt
    if held_keys[KeyCode.s]:
      self.position -= self.forward * self.speed * dt
    if held_keys[KeyCode.a]:
      self.position -= self.right * self.speed * dt
    if held_keys[KeyCode.d]:
      self.position += self.right * self.speed * dt


    self.y += self.gravity * dt

 
    if self.y < -1:
      self.y = -1
      self.gravity = 0  
