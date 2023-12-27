# CasualConvoAI 
<p align="center"><img src="https://github.com/ACDrafahl/CasualConvoAI/assets/118315981/dccd8cfa-10f6-4916-bf58-aa5ac086f420" width="250" ><br><h1 align="center"></h1>
</p>

A locally hosted AI that runs on consumer level hardware using an existing LLM (Large Language Model) and user-end fine tuning for desired behaviors. The AI will respond to verbal user input and respond with speech synthesis. If possible, the AI will also feature a visual representation of speech (such as an avatar) to give it approachability and character.

# Research Findings
Through my research I’ve arrived at a general outline for development requirements and potential limitations:
## Requirements
1. The AI must run locally on typical consumer hardware so as to avoid costly API services to existing commercial LLMs and offer full flexibility for use in the application.
2. The speech recognition and speech synthesis model must also be free and accessible locally.
## Limitations
1. Searching exclusively for local LLMs greatly reduces the options available. GPT-4 is by far the easiest to implement, but the API is costly. Llama 2 can run free locally and is available for research and even commercial purposes, but it requires a substantial GPU, which breaks the consumer hardware requirement. One of the only options left is GPT4ALL, which is slower, but runs on a cpu with lower ram and storage requirements than most all LLMs.
2. Similar problems occur with the speech synthesis. ElevenLabs is ideal, as it offers a wide range of expressive vocal AI voices, but again, costs are high. Instead, an older, open source model will probably have to be used. On the bright side, speech recognition, at least from my first impressions, should be fairly easy to integrate and won’t incur costs.

# Process
## I. Documentation
I will have to research how to properly document my progress on GitHub throughout development. The goal is to make this repository easy to navigate and simple to understand, despite the more complicated subject matter.
## II. Divide and Conquer
Since this project has widely differing facets that are daunting when approached all at once, and because I alone am the entirety of the Research and Development Department, I plan on breaking this project into comprehensive chunks. 
  ### A. Speech Recognition as User Input
  This should be one of the easiest parts of the project, and as user input is needed before receiving AI responses, it should support the process of following steps. 
  ### B. LLM Integration
  This is the most difficult step of the project by far, and also the most important. It will require further research about the GPT4ALL model and, likely, many hours of 
  troubleshooting.
  ### C. Speech Synthesis
  The final hurdle. Besides the difficulty of finding a solid model, this, like point A, should be fairly straightforward. If I decide to add visuals, this step gets worse.
## III. Testing
Of course, this will be necessary at every step. However, once the groundwork is laid, testing is a matter of training the AI itself.


