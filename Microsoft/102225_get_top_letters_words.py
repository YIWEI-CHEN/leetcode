from collections import Counter
import re

def get_top_letters_and_words(text, top_n=10):
    """
    Analyze text to find the most frequent letters and words.
    
    Args:
        text (str): The input text to analyze
        top_n (int): Number of top items to return (default: 10)
    
    Returns:
        dict: Dictionary containing 'top_letters' and 'top_words' lists
    """
    if not text:
        return {'top_letters': [], 'top_words': []}
    
    # Convert to lowercase for consistent analysis
    text_lower = text.lower()
    
    # Extract and count letters (excluding spaces and punctuation)
    letters = re.findall(r'[a-zA-Z]', text_lower)
    letter_counts = Counter(letters)
    
    # Extract and count words (clean and split)
    # Split contractions at apostrophes (didn't -> didn, t)
    """Regex Explanation:
    1. r'...' - Raw string literal (prevents Python from interpreting backslashes)

    2. \b - Word boundary
        - Matches the position between a word character and a non-word character
        - Ensures we capture complete words, not parts of words
    3. [a-zA-Z] - Character class
        - Matches any single letter (lowercase a-z or uppercase A-Z)
        - Does NOT include apostrophes, numbers, or other characters
    4. + - Quantifier
        - Matches one or more of the preceding character class
        - So [a-zA-Z]+ matches one or more consecutive letters
    5. \b - Another word boundary at the end
    """
    words = re.findall(r'\b[a-zA-Z]+\b', text_lower)
    word_counts = Counter(words)

    def custom_sorted(counter):
        # Sort the counter by frequency (highest first) and then alphabetically
        return sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    # Get top N letters and words
    top_letters = custom_sorted(letter_counts)[:top_n]
    top_words = custom_sorted(word_counts)[:top_n]

    return {
        'top_letters': top_letters,
        'top_words': top_words
    }

def display_results(results, title="Text Analysis Results"):
    """
    Display the analysis results in a formatted way.
    
    Args:
        results (dict): Results from get_top_letters_and_words()
        title (str): Title for the output
    """
    print(f"\n{title}")
    print("=" * len(title))
    
    print("\nTop Letters:")
    print("-" * 12)
    for i, (letter, count) in enumerate(results['top_letters'], 1):
        print(f"{i:2}. '{letter}': {count}")
    
    print("\nTop Words:")
    print("-" * 10)
    for i, (word, count) in enumerate(results['top_words'], 1):
        print(f"{i:2}. '{word}': {count}")

# Example usage
if __name__ == "__main__":
    # Sample text for demonstration
    sample_text = """
    The quick brown fox jumps over the lazy dog. The dog was sleeping peacefully 
    under the tree when the fox appeared. This is a classic example sentence that 
    contains every letter of the alphabet at least once. The fox and the dog became 
    friends after this encounter, and they often played together in the forest.
    """
    
    sample_text2 = """
    I didn't know what couldn't be done. It's amazing how we're learning and they've 
    improved so much. We'll see what happens when you're ready. Don't worry about 
    what won't work - focus on what will. She's been working hard, and he's been 
    helping too. We've got this, and you've got the skills needed.
    """
    
    # Analyze the sample text
    results = get_top_letters_and_words(sample_text2, top_n=5)
    display_results(results, "Sample Text Analysis")
    
    # You can also analyze custom text
    print("\n" + "="*50)
    print("Try with your own text:")
    print("="*50)
    
    # Uncomment the lines below to input custom text
    # custom_text = input("Enter your text: ")
    # custom_results = get_top_letters_and_words(custom_text, top_n=5)
    # display_results(custom_results, "Your Text Analysis")