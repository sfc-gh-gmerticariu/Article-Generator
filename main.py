import os
import streamlit as st
import openai

api_key = os.environ['API-KEY']
openai.api_key = api_key

org_key = os.environ['OPEN-AI-ORGANISATION']
openai.organization = org_key

# RETRIEVE OPENAI MODEL
openai.Model.list()
openai.Model.retrieve("text-davinci-003")

# PROMPT FUNCTION
def prompt(input):
  with st.spinner('Writing...'):
    set_prompt = input
    set_max_tokens = 1024
    set_creativity = 0.2 #between 0 and 2
    set_variations = 1
    set_variety_range = 1 #between -2 and 2
    set_uniqueness = 1 #between -2 and 2
  
    output = openai.Completion.create(
    model="text-davinci-003",
    prompt=set_prompt,
    max_tokens=set_max_tokens,
    top_p=1,
    temperature=set_creativity,
    n=set_variations,
    presence_penalty = set_variety_range,
    frequency_penalty = set_uniqueness
  )

  output_list = output.choices

  for item in range(len(output_list)):
    output_dict = output_list[item]
    output_text = output_dict['text']
    return output_text


# Title

st.sidebar.title('WizCase Article Generator (Beta)')

# 00 - GLOBAL VARIABLES
year_current = 2023

tone = st.sidebar.multiselect('Select the tone of the text.', ['Conversational', 'Informative', 'Professional'])

article_title = st.sidebar.text_input('Enter the article title', placeholder = "eg. How to Watch Out-of-Market 2023 NFL Games Without Cable")
if(article_title):
  st.header(article_title)

  # Make a title generator script

consumer_goal = st.sidebar.text_input('What is the consumer trying to achieve?', placeholder='eg. Watch out-of-market NFL games without cable.')

consumer_problem = st.sidebar.text_input('What problem does ExpressVPN help solve for the consumer?', placeholder='eg. Limited access to NFL games.')

# PROMPT HEADER
prompt_header = f"""
You are a tech journalist that reviews VPNs. \n
Your writing is {tone}.\n
You write in the first-person and talk directly to your readers.\n
"""

# services_dict = {
#   "ExpressVPN": {"ksp": 
#     "Ultra-Fast Worldwide Servers", "features": ['3000+ servers in 94 international locations.', 'Unbeatable server speeds.', 'Connect up to 5 devices at a time.','Support via email, 24/7 live chat, troubleshooting guides, and video tutorials.', '30-Day money-back guarantee.']
#   },
#   "CyberGhost": {
#     "ksp": "KSP 1",
#     "features": ['Feature 1.', 'Feature 2', 'Feature 3.','Feature 4.', 'Feature 5']
#   },
#   "Private Internet Access": {
#     "ksp": "KSP 1",
#     "features": ['Feature 1.', 'Feature 2', 'Feature 3.','Feature 4.', 'Feature 5']
#   },
#   "NordVPN": {
#     "ksp": "KSP 1",
#     "features": ['Feature 1.', 'Feature 2', 'Feature 3.','Feature 4.', 'Feature 5']
#   },
#   "Surfshark": {
#     "ksp": "KSP 1",
#     "features": ['Feature 1.', 'Feature 2', 'Feature 3.','Feature 4.', 'Feature 5']
#   },
# }

# ACCESS SERVICE NAME, KSP, AND FEATURE LIST FROM DICTIONARY
# for key1 in services_dict:
#   st.write(key1)
#   st.write(services_dict[key1]["ksp"])
#   for feature in services_dict[key1]["features"]:
#     st.write(feature)

# services_select = st.sidebar.multiselect('Select the services being reviewed.', services_dict.keys())

# 01 - INTRODUCTION
section_heading = '01: Introduction'
st.sidebar.subheader(section_heading)

