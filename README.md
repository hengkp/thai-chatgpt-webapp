# Thai ChatGPT Web Application

Welcome to the Thai ChatGPT Web Application! This project is a demonstration of using OpenAI's GPT-3 model to build a chatbot in the Thai language.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Before you begin, make sure you have the following dependencies installed:

- Python 3.6 or higher
- Flask
- Hugging Face's transformers library
- pandas
- requests
- bs4 (beautifulsoup4)

You can install these dependencies by running the following command:


### Installing
To get the project up and running on your local machine, follow these steps:

1. Clone the repository to your local machine
```
git clone https://github.com/hengkp/thai-chatgpt-web-application.git
```

2. Navigate to the project directory
```
cd thai-chatgpt-web-application
```

3. Install the required packages
```
pip install -r requirements.txt
```

4. Replace `<your_api_key>` in `app.py` with your own OpenAI API key.<br>
You can get by signing up for an account [here](https://beta.openai.com/signup/)

5. Run the app
```
python app.py
```

6. Open your browser and go to http://localhost:5000 to see the application running

## Data Collection

The data used to train the Thai ChatGPT model was collected from various websites using the scraper.py file. The script goes to each website, extracts the text, and stores it in a structured format in a .csv file.

## Model Training

The model.py file contains the code for training the Thai ChatGPT model using the collected data. The script fine-tunes the GPT-3 model on the dataset and saves the trained model to be used in the web application.

## Deployment

The Thai ChatGPT web application can be deployed on a hosting service such as Heroku or GitHub Pages.

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - The web framework used
- [OpenAI GPT-3](https://openai.com/docs/api-reference/introduction/) - Thai language model
- [Hugging face's transformers](https://huggingface.co/transformers/) - Used to fine-tune GPT-3 model
- [pandas](https://pandas.pydata.org/) - Used for data manipulation
- [requests](https://pypi.org/project/requests/) - Used for sending HTTP requests
- [bs4](https://pypi.org/project/beautifulsoup4/) - Used for web scraping

## Acknowledgements

- Special thanks to OpenAI for providing the GPT-3 model and API access.
- The code for this project was heavily influenced by the examples provided by OpenAI and [this tutorial](https://www.twilio.com/blog/how-to-build-a-chatbot-with-openai-gpt-3-and-python).

## Authors

**Kriengkrai Phongkitkarun** - *Initial work* - [hengkp](https://github.com/hengkp)
