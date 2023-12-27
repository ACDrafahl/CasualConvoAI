# Research
## 12.26.2023: Behaviors
Today I set up the GPT4All application and downloaded 2 models for testing. The speed of responses seem fast enough for conversations to be tolerably slow, which is a relief. 

Unfortunately, I'm realizing that changing the AI's behavior might be more difficult than I expected. I thought originally that I would perform fine-tuning, but that requires a crazy-powerful GPU, so it's off the table. My other options are prompt engineering and embedding. Admittedly, I don't know much about embedding, but prompt engineering seems like the most manageable option.

I messed around with chatGPT to see what this would look like. This is what we arrived at:

"Your plan sounds well thought out and comprehensive. Let me break down the key components:

Initial Setup with Desired Behaviors:

You prompt the user to provide a list of desired behaviors.
You then use these behaviors to instruct the AI explicitly, setting the tone for the conversation.
Continuation with Speech Recognition and Synthesis:

You use speech recognition to take user input in the form of spoken words.
You employ speech synthesis to provide auditory output, making the interaction more dynamic and engaging.
Onscreen Console for Dynamic Interaction:

You offer an onscreen console with options to the user.
Options include clearing behaviors, adding behaviors, and reinforcing behaviors."

We did a test run, and this worked decently well. The only problem is, when running it with the GPT4All models, they seem to forget instantly how they were supposed to act. If I can't rectify this, I might have to toss the behavioral aspect out the window. (Which would probably be okay; I'm getting a bit overambitious.)

UPDATE: I tried some out of the box methods and got the minstral AI to change its behavior. There may be hope yet. Even if I do move forward though, I will implement this feature much later.  
