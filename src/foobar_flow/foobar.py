# Define a function to handle the flow
def sample_flow():
    # Prompt the user for input
    user_input = input("Please enter your query: ")
    
    # Process the input (in this case, just echo it back)
    process_input(user_input)

# Define a function to process the input
def process_input(query):
    # Echo the input back to the user
    print(f"You entered: {query}")

# Main entry point of the script
if __name__ == "__main__":
    sample_flow()