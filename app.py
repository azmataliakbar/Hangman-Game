# app.py

import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="🎮 Hangman Game", page_icon="🪢")

# Add a colorful title
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: white;
        background-color: #FF5733;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    <div class="title">🎮 Hangman Game 🪢</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful header
st.markdown(
    """
    <style>
    .header {
        font-size: 27px;
        font-weight: bold;
        color: #33FF57;
        text-align: center;
    }
    </style>
    <div class="header">✨ Guess the Word Before the Hangman is Complete! ✨</div>
    """,
    unsafe_allow_html=True
)

# List of words for the game
words = ["PYTHON", "STREAMLIT", "HANGMAN", "PROGRAMMING", "DEVELOPER", "CODE"]

# Initialize session state for game variables
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
if "guessed_letters" not in st.session_state:
    st.session_state.guessed_letters = []
if "attempts" not in st.session_state:
    st.session_state.attempts = 6

# Function to reset the game
def reset_game():
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.attempts = 6

# Display the current state of the word
def display_word():
    return " ".join([letter if letter in st.session_state.guessed_letters else "_" for letter in st.session_state.word])

# Add instructions
st.markdown(
    """
    <style>
    .instructions {
        font-size: 20px;
        color: #33A8FF;
        text-align: center;
    }
    </style>
    <div class="instructions">🎯 Guess the letters to complete the word. You have 6 attempts!</div>
    """,
    unsafe_allow_html=True
)

# Display the word with guessed letters
st.markdown(
    f"""
    <style>
    .word {{
        font-size: 30px;
        font-weight: bold;
        color: #FFA500;
        text-align: center;
    }}
    </style>
    <div class="word">{display_word()}</div>
    """,
    unsafe_allow_html=True
)

# Display the number of attempts left
st.markdown(
    f"""
    <style>
    .attempts {{
        font-size: 25px;
        font-weight: bold;
        color: #FF3333;
        text-align: center;
    }}
    </style>
    <div class="attempts">🪢 Attempts Left: {st.session_state.attempts}</div>
    """,
    unsafe_allow_html=True
)

# Add a text input for the user to guess a letter
guess = st.text_input("🔤 Guess a letter:", max_chars=1, key="guess").upper()

# Add a button to submit the guess
if st.button("🚀 Submit Guess"):
    if guess in st.session_state.guessed_letters:
        st.markdown(
            """
            <style>
            .feedback {
                font-size: 25px;
                font-weight: bold;
                color: #FF3333;
                text-align: center;
            }
            </style>
            <div class="feedback">⚠️ You already guessed that letter!</div>
            """,
            unsafe_allow_html=True
        )
    elif guess in st.session_state.word:
        st.session_state.guessed_letters.append(guess)
        st.markdown(
            """
            <style>
            .feedback {
                font-size: 25px;
                font-weight: bold;
                color: #33FF57;
                text-align: center;
            }
            </style>
            <div class="feedback">🎉 Correct guess!</div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.session_state.attempts -= 1
        st.session_state.guessed_letters.append(guess)
        st.markdown(
            """
            <style>
            .feedback {
                font-size: 25px;
                font-weight: bold;
                color: #FF3333;
                text-align: center;
            }
            </style>
            <div class="feedback">😢 Wrong guess!</div>
            """,
            unsafe_allow_html=True
        )

# Check if the game is over
if st.session_state.attempts == 0:
    st.markdown(
        f"""
        <style>
        .game-over {{
            font-size: 30px;
            font-weight: bold;
            color: #FF3333;
            text-align: center;
        }}
        </style>
        <div class="game-over">💀 Game Over! The word was: {st.session_state.word}</div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🔄 Play Again"):
        reset_game()
elif all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
    st.markdown(
        f"""
        <style>
        .game-over {{
            font-size: 30px;
            font-weight: bold;
            color: #33FF57;
            text-align: center;
        }}
        </style>
        <div class="game-over">🎉 You Win! The word was: {st.session_state.word}</div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🔄 Play Again"):
        reset_game()

# Add a colorful footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 20px;
        color: #33C1FF;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="footer">🚀 Thanks for playing Hangman! 🚀</div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h5 style="color: lightgreen; font-weight: bold; text-align: center; margin-top: 20px; margin-left: 45px;">
        ✏️📚 Author: Azmat Ali 📚✏️
    </h5>
    """,
    unsafe_allow_html=True
)