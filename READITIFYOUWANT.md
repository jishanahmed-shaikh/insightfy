1. Ensure PYTHON 3.11 or above is installed on your system and Clone the Repository, Make Sure you are in the 'insightify' Directory.
2. Make sure to download all the required Libraries for the project mentioned in the requirements.txt by using the following command
    pip install -r requirements.txt
3. Make sure to install Python libraries :
    nltk.download('vader_lexicon')
    nltk.download('punkt')
    nltk.download('stopwords')
    .......................... and more as the program would ask after running "STEP 4" and testing the Web Application
4. Use this command to run the server: "uvicorn app.main:app --reload"
5. Happy Coding