prompt_input = f"""
{prompt_header}\n
Write a 3-paragraph article introduction for an article about {article_title}. \n 
Start with a personal anecdote describing the consumer's problem. The consumer's problem is {consumer_problem}. \n
Agitate the consumer's problem to make it more pressing by mentioning some solutions the consumer might have already considered, and mention why they wouldn't work. \n
Mention that ExpressVPN was the best VPN that you tested, and include a few reasons why it was the best. \n
\n
Use the following text as a reference for length, language structure, and tone: \n
###
As a fan of American football, I find it very frustrating that I can’t watch out-of-market games — even when I’m paying to watch them on Hulu. Even with a Sunday Ticket, I still don’t have access to every live game or NFL Network. Thankfully, Game Pass Pro INTL gives me access to all 250+ live NFL games (including playoffs and the Super Bowl), NFL RedZone, and more.

If you’re in the US, you’ll need a VPN to sign up for NFL Game Pass Pro INTL. While Game Pass is available in the US, the domestic (US) version doesn’t broadcast any regular-season games live — you’ll only have access to full replays once the game ends.

With lightning-fast speeds and servers in 94+ countries, ExpressVPN is my top recommendation to watch every NFL game live. You can try ExpressVPN with NFL Game Pass completely risk-free. Thanks to its 30-day money-back guarantee, you can get a refund if you’re not happy.
"""

if(st.sidebar.button("Write for me", key=1)):
  st.write(prompt(prompt_input))

# 02 - QUICK GUIDE
section_heading = f"02: Quick Guide: 3 easy steps to {consumer_goal}."
st.sidebar.subheader(section_heading)

prompt_input = f"""
{prompt_header}\n
Write a list of 3 steps based on this heading: {section_heading}. \n 
Each step must be limited to 2 sentences. \n 
\n
Step 1 must be about getting a VPN, specifically ExpressVPN. \n
Step 2 must be about connecting to a VPN server that allows the reader to watch the content mentioned in the section title. \n
Step 3 must be about the reader watching the content mentioned in the section title \n
"""

if(st.sidebar.button("Write for me", key=2)):
  st.subheader(section_heading)
  st.write("PROMPT:")
  st.write(prompt_input)
  st.write("OUTPUT:")
  st.write(prompt(prompt_input))

# 03 - WHY VPN
section_heading = f"03: Why you need a VPN to {consumer_goal}."
st.sidebar.subheader(section_heading)

prompt_input = f"""
{prompt_header}
Write 3 paragraphs about {section_heading}. \n 

Use the following text as a reference for language structure and tone:\n
### \n
Even though NFL Game Pass Pro is available worldwide, you won’t be able to live stream any regular-season or post-season games with a US Game Pass — you’ll only be able to watch on-demand replays after the game. This is because regular-season games are licensed to networks like CBS, FOX, NBC, ESPN, and Amazon Prime Video. You’ll need subscriptions to multiple streaming platforms to catch every game, which adds up to hundreds of dollars per season.
However, outside the US, UK, Canada, and Ireland, you can buy an international NFL Game Pass Pro with no restrictions. When you buy a Game Pass in countries like Brazil, India, Japan, Germany, and South Africa, you’ll have access to all pre-season, regular-season, and post-season NFL games live! You’ll also have access to extras like NFL RedZone and an entire library of on-demand NFL films and series.
With the help of a VPN, you can spoof your location by connecting to a server in another country. When you connect to a server outside the US, you’ll be able to sign up for an NFL Game Pass Pro INTL and access every game live, including playoffs and the Super Bowl.
"""

if(st.sidebar.button("Write for me", key=3)):
  st.subheader(section_heading)
  st.write("PROMPT:")
  st.write(prompt_input)
  st.write("OUTPUT:")
  st.write(prompt(prompt_input))


# 04: BEST VPNS
st.sidebar.subheader("04: Best VPNs")
vpn_name = st.sidebar.text_input("What VPN?", placeholder='VPN Name')

ksp_01 = st.sidebar.text_input("Key Feature #1", placeholder='Key Feature #1')
key_benefit_01 = st.sidebar.text_input("Key Benefit #1", placeholder='Key Benefit #1')

