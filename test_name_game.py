import name_game

def test_names():
    results = name_game.name_game("Amanda").splitlines()
    assert results[0] == "amanda, amanda, bo-bamanda"
    
    results = name_game.name_game("Stan").splitlines()
    assert results[0] == "stan, stan, bo-ban"
    
    results = name_game.name_game("Bryan").splitlines()
    assert results[0] == "bryan, bryan, bo-byan"

def test_no_swearing():
    results = name_game.name_game("Chuck").splitlines()
    assert results[2] == "Hey, you're trying to trick me!"
    