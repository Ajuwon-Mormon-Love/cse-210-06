import constants
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("Reach this side and avoid the mines")
    banner.set_font_size(constants.FONT_SIZE)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(constants.MAX_X /2)
    position = Point(x, constants.MAX_Y - 20)

    robot = Actor()
    robot.set_text("O")
    robot.set_font_size(constants.FONT_SIZE)
    robot.set_color(constants.GREEN)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    for n in range(constants.DEFAULT_MINES):
        text = constants.MINES
        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, constants.ROWS - 2)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        color = constants.WHITE
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(constants.FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(Point(0,1))
        cast.add_actor("artifacts", artifact)
       
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()