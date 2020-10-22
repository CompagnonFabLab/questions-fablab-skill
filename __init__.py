from mycroft import MycroftSkill, intent_file_handler


class QuestionsFablab(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fablab.questions.intent')
    def handle_fablab_questions(self, message):
        self.speak_dialog('fablab.questions')


def create_skill():
    return QuestionsFablab()