ksp_02 = st.sidebar.text_input("Key Feature #2", placeholder='Key Feature #2')
key_benefit_02 = st.sidebar.text_input("Key Benefit #2", placeholder='Key Benefit #2')

features = st.sidebar.text_area("Features", placeholder = "VPN Features")

section_heading = f"{vpn_name} — {ksp_01} to {key_benefit_01}"

prompt_features_list = f"""
{prompt_header}\n
Rewrite the following text as a bullet list: \n
{features}.\n
\n

Use the following text as a reference for language structure and tone: \n
###
- 3000+ servers in 94 international NFL broadcasting locations\n
- Unbeatable server speeds with no buffering or lag to interrupt your Sunday games\n
- Connect up to 5 devices at the same time\n
- Support via email, 24/7 live chat, troubleshooting guides, and video tutorials on the website\n
- 30-day money-back guarantee\n
"""

prompt_par_01 = f"""
{prompt_header}\n
Write a 4-sentence paragraph expanding on the following {vpn_name} feature and what it helps the reader achieve:\n
{ksp_01} helps the reader {key_benefit_01}.\n
\n
Start with mentioning the key feature and what it helps the reader achieve.\n
Include a personal experience related to the key feature.\n

Use the following text as a reference for language structure and tone: \n
###
ExpressVPN is your best bet for watching every NFL game live from anywhere, thanks to its 3000+ ultra-fast worldwide servers. While connected to local and distant servers, ExpressVPN delivered consistently high speeds and never caused more than a 17% reduction from my baseline speeds. At around 100Mbps, I never had to worry about mid-game buffering or lag. This is especially comforting when watching Bucs games since you never know which game will be Tom Brady’s last.
"""

prompt_par_02 = f"""
{prompt_header}\n
Write a 4-sentence paragraph expanding on the following {vpn_name} feature and what it helps the reader achieve:\n
{ksp_02} helps the reader {key_benefit_02}.\n
\n
Start with mentioning the key feature and what it helps the reader achieve.\n
Include a personal experience related to the key feature.\n

Use the following text as a reference for language structure and tone: \n
###
You can use Smart DNS on devices that don’t usually support VPNs, including Samsung and LG TVs, Xbox, PlayStation, and Apple TV — all of which have dedicated Game Pass apps. Once you connect to one of CyberGhost’s DNS servers in the Netherlands, Germany, or Japan, you’ll be able to access your NFL Game Pass Pro INTL and watch every game live on a big screen.
"""

prompt_par_pricing = f"""
{prompt_header}\n
Write a 4-sentence paragraph describing {vpn_name}'s pricing and refund policy.\n
Mention how {vpn_name}'s compares to other VPNs.\n
Mention if there are discounts for long-term subscriptions. \n
Include a personal experience related to the pricing, discounts, or refunds.\n

Use the following text as a reference for language structure and tone: \n
###
Although ExpressVPN costs slightly more than other VPNs on this list, its unmatched speeds and compatibility make it more than worth the price. Plus, you can get a 49% discount on a 1-year + 3 months plan (it’s just $6.67/month). All subscriptions are backed by a 30-day money-back guarantee. That means you can try ExpressVPN with NFL Game Pass Pro at no risk to you. If you’re not happy with the service, you can get a full refund. When I tested the policy for myself, my refund was approved via 24/7 live chat with no questions asked. The money was back in my bank account 2 days later.
"""

if(st.sidebar.button("Write for me", key=4)):
  st.header(section_heading)
  st.write("[HERO IMAGE GOES HERE]")
  st.subheader("Key Features:")
  st.write(prompt(prompt_features_list))
  st.write(prompt(prompt_par_01))
  st.write(prompt(prompt_par_02))
  st.write("[IMAGE GOES HERE]")
  st.write(prompt(prompt_par_pricing))
  st.write(f"{vpn_name} unblocks:")
  st.write(f"{vpn_name} works on:")
