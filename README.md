# Webpage-Socket-Practice
This is a simple program of a Webpage form to practice Socket Programming. It's simply using the submitted field to parse an existing data (```parse.txt```) and respond to user accordingly.


<br>

## Getting Started
This program includes the following files:
- ```Webpage Form.py```: the main scripting file to run as a server.
- ```parse.txt```: which is represented as the database. It includes the dataset that will be compared with user's inputs.
- ```main.html```: which is the homepage containing the form that the user will use to submit.
- ```OK.html```: a basic success page that the user will be forward to whenever parsing returns positive.
- ```NOT_OK.html```: a basic success page that the user will be forward to whenever parsing returns negative.


<br>

## Usage
1. Run the server file ```Webpage Form.py```.
2. Click on the localhost link that the server will provide to you to go to the main page.
3. Fill the form, then click "Submit"
4. If the submitted information exist in ```parse.txt```, you will be forwarded to ```OK.html``` page indicating success. Otherwise, you will be forwarded to ```NOT_OK.html``` page indicating failure (or the data doesn't exist).


<br>

#### Important Note: 
It's important to mention that you might face some issues like Connection Aborted Error. There several reason for this problem such as presense of anti-virus, firewall blocking the port, network configuration or many other reasons. Instead of investigating and disabling them, I would recommend opening the page in private browsing mode (e.g. Incognito).

