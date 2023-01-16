"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    count: int =0

    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1

    pass


def index():
    return pc.text("ROot Page")

def about():
    return pc.text("About Page")

def click():
    return pc.center(
        pc.vstack(
            pc.heading(
                'click!',
                font_size="2rem",
                margin_botton=10
            ),
            pc.hstack(
                pc.button(
                    "-",
                    color_scheme="red",
                    border_radius="1rem",
                    on_click=State.decrement,
                    size='1g',
                ),
                pc.heading(State.count, font_size="2rem"),
                pc.button(
                    "+",
                    color_scheme="green",
                    border_radius="1rem",
                    on_click=State.increment,
                    size="1g",
                ),
                spacing="20px",
            ),
        ),
        padding_top ="10%",
        font_size="2rem"
    )






# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, path="/")
app.add_page(about, path="/about")
app.add_page(click, path="/click")
app.compile()
