# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The hints were wrong
- New Game button is not allowing user to play a new game
- Accepts numbers not in the range 1-100
- Difficulty levels are wrong

---

## 2. How did you use AI as a teammate?

I used Claude Code in agent mode as my AI tool throughout this project. I sometimes asked to explain lines of code that didn't make sense and other times I was talking to it about how to fix it. One example of an incorrect AI suggestion: Claude first reset `attempts` to `1` in the New Game button, which looked correct but was itself a bug causing the attempts counter to be off by one from the start. I caught it by asking Claude to do a code review of other function, which exposed the inconsistency.

---

## 3. Debugging and testing your fixes

I manually tested using the app and giving edge case inputs. For instance, I tried various difficulty levels, tested the new game button, inputted an out-of-range number, etc. I also added few testcases with the help of Claude in the test folder. I used `pytest` to test them, and they were successful.


---

## 4. What did you learn about Streamlit and state?

The secret number was not stable in the original app when New Game was clicked because the reset block didn't clear `status`, `score`, or `history`, and used a hardcoded `random.randint(1, 100)` that ignored the selected difficulty. Streamlit reruns the entire script from top to bottom on every user interaction, so any variable not stored in `st.session_state` is lost on each rerun. The game keeps a stable secret by only calling `random.randint` inside an `if "secret" not in st.session_state` check, so it only generates once per game.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is asking AI to explain what the broken code is doing before asking for a fix, understanding the bug first led to better and more targeted changes. This project changed how I think about AI-generated code: bugs can be subtle and conditional (like the string comparison only triggering every other attempt), so I need to read and question AI output rather than assume it's correct.
