import time
import secrets

# Simulated secure password
SECURE_PASSWORD = "securepassword"

def verify_password(input_password):
    """
    Verifies if the provided password matches the secure password.
    """
    if len(input_password) != len(SECURE_PASSWORD):
        return False

    # Compare character by character, simulating an unintentional timing leak
    for i in range(len(SECURE_PASSWORD)):
        if input_password[i] != SECURE_PASSWORD[i]:
            return False
        # Simulate timing difference for each correct character matched
        time.sleep(0.01)  # Adds a small delay for each matching character

    return True

def timing_attack():
    """
    Attempts a timing attack to guess the password.
    """
    guessed_password = ""
    for position in range(len(SECURE_PASSWORD)):
        max_time = 0
        best_guess = ''

        # Try all possible characters for this position
        for char in "abcdefghijklmnopqrstuvwxyz":
            trial_password = guessed_password + char + 'a' * (len(SECURE_PASSWORD) - len(guessed_password) - 1)

            # Measure the time taken to verify this trial password
            start_time = time.time()
            verify_password(trial_password)
            elapsed_time = time.time() - start_time

            # Record the character with the highest time
            if elapsed_time > max_time:
                max_time = elapsed_time
                best_guess = char

        # Add the best guess character to the guessed password
        guessed_password += best_guess
        print(f"Guessed so far: {guessed_password}")

    return guessed_password

# Running the timing attack
print("Starting timing attack...")
recovered_password = timing_attack()
print(f"Recovered password: {recovered_password}")
