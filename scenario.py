class Scenario:
    def __init__(self, props):
        self.props = props

    def draw(self):
        for prop in self.props:
            prop.draw()

    def update(self):
        for prop in self.props:
            prop.update()

    def remove_prop(self, prop):
        self.props.remove(prop)