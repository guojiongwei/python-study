
class Demo:
  def __init__(self, name):
    self.name = name
    self.sex = '男'

  def on_change_sex(self, sex):
    self.sex = sex

  def say(self):
    return self.name

demo = Demo('张三')
demo.on_change_sex('女111')
print(demo.say())
print(demo.sex)
