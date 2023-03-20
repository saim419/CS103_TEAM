'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="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"  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="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" # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey='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'
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    '''Saim Siddiqui'''
    def getCarPreferences():
        type_of_car = input("Do you prefer sport or normal cars? ")
        age_of_car = input("Do you prefer a new or an old car? ")
        brand_of_car = input("Which brand do you prefer? ")
        return "You prefer a {age_of_car} {type_of_car} car from the {brand_of_car} brand."
    
   @app.route('/gptdemo', methods=['GET', 'POST'])
   def gptdemo():
       ''' handle a get request by sending a form 
       and a post request by returning the GPT response
       '''
       if request.method == 'POST':
        # Ask the user for their car preferences
          gptAPI = GPT(os.environ.get("APIKEY"))
          car_preferences = gptAPI.getCarPreferences()
         # Get the prompt from the form
          prompt = request.form['prompt']
         # Combine the prompt and car preferences into one string
          input_text = f"{prompt}\n\n{car_preferences}"
        # Get the GPT response
          answer = gptAPI.getResponse(input_text)
        # Return the response to the user
          return f'''
            <h1>GPT Demo</h1>
            <pre style="bgcolor:yellow">{prompt}</pre>
            <hr>
            Here is the answer in text mode:
            <div style="border:thin solid black">{answer}</div>
            Here is the answer in "pre" mode:
            <pre style="border:thin solid black">{answer}</pre>
            <a href={url_for('gptdemo')}> make another query</a>
            '''
         else:
              return '''
            <h1>GPT Demo App</h1>
            Enter your query below
            <form method="post">
                <textarea name="prompt" rows="5" cols="50"></textarea>
                <br>
                <input type="submit" value="Submit">
            </form>
                    '''


if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
