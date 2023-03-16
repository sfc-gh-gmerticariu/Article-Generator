import streamlit as st

# Title
st.sidebar.title('WizCase Article Generator (Beta)')

#st.header('This is a header')

# st.subheader('Output Text')

#st.text('This is some body text')

# success, info
# st.success('Success message', icon="🙌")
# st.info('Info message', icon="🔥")
# st.warning('Warning message', icon="⚠️")
# st.error('Error message', icon="💁‍♂️")

# write text (can also write variables)
# st.write('This is some text')
# variable = "this is a variable"
# st.write("This is a variable", variable)

# checkbox
# if(st.checkbox("This is a checkbox")):
#   st.write('You checked the checkbox')

# radio
# radio_value = st.radio('Select an option', ('Option 1', 'Option 2'))
# st.write(radio_value, 'was selected.')

# selection box / dropdown
# dropdown_value = st.selectbox("Select an option", ['Option A', 'Option B', 'Option C'])
# st.write('You selected', dropdown_value)

# multiselection dropdown
# multi_value = st.multiselect('Select multiple options', ['Option A', 'Option B', 'Option C'])
# st.write('You selected ')
# for option in multi_value:
#   st.write(option)

# text input
# text_input = st.text_input('Type some text', 'Start typing')
# st.write('Wow, you typed', text_input)

# button
# if(st.button("Click me, I'm a button")):
#   st.text("Good job pressing that button!")

# slider
# slider = st.slider("Creativity level", 1, 5)
# st.write("Creativity level:", slider)

# 00 - GLOBAL VARIABLES
st.sidebar.header('0: Global Variables')
year_current = 2023

tone_selected = st.sidebar.multiselect('Select the tone of the text.', ['Conversational', 'Informative', 'Professional'])
st.sidebar.write('The tone will be:')
for option in tone_selected:
  st.write(option)

article_title_placeholder = f"How to Watch Out-of-Market {year_current} NFL Games Without Cable"
article_title = st.sidebar.text_input('Enter the article title', article_title_placeholder)
if(article_title):
  st.header(article_title)

  # Make a title generator script

consumer_goal = st.sidebar.text_input('What is the consumer trying to achieve?', placeholder='eg. Watch out-of-market NFL games without cable.')

consumer_problem = st.sidebar.text_input('What problem does ExpressVPN help solve for the consumer?', placeholder='eg. Limited access to NFL games.')

# 01 - INTRODUCTION
section_heading_01 = '1: Introduction'
# st.sidebar.header(section_heading_01)

prompt_input_01 = f"""
You are a tech journalist that reviews VPNs. \n
Write an article introduction for an article about {article_title}. \n 
The tone should be {tone_selected}. \n
The introduction should be written in first-person. \n
The introduction should be 3 paragraphs. \n
Paragraph 1: Start with a personal anecdote describing the consumer's problem. The consumer's problem is {consumer_problem}. \n
Paragraph 2: Agitate the consumer's problem to make it more pressing by mentioning some solutions the consumer might have already considered. \n
Paragraph 3: Gently mention that ExpressVPN was the best solution that you tested, and include a few reasons why it was the best. \n
"""

output_01 = """
  As a die-hard NFL fan, I know the frustration of not being able to watch out-of-market games due to local and national blackouts. You might have already considered purchasing an expensive cable package or subscribing to a streaming service that offers limited access. But what if there was another way? 

After extensive research and testing, I've found that ExpressVPN is the best solution for watching out-of-market 2023 NFL games without cable. With its fast speeds, reliable connections, and easy setup process, you can be sure you won't miss any of your favorite teams' big plays this season. Plus, with its military grade encryption technology and no logs policy, you can rest assured knowing your data is secure while streaming live sports online.
  """

# 02 - QUICK GUIDE
section_heading_02 = f"2: Quick Guide: 3 easy steps to {consumer_goal}."
# st.sidebar.header(section_heading_02)

