'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'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'


@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
    '''

#Saim Siddiqui Car Listing page query
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form
    and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        # Ask the user for their car preferences
        gptAPI = GPT(os.environ.get("APIKEY"))
        car_preferences = "List 100 cars that meet these requirements and list their prices and where in United States has most of these cars and list exact links to the car page the car is listed  and mileage the user wants give accordingly the cars with that sort of mileage. "
        # Get the prompt from the form
        prompt = request.form['prompt']
        # Combine the prompt and car preferences into one string
        input_text = f"{prompt}\\n\\n{car_preferences}"
        # Get the GPT response
        answer = gptAPI.getResponse(input_text)
        # Return the response to the user
        return f'''
            <h1>GPT Demo</h1>
            <pre style="background-color: yellow">{prompt}</pre>
            <hr>
            Here is the answer in text mode:
            <div style="border:thin solid black; white-space: pre-wrap">{answer}</div>
            Here is the answer in "pre" mode:
            <pre style="border:thin solid black; white-space: pre-wrap">{answer}</pre>
            <a href="{url_for('gptdemo')}">make another query</a>
        '''
    else:
        return '''
            <h1>Car Listing</h1>
            Write a description of the cars you like:
            <form method="post">
                <textarea name="prompt" rows="5" cols="50"></textarea>


                <input type="submit" value="Submit">
            </form>
        '''
# Harper Pham's Fashion Recommendation page query
def gptfashion():
    ''' handle a get request by sending a form
    and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        # Ask the user for their fashion style
        gptAPI = GPT(os.environ.get("APIKEY"))
        fashion_style = "Enter your fashion style and list your budget and clothing brands to shop and list exact links to the shopping page. "
        # Get the prompt from the form
        prompt = request.form['prompt']
        # Combine the prompt and fashion style into one string
        input_text = f"{prompt}\\n\\n{fashion_style}"
        # Get the GPT response
        answer = gptAPI.getResponse(input_text)
        # Return the response to the user
        return f'''
            <h1>Fashion Style</h1>
            <pre style="background-color: yellow">{prompt}</pre>
            <hr>
            Here is the answer in text mode:
            <div style="border:thin solid black; white-space: pre-wrap">{answer}</div>
            Here is the answer in "pre" mode:
            <pre style="border:thin solid black; white-space: pre-wrap">{answer}</pre>
            <a href="{url_for('gptdemo')}">make another query</a>
        '''
    else:
        return '''
            <h1>Fashion Style</h1>
            Write a description of your fashion style:
            <form method="post">
                <textarea name="prompt" rows="5" cols="50"></textarea>
                <input type="submit" value="Submit">
            </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

    
