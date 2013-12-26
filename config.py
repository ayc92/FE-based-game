import ConfigParser

class Level(object):
  def load_file(self, filename="level.map"):
    self.map = [[]]
    self.key = {}
    self.posx = 0
    self.posy = 0
    parser = ConfigParser.ConfigParser()
    parser.read(filename)
    tempMap = parser.get("level", "map").split("\n")
    for line in tempMap:
      self.map.append(list(line))
    for section in parser.sections():
      if len(section) == 1:
        desc = dict(parser.items(section))
        self.key[section] = desc
    self.map.pop(0)
    print len(self.map)
    self.width = len(self.map[0])
    self.height = len(self.map)
    for y, line in enumerate(self.map):
      for x, c in enumerate(line):
        if self.map[y][x] == "x":
          self.posx = x
          self.posy = y

    def get_tile(self, x, y):
      try:
        char = self.map[y][x]
      except IndexError:
        return {}
      try:
        return self.key[char]
      except KeyError:
        return {}

  def is_wall(self, x, y):
    return self.get_bool(x, y, 'wall')

  def render(self):
    out = ""
    for line in self.map:
      # for map_x, c in enumerate(line):
      #   tile = self.key[c]['name']
      #   if tile == 'unit':
      #     out += "x"
      #   elif tile == 'blank':
      #     out += "-"
      for char in line:
        out += char
      out += "\n"
    return out

  def move(self, dx, dy):
    y = self.posy
    x = self.posx
    self.map[y][x] = '-'
    self.posy = (self.height+y+dy)%self.height
    self.posx = (self.width+x+dx)%self.width

    self.map[self.posy][self.posx] = 'x'

