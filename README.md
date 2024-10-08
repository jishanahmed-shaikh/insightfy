1. Ensure PYTHON 3.11 or above is installed on your system and Clone the Repository, Make Sure you are in the 'insightfy' Directory.
2. (You can Create a Virtual Environment "venv" for the project) Make sure to download all the required Libraries for the project mentioned in the requirements.txt by using the following command pip install -r requirements.txt
3. Make sure to install Python libraries :
   - nltk.download('vader_lexicon')
   - nltk.download('punkt')
   - nltk.download('stopwords')
   - .......................... and more as the program would ask after running "STEP 4" and testing the Web Application
5. Use this command to run the server: "uvicorn app.main:app --reload"
6. Happy Coding
