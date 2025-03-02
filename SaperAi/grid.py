from PIL import Image
import random
import glob

from field import Field


class Grid:
    def __init__(self, how_many_fields, field_size, params_data):
        self.grid = []
        self.path = []
        self.how_many_fields = how_many_fields
        self.drawing_size = how_many_fields*field_size

        bomb_list = self.get_images('images/bomby/*.*')
        other_image_list = self.get_images('other_images/*.*')

        for y in range(0, how_many_fields):
            horizontal = []
            for x in range(0, how_many_fields):
                is_wall_field = self.is_wall_field(how_many_fields, x, y)
                is_mud = self.is_special_field(not is_wall_field)
                is_water = self.is_special_field(not is_wall_field) if not is_mud else False
                is_bomb = self.is_bomb_field(not is_wall_field, not is_water)
                field_params = self.generate_params(params_data, is_bomb)
                photo = self.get_photo(bomb_list if is_bomb else other_image_list)
                field = Field(x, y, field_params, field_size, not is_wall_field, is_bomb, is_mud, is_water, photo)
                horizontal.insert(len(horizontal), field)
            self.grid.insert(len(self.grid), horizontal)

    def get_images(self, directory):
        return [Image.open(filename).filename for filename in glob.glob(directory)]

    def get_photo(self, images):
        return images[random.randrange(len(images))]

    def is_wall_field(self, how_many_fields, x, y):
        if x == (how_many_fields-1 and y == (how_many_fields-1)):
            is_wall_field = False
        else:
            is_wall_field = random.randrange(8) == 1
        return is_wall_field

    def is_special_field(self, is_walkable):
        return random.randrange(5) == 1 if is_walkable else False

    def is_bomb_field(self, is_walkable, is_not_water):
        return random.randrange(20) == 1 if is_walkable and is_not_water else False

    def get_neighbours(self, field):
        neighbours = []

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue

                check_x = field.x + x
                check_y = field.y + y

                if self.how_many_fields > check_x >= 0 and self.how_many_fields > check_y >= 0:
                    neighbours.insert(len(neighbours), self.grid[check_y][check_x])

        return neighbours

    def set_path(self, path):
        self.path = path

    def first_and_last(self):
        last = self.how_many_fields - 1
        return [self.grid[0][0], self.grid[last][last]]

    def generate_params(self, params_data, is_bomb):
        is_bomb = int(is_bomb)
        correct_params = list(filter(lambda x: x[-1] == '{}'.format(is_bomb), params_data))
        correct_params_amount = len(correct_params)
        n = random.randrange(correct_params_amount)
        return correct_params[n]


