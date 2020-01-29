# WhatsApp chat analyser   
Analysing WhatsApp chats for the following data:
* The number of messages sent by each of you
* The average length of your messages
* Who texts first and the first text in each conversation
* Your chatting time patterns — hourly, daily, and monthly
* Most shared website links (todo)
* Most common words that each of you use

#### Code according this [guide](https://medium.com/better-programming/https-medium-com-nityeshagarwal-whatsapp-chat-analyser-a-guided-project-7d21e033109d)
  
#### Chat export [guide](https://www.guidingtech.com/export-whatsapp-chat-pdf/)  

  
#### Running (On Mac)  
* [Install virtual env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments) 
> python3 -m pip install --user virtualenv
* Create a virtual environment  (root dir of the project)
> python3 -m venv env
* Activate the virtual environment 
> source env/bin/activate
* Install dependencies 
> pip install -r requirements.txt --user
* Run 
> cd module 
> python3  whatsapp-analyser.py

#### ToDo
* Add tests
* Change data structures (maybe use a database?)
* Automate chat export (requires WhatsApp authentication)
* Get the chat file from environment variable/parameter or as input
* Improve data visualization