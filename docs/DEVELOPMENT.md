# Development
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

UPDATE: I tried some out of the box methods and got the minstral AI to change its behavior. There may be hope yet. Even if I do move forward though, I will implement this feature much later. I might also look into importing external AI's, as I just found out GPT4All can run some of those as well. 

## 12.28.2023: Speech-to-Text
I'm looking into offline solutions for speech-to-text user input. While it's not neccessary for my AI to run without internet, after settling on GPT4All, I've become attached to the idea that this whole project can run without internet access. Plus, avoiding APIs means we can keep this thing entirely free.

The front runner for this is PocketSphinx by CMU Sphinx, although it seems like the setup might be pretty intensive (and I'm not sure how fast it runs yet). Other candidates include VOSK, which seems like it might be kind of slow (but pretty simple to set up,) and OpenAI Whisper, which will probably be too powerful for my pc to run efficiently. 

Looking at online demos, I'm immediately impressed with VOSK's precision and speed. It's way better than I hoped. It seems like CMU Sphinx made this one too, and it's more updated than PocketSphinx. I think I'm going with VOSK.

After some difficulty with the setup, I found something that works. It actually works decently well, which is really exciting. After overriding the overflow exception and changing to a smaller model, I'm able to get pretty consistent results. 

## 12.29.2023: Implementing GPT4All
Slight update on the behavioral customization: GPT4All seems to have a built-in template system that will make this way easier, which is incredible. Essentially it uses a form of prompt engineering that tacks a desired behavior on to the end of every response, i.e., "hi, who are you? [Respond like a pirate]." That behavior will be hidden, so to the user, it simply seems that the behavior has been permanently altered. 

Otherwise, I've been able to successfully get the model up and responding to manually typed prompts. 

## 1.3.2023: Killing Vosk Once and for All
I have wrestled with vosk for several days now, desperately trying to get clean output from it based on push-to-talk input, only to get glimmers of hope that were snuffed out again and again. It is no longer worth my time, nor is it a viable means of completing this project. As much as I hate to say it, it's back to the drawing board. I'm looking into Whisper.ai again, since it has some lighter models that might work on my cpu, and there's an existing repository called whisper-mic that should allow for near-real-time input with decently straightforward functionality. At this point, I'll try anything. 

Upon just testing Whisper for a minute or so, it's already worlds better than vosk. I'm talking out of the package, comprehensive speech recognition with PUNCTUATION built in. It's insanely good, and I did confirm that it still runs without Wi-Fi, so the constraints of the project remain intact. 

## 1.5.2023 Successfully Linking Whisper and GPT4All
After plenty of research and several different approaches, I was able to get Whisper running with push-to-talk using the space bar. After that, all I had to do was bring in the working GPT4All code and feed in the input text as a prompt. It was definitley a eureka moment when I said "Hello," and after about ten seconds, the system responded back, "Hello, how may I help you today?" This is a huge step, and I don't want to diminish that triumph, but there's still so much more to do. I need to polish this code, but for now I'm going to move on to speech synthesis. 

From my research, I've found a few candidates: Coqui TTS, TorToiSe, and Piper. Coqui looks pretty promising, so I'll probably start with that one. TorToiSe is known for being slow (hence, tortoise,) but there might be ways to speed it up. Piper is not very realistic, but it is fast, and if worst come to worst, I can default to that or built in python TTS, since they're basically on the same level. 

## 1.8.2023 Testing TTS
After some tedious difficulties with setup, I was able to get Coqui working. However, running a simple sentence took almost a minute, and with speech-to-text and AI generation already taking time on their own, I'm not willing to tack on that much time for a response. Even without those barriers, it would be a dull conversation. 

So, I'm trying out Piper. 
