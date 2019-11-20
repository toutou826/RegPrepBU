
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from test import getResult
from findRate import findRating

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    body = request.values.get('Body', None)
    resp = MessagingResponse()
    result = getResult(body)
    
    sectionsOutput = f'There are {len(result)} sections for {body}.\n'
    teacherList = []
    for section in result:
        teacherList.append(section.teacher)
        sectionsOutput + f"Section Name: {section.sectionName}, Teacher Name: {section.teacher}, Time: {section.time} \n"

    # ratings = findRating(result)

    resp.message(sectionsOutput)

    # resp.message(ratings)

    return str(resp)