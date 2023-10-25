import random
import time

def main():
  with open('test', 'r') as file:
    # Read the file content
    content = file.read()

    # Split the content into sentences
    sentences = content.split('.')

    # Filter out sentences with less than 10 words
    long_sentences = [sentence for sentence in sentences if len(sentence.split()) >= 10]

    # Randomly select a sentence from the long sentences
    random_sentence = random.choice(long_sentences)

    # Display the sentence to the user
    print(random_sentence)

    time.sleep(5)

    # Start the timer
    start_time = time.time()

    # Get the user's input
    user_input = input("Type the sentence and press enter: ")

    # Stop the timer
    end_time = time.time()

    # Calculate the typing speed and accuracy
    typing_speed = len(random_sentence.split()) / (end_time - start_time) / 60
    accuracy = len([char for char in user_input if char in random_sentence]) / len(random_sentence)

    # Display the results to the user
    print("Your typing speed is {} words per minute.".format(typing_speed))
    print("Your accuracy is {}%.".format(accuracy * 100))

if __name__ == "__main__":
    main()
