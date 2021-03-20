from mycroft import MycroftSkill, intent_file_handler


class Ppasseiocachorro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ppasseiocachorro.intent')
    def handle_ppasseiocachorro(self, message):
        self.speak_dialog('ppasseiocachorro')


def create_skill():
    return Ppasseiocachorro()

