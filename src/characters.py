import pymunk as pm
from pymunk import Vec2d


class Bird():
    def __init__(self, distance, angle, x, y, space):
        self.life = 500
        mass = 5
        self.radius = 12
        inertia = pm.moment_for_circle(mass, 0, self.radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        power = distance * 53
        impulse = power * Vec2d(1, 0)
        angle = -angle
        body.apply_impulse(impulse.rotated(angle))
        shape = pm.Circle(body, self.radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def getPosition(self):
        # Get Bird position
        return self.body.position

    def getRadius(self):
        return self.radius

    def age(self):
        # Ages the bird by one unit
        # TODO - should only age when no more movement, and then age quickly
        self.life-=1

    def dead(self):
        # Returns if the bird is dead or not
        return self.life<=0


class Pig():
    def __init__(self, x, y, space):
        self.life = 20
        mass = 5
        self.radius = 14
        inertia = pm.moment_for_circle(mass, 0, self.radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        shape = pm.Circle(body, self.radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def getPosition(self):
        # Get Pig position
        return self.body.position

    def getRadius(self):
        # Get Radius
        return self.radius
