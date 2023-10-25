import random
import time

def main():
  with open('test', 'r') as file:
    # Read the file content
    content = file.read()

    # Get the random sentence from the content
    sentences = content.split('.')
    random_sentence = random.choice(sentences)

    # Display the random sentence to the user
    print("\n" + random_sentence + "\n")
    print("Please type the above sentence exactly as it appears and press enter: ")
    time.sleep(5)

    # Calculate typing speed
    start_time = time.time()
    user_input = input("Time's up! Please type the above sentence again and press enter: ")
    end_time = time.time()

    total_typing_time = end_time - start_time
    typing_speed = len(random_sentence.split()) / total_typing_time / 60

    # Calculate accuracy
    correct_input = random_sentence
    user_accuracy = len([char for char in user_input if char in correct_input]) / len(correct_input)

    # Display results
    print("\nTyping speed: {:.2f} WPM".format(typing_speed))
    print("Accuracy: {:.2f}%".format(user_accuracy * 100))

if __name__ == "__main__":
    main()