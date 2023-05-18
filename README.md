# slack-chat-bot
A Slack chat bot that can index an arbitrary website and have relevant conversations. Built using LangChain, llama-index, and slack_bolt. 

To index an arbitrary site, use the `wget` command to replace the current contents of `sitemap/`. 
**Remember to include environment variables `SLACK_APP_TOKEN`, `SLACK_BOT_TOKEN`, and `OPENAI_API_KEY`! 
**

Steps taken to build this:
1. Create a local mirror of desired website to index. 
2. Learn NLP basics and set up a basic chatbot in Jupyter Notebook using LangChain and lama-index. 
3. Set up a Slack app in Socket mode. 
4. Enable basic, manual interaction in the Slack app (check for event listening and the ability to send messages as the bot).
5. Integrate the chatbot with Slack to automatically generate responses for messages. 

This bot can be further enhanced by tinkering with finer details such as customized responses for various event possibilities (like reactions to messages, app mentions, and more). Coverage can be added for slash commands and incoming webhooks, as well as FAQ-like suggestions for what to ask. 

This bot is currently operating in Socket mode, which allows for the bot to be used in workspaces without a public HTTP Request URL. It could be made public and distributable with a redirect URL. 

Some examples of ineraction this bot is capable of: 

<img width="518" alt="Screen Shot 2023-05-18 at 11 53 54 AM" src="https://github.com/snpal/slack-chat-bot/assets/31996868/1d404bc4-7f53-47e4-ba77-824d676a4898">

<img width="517" alt="Screen Shot 2023-05-18 at 11 49 59 AM" src="https://github.com/snpal/slack-chat-bot/assets/31996868/1c0d0c9c-b957-4785-8ca7-3cefdb5563b9">

<img width="599" alt="Screen Shot 2023-05-18 at 11 50 23 AM" src="https://github.com/snpal/slack-chat-bot/assets/31996868/9cfdfe7c-433d-4a57-a35d-f507ee16093b">

<img width="500" alt="Screen Shot 2023-05-18 at 11 49 24 AM" src="https://github.com/snpal/slack-chat-bot/assets/31996868/8ccdeb2a-498d-4ab0-badd-3820a92e023b">

<img width="515" alt="Screen Shot 2023-05-18 at 11 52 11 AM" src="https://github.com/snpal/slack-chat-bot/assets/31996868/578a86f8-e66a-4736-bab7-0013efebf958">

<img width="500" alt="Screen Shot 2023-05-18 at 11 52 40 AM" src="https://github.com/snpal/slack-chat-bot/assets/31996868/3d6f6995-7c8a-42e0-9f8a-e373424164ef">
