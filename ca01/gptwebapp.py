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


#Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'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'



@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Team Monsters</h1>
       
        <a href="{url_for('gptCars')}">Ask questions to GPTCars</a>
        <br></br>
        <a href="{url_for('gptMusic')}">Ask questions to GPTMusic</a>
        <br></br>
        <a href="{url_for('gptFashion')}">Ask questions to GPTFashion</a>
        <br></br>
        <a href="{url_for('about')}">About Page</a>
    '''

#Saim
@app.route('/gptCars', methods=['GET', 'POST'])
def gptCars():
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
            <a href="{url_for('gptCars')}">make another query</a>
            <br></br>
            <a href="{url_for('index')}">back to Home</a>
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
@app.route('/gptFashion', methods=['GET', 'POST'])
def gptFashion():
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
            <a href="{url_for('gptFashion')}">make another query</a>
            <br></br>
            <a href="{url_for('index')}">back to Home</a>
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

@app.route('/gptMusic', methods=['GET', 'POST'])
def gptMusic():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        gptAPI = GPT(os.environ.get("APIKEY"))
        musicPreferences = "List three musical artists similar to these"
        
        prompt = request.form['prompt']

        input_text = f"{prompt}\n\n {musicPreferences}"

        answer = gptAPI.getResponse(input_text)
        return f'''
            <h1>GPT Music</h1>
            <pre style="bgcolor:yellow">{prompt}</pre>
            <hr>
            Here is the answer in text mode:
            <div style="border:thin solid black">{answer}</div>
            Here is the answer in "pre" mode:
            <pre style="border:thin solid black">{answer}</pre>
            <a href={url_for('gptMusic')}> make another query</a>
            <br></br>
            <a href="{url_for('index')}">back to Home</a>
        '''
    else:
        return '''
        <h1>GPT Music</h1>
        List your 5 favorite Music artists
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
@app.route('/about',methods=['GET', 'POST'])   
def about():
    return f'''
    <h1>{{ Saim Siddiqui }}'s Car Listing</h1>

    <p>Write a description of the cars you like::</p>

    <pre>{{list sports cars}}</pre>

    <p>GPT's response:</p>

    <pre>{{ 1. Porsche 911 Carrera 4S Cabriolet - $123,514 - Most of these cars are available in California; https://www.porsche.com/usa/models/911/911-carrera-4s-cabriolet/ - Up to 24 MPG

    2. Jaguar F-Type SVR Convertible - $127,595 - Most of these cars are available in Florida; https://www.jaguarusa.com/all-models/f-type/f-type-svr/index.html - Up to 22 MPG
    
    3. Mercedes-Benz AMG GT Roadster - $149,000 - Most of these cars are available in New York; https://www.mbusa.com/en/vehicles/mercedes-benz/amg/amg-gt-roadster - Up to 21 MPG
    
    4. BMW M8 Convertible - $142,195 - Most of these cars are available in Texas; https://www.bmwusa.com/vehicles/m-models/m8-convertible.html - Up to 24 MPG
    
    5. Audi R8 Spyder - $169,900 - Most of these cars are available in California; https://www.audiusa.com/models/audi-r8-spyder - Up to 19 MPG
    
    6. Lamborghini Huracan LP610-4 Spyder - $280,000 - Most of these cars are available in California; https://www.lamborghini.com/en-en/models/huracan/huracan-spyder - Up to 18 MPG
    
    7. Aston Martin V12 Vantage S Roadster - $172,743 - Most of these cars are available in Florida; https://www.astonmartin.com/en-us/models/vantage/vantage-s/roadster - Up to 16 MPG
    
    8. Maserati GranTurismo Convertible - $151,790 - Most of these cars are available in California; https://www.maseratiusa.com/gran-turismo-convertible - Up to 17 MPG
    
    9. Nissan GT-R Nismo - $177,030 - Most of these cars are available in California; https://www.nissanusa.com/vehicles/sports-cars/gt-r-nismo.html - Up to 17 MPG
    
    10. Cadillac ATS-V Coupe - $62,890 - Most of these cars are available in California; https://www.cadillac.com/ats-sedan/ats-v-coupe - Up to 21 MPG }}</pre>

    <a href="{url_for('gptCars')}">Ask questions to GPTCars</a>


    <h1>Jaden's Page</h1> 

    <p>Tell GPT your favorite Music Artists:</p>

    <pre>{{List three musical artists similar to these}}</pre>

    <p>GPT's response:</p>

    <pre>{{1. Chance the Rapper
        2. J. Cole
        3. Kid Cudi}}</pre>

    <a href="{url_for('gptMusic')}">Ask questions to GPTMusic</a>

    <h1>Harper's Fashion Style</h1>
    <p>Write a description of your fashion style:</p>

    <pre>{{List clothing items that match the preferences}}</pre>

    <p>GPT's response:</p>

    <pre>{{1. Brandy Melville Reese Denim Skirt ($42)
    2. Brandy Melville Crop Pocket Tee ($20)
    3. Brandy Melville Pink Logo Patch Hat ($25)
    4. Brandy Melville Daisy Print Shorts ($35)
    5. Brandy Melville Cropped Mesh Tank ($30)
    6. Brandy Melville Eyelet Shorts ($35)
    7. Brandy Melville Chevron Print Shirt ($45)
    8. Brandy Melville Striped Drawstring Shorts ($25)
    9. Brandy Melville Tie Front Shirt ($35)
    10. Brandy Melville Gingham Romper ($45)}}</pre>

    <a href="{url_for('gptFashion')}">Ask questions to GPTFashion</a>'''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