prompt_input_02 = f"""
You are a tech journalist that reviews VPNs. \n
Write a list of 3 steps based on this article section heading: {section_heading_02}. \n 
The tone should be {tone_selected}. \n
The text must be written in first-person. \n
Each step must be limited to 2 sentences. \n
Step 1 must be about getting a VPN, specifically ExpressVPN. \n
Step 2 must be about connecting to a VPN server that allows the reader to watch the content mentioned in the section title. \n
Step 3 must be about the reader watching the content mentioned in the section title \n

###
Use the following text as a reference for language structure and tone: \n
Get a VPN. ExpressVPN has the fastest servers in 94 countries, so you can get an NFL Game Pass Pro INTL from anywhere.\n
Connect to a server outside the US and sign up for NFL Game Pass Pro INTL. Game Pass shows every game live in Germany, France, India, Brazil, the Netherlands, South Africa, and more.\n
Start streaming every NFL game live from anywhere!\n
"""

output_02 = """
  Step 1: Get ExpressVPN. It has the fastest servers in 94 countries, so you can access NFL Game Pass Pro INTL from anywhere. 

Step 2: Connect to a server outside the US and sign up for NFL Game Pass Pro INTL. This will give you access to live games in Germany, France, India, Brazil, the Netherlands, South Africa and more. 

Step 3: Start streaming every NFL game live from wherever you are! Enjoy watching your favorite teams compete this season!
  """

# 03 - WHY VPN
section_heading_03 = f"03: Why you need a VPN to {consumer_goal}."
section_length_03 = "3 paragraphs"
# st.sidebar.header(section_heading_02)

prompt_input_03 = f"""
You are a tech journalist that reviews VPNs. \n
Write an article section about {section_heading_03}. \n 
The tone must be {tone_selected}. \n
Write in the first-person. \n
The section must be {section_length_03}. \n

Use the following text as a reference for language structure and tone: ### \n
Even though NFL Game Pass Pro is available worldwide, you won’t be able to live stream any regular-season or post-season games with a US Game Pass — you’ll only be able to watch on-demand replays after the game. This is because regular-season games are licensed to networks like CBS, FOX, NBC, ESPN, and Amazon Prime Video. You’ll need subscriptions to multiple streaming platforms to catch every game, which adds up to hundreds of dollars per season.
However, outside the US, UK, Canada, and Ireland, you can buy an international NFL Game Pass Pro with no restrictions. When you buy a Game Pass in countries like Brazil, India, Japan, Germany, and South Africa, you’ll have access to all pre-season, regular-season, and post-season NFL games live! You’ll also have access to extras like NFL RedZone and an entire library of on-demand NFL films and series.
With the help of a VPN, you can spoof your location by connecting to a server in another country. When you connect to a server outside the US, you’ll be able to sign up for an NFL Game Pass Pro INTL and access every game live, including playoffs and the Super Bowl.
"""

output_03 = """
As a tech journalist, I'm often asked why someone would need a VPN to watch out-of-market NFL games. The answer is simple: the NFL has different licensing agreements in different countries, so if you want to stream live regular season and post-season games outside of the US, UK, Canada or Ireland, you'll need an international Game Pass Pro. 

The great thing about this pass is that it gives you access to all pre-season, regular season and post-season NFL games live! You also get extras like NFL RedZone and an entire library of on-demand films and series. But here's the catch - these passes are only available in certain countries. 

That's where a VPN comes in handy! With a VPN service provider like ExpressVPN or NordVPN ,you can easily spoof your location by connecting to a server in another country where an international Game Pass Pro is available. This way you can sign up for the pass without having to physically be there — giving you access to every game live including playoffs and even the Super Bowl!
  """


# GENERATE
if(st.sidebar.button("Generate", key=1)):
  # st.sidebar.text("Introduction baking...")
  
  st.subheader(section_heading_01)
  st.write(output_01)

  st.subheader(section_heading_02)
  st.write(output_02)

  st.subheader(section_heading_03)
  st.write(output_03)