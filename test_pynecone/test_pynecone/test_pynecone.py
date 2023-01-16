"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
#
#docs_url = "https://pynecone.io/docs/getting-started/introduction"
#filename = f"{config.app_name}/{config.app_name}.py"
#


#
#
#def index():
#    return pc.center(
#        pc.vstack(
#            pc.heading("Welcome to Pynecone!", font_size="2em"),
#            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
#            pc.link(
#                "Check out our docs!",
#                href=docs_url,
#                border="0.1em solid",
#                padding="0.5em",
#                border_radius="0.5em",
#                _hover={
#                    "color": "rgb(107,99,246)",
#                },
#            ),
#            spacing="1.5em",
#            font_size="2em",
#        ),
#        padding_top="10%",
#    )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#import pynecone as pc
#import requests


# In[2]:


#get_ipython().system('pip install pynecone')
# 아까 콘다로 했는데 왜 안깔렸지??


# In[ ]:

class State(pc.State):
    """The app state."""
    count: int =0

    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1

    pass




# def index():
#     return pc.center(
#         pc.vstack(
#             pc.heading(
#                 'click!',
#                 font_size="2rem",
#                 margin_botton=10
#             ),
#             pc.hstack(
#                 pc.button(
#                     "-",
#                     color_scheme="red",
#                     border_radius="1rem",
#                     on_click=State.decrement,
#                     size='1g',
#                 ),
#                 pc.heading(State.count, font_size="2rem"),
#                 pc.button(
#                     "+",
#                     color_scheme="green",
#                     border_radius="1rem",
#                     on_click=State.increment,
#                     size="1g",
#                 ),
#                 spacing="20px",
#             ),
#         ),
#         padding_top ="10%",
#         font_size="2rem"
#     )


# 이래도 멀쩡히 잘 돌아감~!~
def index():
    return pc.center(
        pc.vstack(pc.heading('click!', font_size="2rem", margin_botton=10),
            pc.hstack(pc.button("-", color_scheme="red",border_radius="1rem",on_click=State.decrement,size='1g'),
                      pc.heading(State.count, font_size="2rem"),
                      pc.button("+",color_scheme="green",border_radius="1rem",on_click=State.increment,size="1g"),
                      spacing="20px",
            ),
        ),
        padding_top ="10%",font_size="2rem"
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#app = pc.App(state=State)
#app.add_page(index)
#app.compile()

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
