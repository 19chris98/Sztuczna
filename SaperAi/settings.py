"""
Settings for setup conts for run a game
"""

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600

BLACK = (0, 0, 0)

HOW_MANY_FIELDS = 20

FIELD_SIZE = DISPLAY_HEIGHT / HOW_MANY_FIELDS
ROBOT_SIZE = int(FIELD_SIZE * 1)


MODEL_FILE_1 = 'tf/tf_files_2/retrained_graph.pb'
LABEL_FILE_1 = 'tf/tf_files_2/retrained_labels.txt'

ROBOT_IMG_PATH = 'images/robot.png'
BOMB_IMG_PATH = 'images/bomba.png'


DATA_PATH = 'data/data.txt'
FONT_NAME = 'freesansbold.ttf'
GAME_NAME = 'Saper'

ACTIONS = {
    'bomba': 'Detonuje',
    'c4': 'Rozbrajam',
    'dynamit': 'Zabieram',
    'mina': 'Detonuje'
}
