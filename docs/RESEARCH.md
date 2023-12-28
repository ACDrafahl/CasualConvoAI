# Research
## 12.27.2023: Behaviors
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
## 12.28.2023: Speech-to-Text
I'm looking into offline solutions for speech-to-text user input. While it's not neccessary for my AI to run without internet, after settling on GPT4All, I've become attached to the idea that this whole project can run without internet access. Plus, avoiding APIs means we can keep this thing entirely free.

The front runner for this is PocketSphinx by CMU Sphinx, although it seems like the setup might be pretty intensive (and I'm not sure how fast it runs yet). Other candidates include VOSK, which seems like it might be kind of slow (but pretty simple to set up,) and OpenAI Whisper, which will probably be too powerful for my pc to run efficiently. 

Looking at online demos, I'm immediately impressed with VOSK's precision and speed. It's way better than I hoped. It seems like CMU Sphinx made this one too, and it's more updated than PocketSphinx. I think I'm going with VOSK.

After some difficulty with the setup, I found something that works. It actually works decently well, which is really exciting. After overriding the overflow exception and changing to a smaller model, I'm able to get pretty consistent results. 
