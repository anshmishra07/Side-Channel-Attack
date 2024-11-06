import time
import secrets


SECURE_PASSWORD = "securepassword"

def verify_password(input_password):
    
    if len(input_password) != len(SECURE_PASSWORD):
        return False

    for i in range(len(SECURE_PASSWORD)):
        if input_password[i] != SECURE_PASSWORD[i]:
            return False
      
        time.sleep(0.01)  

    return True

def timing_attack():
    
    guessed_password = ""
    for position in range(len(SECURE_PASSWORD)):
        max_time = 0
        best_guess = ''

       
        for char in "abcdefghijklmnopqrstuvwxyz":
            trial_password = guessed_password + char + 'a' * (len(SECURE_PASSWORD) - len(guessed_password) - 1)

            
            start_time = time.time()
            verify_password(trial_password)
            elapsed_time = time.time() - start_time

          
            if elapsed_time > max_time:
                max_time = elapsed_time
                best_guess = char

    
        guessed_password += best_guess
        print(f"Guessed so far: {guessed_password}")

    return guessed_password


print("Starting timing attack...")
recovered_password = timing_attack()
print(f"Recovered password: {recovered_password}")
