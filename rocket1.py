from ggrocket import Rocket, Planet

earth = Planet()
rocket = Rocket(earth, altitude=50)
earth.run(rocket)
