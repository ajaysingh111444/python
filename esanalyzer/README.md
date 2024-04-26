# esanalyzer
The Python Emotion and Sentiment Analysis library you've been looking for.


## Services
- Emotion Analysis("fear", "anger", "surprise", "sadness", "disgust", "joy")
- Sentiment Analysis("Positive","Negative")
- Multi Language Support


## Usage
- Install using `pip install esanalyzer`


```python 


	from esanalyzer import EmotionAnalyzer

	# Create an instance of EmotionAnalyzer
	analyzer = EmotionAnalyzer()

	# Call the analyze method with the text
	text = "Wow, I am so happy"
	result = analyzer.analyze(text)

	# Use the result as needed
	print(result)
	
	{'library': 'default', 'result': {'surprise': 80}, 'max_prediction': {'label': 'surprise', 'percentage': 80}, 'sentiment': 'Positive', 'sentiment_score': 0.999592125415802, 'threshold_value': 0.8}
	

```