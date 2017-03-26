class State:
  def __init__(self, name, state):
    self.name = name
    self.state = state
  def getName(self):
    return self.name
  def getState(self):
    return self.state


def main():
  machine = State("Machine", 1)
  print(machine.getState())


if __name__ == "__main__":
  main()