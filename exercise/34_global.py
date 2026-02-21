# communicator.py

# Global credit variable
credit = 10


def sendsms(mobile_no, message):
    global credit
    if credit >= 2:
        credit -= 2
        print(f"SMS sent to {mobile_no}: {message}")
        print(f"Remaining credit: {credit}")
    else:
        print("Insufficient credit to send SMS.")


def sendWhatmsg(mobile_no, message):
    global credit
    if credit >= 1.5:
        credit -= 1.5
        print(f"WhatsApp message sent to {mobile_no}: {message}")
        print(f"Remaining credit: {credit}")
    else:
        print("Insufficient credit to send WhatsApp message.")


def sendEmail(email, message):
    global credit
    if credit >= 1:
        credit -= 1
        print(f"Email sent to {email}: {message}")
        print(f"Remaining credit: {credit}")
    else:
        print("Insufficient credit to send Email.")


def increaseCredit(points):
    global credit
    if points > 0:
        credit += points
        print(f"Credit increased by {points}.")
        print(f"Total credit: {credit}")
    else:
        print("Points must be positive to increase credit.")