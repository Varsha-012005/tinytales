import sys
import requests
import json
import traceback
import time
from datetime import datetime

# Configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"
DEFAULT_PROMPT = "random story"
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
TIMEOUT = 300  # Increased timeout to 300 seconds
DEFAULT_PROMPT = """Write a creative and engaging short story with the following requirements:
- Title: Create an interesting title
- Characters: Develop 2-3 main characters with distinct personalities
- Setting: Describe the time and place where the story occurs
- Plot: Include a clear beginning, middle with conflict, and satisfying resolution
- Theme: Convey a meaningful message or lesson
- Style: Use vivid descriptions and natural dialogue

Story topic: {user_input}"""

def generate_story(prompt, word_count=100, genre=None, retries=MAX_RETRIES):
    """
    Generate a story using Ollama API with retry logic
    """
    attempt = 0
    last_error = None
    
    # Build the prompt with word count and genre
    # Build the comprehensive prompt with all story requirements
    full_prompt = DEFAULT_PROMPT.format(user_input=prompt)
    if genre:
        full_prompt += f"\nGenre: {genre.capitalize()} (ensure the story follows genre conventions)"
        full_prompt += (
        f"\nWord count: Approximately {word_count} words\n"
        f"\nAdditional instructions:\n"
        "- Avoid clichés and overused tropes\n"
        "- Show character emotions through actions and dialogue\n"
        "- Maintain consistent pacing throughout the story\n"
        "- End with a satisfying conclusion that ties up main plot points"
    )
    
    while attempt < retries:
        attempt += 1
        try:
            print(f"Attempt {attempt}/{retries}: Generating story...", file=sys.stderr)
            
            response = requests.post(
                OLLAMA_ENDPOINT,
                json={
                    "model": MODEL_NAME,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_ctx": 512
                    }
                },
                timeout=TIMEOUT
            )
            
            response.raise_for_status()
            result = response.json()
            
            if "response" in result:
                return result["response"].strip()
            else:
                raise ValueError("No response from AI model")

        except requests.exceptions.RequestException as e:
            last_error = e
            print(f"Attempt {attempt} failed: {str(e)}", file=sys.stderr)
            if attempt < retries:
                print(f"Retrying in {RETRY_DELAY} seconds...", file=sys.stderr)
                time.sleep(RETRY_DELAY)
        except json.JSONDecodeError as e:
            last_error = e
            print(f"JSON decode error: {str(e)}", file=sys.stderr)
            break
        except Exception as e:
            last_error = e
            print(f"Unexpected error: {str(e)}", file=sys.stderr)
            break
    
    # If all retries failed, return a fallback story
    fallback_story = (
        f"Could not generate story due to technical difficulties. "
        f"Original prompt was: '{prompt}'. "
        f"Error: {str(last_error)}"
    )
    return fallback_story

def main():
    try:
        # Get arguments from command line
        prompt = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROMPT
        word_count = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        genre = sys.argv[3] if len(sys.argv) > 3 else None
        
        # Log the generation attempt
        print(f"Generating story for prompt: '{prompt}' at {datetime.now()}", file=sys.stderr)
        print(f"Word count: {word_count}, Genre: {genre or 'None'}", file=sys.stderr)
        
        # Generate the story
        story = generate_story(prompt, word_count, genre)
        
        # Return the generated text
        print(story)
        
    except Exception as e:
        error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_msg, file=sys.stderr)
        print("Failed to generate story. Please try again later.")
        sys.exit(1)

if __name__ == "__main__":
    main()