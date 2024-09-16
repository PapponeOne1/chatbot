# Initialize a simple dictionary to store questions and answers
chatbot_memory = {}

def process_input(user_input):
    # Split the input into words
    words = user_input.lower().split()
    return words

def save_interaction(question, answer):
    words = tuple(process_input(question))
    chatbot_memory[words] = answer

def find_best_match(question):
    question_words = process_input(question)
    best_match = None
    best_match_count = 0
    
    for stored_question in chatbot_memory.keys():
        common_words = set(question_words) & set(stored_question)
        match_count = len(common_words)
        
        if match_count > best_match_count:
            best_match = stored_question
            best_match_count = match_count
            
    return best_match, best_match_count

def get_response(question):
    best_match, best_match_count = find_best_match(question)
    if best_match and best_match_count / len(best_match) >= 0.5:
        return chatbot_memory[best_match]
    else:
        return "I don't know the answer to that. Can you tell me? Just write the answer you would expect."

def initialize_memory():
    # Add a few basic questions and answers to the chatbot's memory
    basic_interactions = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but thanks for asking! How about you?",
        "what is your name": "I'm a learning chatbot. You can teach me new things!",
        "what can you do": "I can try to answer your questions and learn from you.",
    }
    for question, answer in basic_interactions.items():
        save_interaction(question, answer)

def chat():
    print("Chatbot: Hi! I'm here to learn from you.")
    
    # Initialize chatbot memory with basic questions and answers
    initialize_memory()
    
    waiting_for_answer = False
    last_question = None
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Check if the bot is waiting for an answer
        if waiting_for_answer:
            # Save the interaction
            save_interaction(last_question, user_input)
            print("Chatbot: Thank you! I've learned something new.")
            waiting_for_answer = False  # Reset the state
            last_question = None  # Clear the last question
            continue
        
        # Normal processing
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        
        # If the bot doesn't know the answer, prompt for one
        if response.startswith("I don't know the answer to that"):
            waiting_for_answer = True
            last_question = user_input

# Start the chatbot
chat()
