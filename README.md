Quizkampen-hack
==========
This repository contains two small python scripts that are intended to be used with ```mitmproxy``` or ```mitmdump```. ```changeQuestions.py``` modifies the incomming question to the client in such a way that the player can see which one is correct. This is done by prepending a number of blank spaces to the question, causing the text to be slightly off centered in the application. This method allows the hack to be used while someone is watching the screen, since the modification is so minor that it's not apperent to the casual observer.

```changeAnswers.py``` modfies the outgoing request so that all the answers are correct. While this work fine, it's not so useful if someone is watching the screen since the application still shows the user that the chocie is incorrect.

Usage
-----
Start mitmdump with one of the scripts as a variable, with quiet mode activated: ```mitmdump -q -s changeAnswers.py```. This opens a HTTP proxy on the defualt port ```8080```. You can then connect to the proxy using your phone, and it will intercept the trafic and modify it using the script.

Limitations
-----
This have only been tested on the latest version of Quizkampen running on iOS.

