from libmproxy.protocol.http import decoded
import json
import HTMLParser
import cgi
import itertools
    
def modifyQuestionResponses(responseContent):
    #Modifies the incomming questions so that the correct one can be spotted
    JSONQuestionResponse=json.loads(responseContent)
    try:
        questions = JSONQuestionResponse["success"]["questions"]
        for question in questions:
            correctAnswerText = question["alt1"]
            answerModifier = "==> "
            modifiedAnswerText = answerModifier + correctAnswerText
            question["alt1"] = modifiedAnswerText
        return json.dumps(JSONQuestionResponse)
    except KeyError:
        pass

def response(context, flow):
    if flow.request.pretty_host(hostheader=True).startswith("quizserver.feomedia.se"):
        print("QF-Response")
        if "qf_games" in flow.request.path:
            with decoded(flow.response):
                questionResponses = (flow.response.content)
                h = HTMLParser.HTMLParser()
                questionResponses = h.unescape(questionResponses)
                modifiedQuestionResponses = modifyQuestionResponses(questionResponses)
                if (modifiedQuestionResponses):
                    flow.response.content = cgi.escape(modifiedQuestionResponses, True);