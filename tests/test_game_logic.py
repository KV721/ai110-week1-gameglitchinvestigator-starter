from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Tests targeting specific bugs that were fixed ---

def test_hint_direction_too_high():
    # Bug: hints were swapped — "Too High" was showing "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert message == "📈 Go LOWER!"

def test_hint_direction_too_low():
    # Bug: hints were swapped — "Too Low" was showing "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert message == "📉 Go HIGHER!"

def test_string_comparison_glitch():
    # Bug: secret was cast to str on even attempts, causing lexicographic comparison.
    # e.g. str(9) > str(50) is True because "9" > "5", wrongly returning "Too High".
    # With the fix, check_guess always receives int secrets and must return "Too Low" here.
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"

def test_update_score_too_high_always_deducts():
    # Bug: "Too High" on even attempt numbers added +5 points instead of deducting.
    # Both even and odd attempt numbers should deduct 5.
    score_after_even = update_score(100, "Too High", 2)
    score_after_odd = update_score(100, "Too High", 3)
    assert score_after_even == 95
    assert score_after_odd == 95

def test_update_score_win_no_off_by_one():
    # Bug: win score used (attempt_number + 1), under-rewarding by 10 points.
    # Winning on attempt 1 should give 100 - 10*1 = 90 points, not 80.
    score = update_score(0, "Win", 1)
    assert score == 90
