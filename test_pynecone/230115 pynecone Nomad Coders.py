#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pynecone as pc
import requests 


# In[2]:


get_ipython().system('pip install pynecone')
# 아까 콘다로 했는데 왜 안깔렸지??


# In[ ]:


def index():
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
                    size='1g',
                ),
                pc.text("0"),
                pd.button(
                    "+",
                    size="1g",
                ),
                spacing="20px",
            ),
        ),
        padding_top ="10%",
        font_size="2rem"
    )

app = pc.App(state=State)
app.add_page(index)
app.compile()



