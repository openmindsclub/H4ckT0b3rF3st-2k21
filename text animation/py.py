from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def doit(screen):
	effects=[
		Cycle(
			screen,
			FigletText("Happy", font='big'),
			int(screen.height/2-8)),
		Cycle(
			screen,
			FigletText("Programmers     Day", font='big'),
			int(screen.height /2+3)),
		Stars(screen,200)
		]
	screen.play([Scene(effects,5000)])


Screen.wrapper(doit)
