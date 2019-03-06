import chatbot

def test_affirmative_responses():
    assert chatbot.affirmative_responses('yes')
    assert chatbot.affirmative_responses('SURE')
    assert chatbot.affirmative_responses('oK')
    assert not chatbot.affirmative_responses('no')
    assert not chatbot.affirmative_responses('')

def test_chat_prompts():
    for count in range(100):
        response = chatbot.chat_prompts()
        assert list(response.keys())[0].__class__ == str
        assert callable(list(response.values())[0])
    