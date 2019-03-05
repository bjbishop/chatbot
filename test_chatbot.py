import chatbot


def test_names_game():
    results = chatbot.name_game("Amanda").splitlines()
    assert results[0] == "amanda, amanda, bo-bamanda"
    results = chatbot.name_game("Stan").splitlines()
    assert results[0] == "stan, stan, bo-ban"
    results = chatbot.name_game("Bryan").splitlines()
    assert results[0] == "bryan, bryan, bo-byan"

def test_swear_word():
    results = chatbot.name_game("Chuck").splitlines()
    assert results[2] == "Hey, you're trying to trick me!"