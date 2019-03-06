import chatbot

def test_affirmative_responses():
    r, next_fun = chatbot.affirmative_responses()
    assert r == 'a' or r == 'b' or r == 'c'
    assert callable(next_fun) == True