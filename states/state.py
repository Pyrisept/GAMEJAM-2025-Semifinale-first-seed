
#state.py
class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, delta_time, actions):
        pass

    def render(self, display):
        pass

    def enter_state(self):
        print(f"Entering state: {self.__class__.__name__}")
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
        print(f"State stack: {[state.__class__.__name__ for state in self.game.state_stack]}")


    def exit_state(self):
        print(f"Exiting state: {self.__class__.__name__}")
        self.game.state_stack.pop()
        print(f"State stack: {[state.__class__.__name__ for state in self.game.state_stack]}")