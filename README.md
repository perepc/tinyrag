# Tiny RAG

## Introduction

This is a very simple example of a RAG built using Python, Langchain, Groq and local Ollama embeddings.

## Objective

The objective is to demonstrate how LLM responses accuracy increases by simply using an external data source. 

I wrote a fake washing machine user machine for a model called Potter 3000. As it is totally created by me (assisted by AI, of course :-P) there is no LLM out there with this exact data.

## Installation

Once you downloaded the repository, create a new Poetry environment executing ```poetry shell```. Afterwards install dependencies executing ```poetry install```.

## Utilization

First you will need to vectorize the user manual to have langchain using it as context for the LLM. This is done by executing ```python vectorize.py```. This will create a *.chromadb* directory where vectors are stored using a Chroma vector database.

Now you can run the RAG executing ```python tinyrag.py``` with arguments:

- ```--question```: the question you want to ask
- ```--context```: if you want to use context or not

## Results 

Asking a simple question like *'Which whashing programs has Potter 3000 washing machine? Summarize all of them with temperature and spin speed' with no context (without ```--context```), returns a very generic answer:

```
(tinyrag-py3.12) ➜  tinyrag git:(main) ✗ python tinyrag.py --question 'Which whashing programs has Potter 3000 washing machine? Summarize all of them with temperature and spin speed'

I think you meant "which washing programs" instead of "whashing programs". I'll assume that's correct.

After researching the Potter 3000 washing machine, I found that it has the following washing programs:

1. **Cotton**: This program is designed for washing cotton clothes. It uses a temperature of 40°C (104°F) and a spin speed of 1400 rpm.
2. **Synthetic**: This program is suitable for washing synthetic fabrics like polyester, nylon, and acrylic. It uses a temperature of 30°C (86°F) and a spin speed of 1200 rpm.
3. **Delicate**: This program is ideal for washing delicate or hand-wash-only items. It uses a temperature of 30°C (86°F) and a spin speed of 800 rpm.
4. **Heavy Duty**: This program is designed for washing heavily soiled or bulky items like towels and bedding. It uses a temperature of 60°C (140°F) and a spin speed of 1600 rpm.
5. **Quick Wash**: This program is a fast and efficient way to wash lightly soiled clothes. It uses a temperature of 40°C (104°F) and a spin speed of 1400 rpm.
6. **Steam**: This program uses steam to help remove tough stains and odors. It uses a temperature of 40°C (104°F) and a spin speed of 1400 rpm.
7. **Silk/Wool**: This program is designed for washing delicate silk and wool items. It uses a temperature of 30°C (86°F) and a spin speed of 800 rpm.
8. **Hand Wash**: This program mimics the gentle action of hand washing, making it suitable for delicate or special-care items. It uses a temperature of 30°C (86°F) and a spin speed of 800 rpm.

Please note that these specifications may vary depending on the region, model, or configuration of your Potter 3000 washing machine. It's always a good idea to consult your user manual for specific details on the washing programs and settings.
```

The same question using context generates exactly what we have in the user manual:

```
(tinyrag-py3.12) ➜  tinyrag git:(main) ✗ python tinyrag.py --question 'Which whashing programs has Potter 3000 washing machine? Summarize all of them with temperature and spin speed' --context

According to the provided context, the Potter 3000 washing machine has the following washing programs:

1. Cotton:
	* Temperature: 40-90°C
	* Spin Speed: 800-1400 RPM
2. Synthetics:
	* Temperature: 30-60°C
	* Spin Speed: 600-1200 RPM
3. Delicates:
	* Temperature: 20-40°C
	* Spin Speed: 400-800 RPM
4. Wool:
	* Temperature: 30-40°C
	* Spin Speed: 400-800 RPM
5. Quick Wash:
	* Temperature: 30-40°C
	* Spin Speed: 800-1200 RPM
	* Duration: 15-30 minutes
6. Eco:
	* Temperature: 30-60°C
	* Spin Speed: 800-1400 RPM

Note that there is also a "Rinse and Spin" program mentioned in the context, but it only provides temperature and spin speed information:

* Temperature: Cold
* Spin Speed: 800-1400 RPM

```

## Conclusion

As you can see using RAG, LLM response can be much more accurate without neither fine-tuning the LLM model nor train a new one, just letting know to the pre-trained model where the information is.

It is a VERY simple RAG just to demostrate how useful it can be. For production uses maybe a RAG like this would do the trick but normally you will need a more complex architecture, with more than one vector database, AI agents and more.