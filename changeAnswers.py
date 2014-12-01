from libmproxy.protocol.http import decoded
import urllib
import json
import itertools


def modifyAnswerRequest(requestContent):
    #Changes the last answers to the correct ones
    JSONGameUpdate = requestContent.split("=",1)[-1]
    gameUpdate = json.loads(JSONGameUpdate)
    my_answers=gameUpdate["my_answers"]
    modifiedAnswers = list(itertools.repeat("0", len(my_answers)))
    modifiedAnswersString = "".join(modifiedAnswers)
    gameUpdate["my_answers"] = modifiedAnswersString 
    return json.dumps(gameUpdate)
    
def request(context, flow):
    """
        Called when a client request has been received.
    """
    if flow.request.pretty_host(hostheader=True).startswith("quizserver.feomedia.se"):
        contentString = urllib.unquote_plus(flow.request.content)
        if contentString.startswith("game_update"):
            print("game_update")
            modifiedAnswer = modifyAnswerRequest(contentString)
            flow.request.content = "game_update="+urllib.quote(modifiedAnswer)