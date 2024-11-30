class MyString:
    def __init__(self, value=''):
        # Ensuring the value is a string
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("The value must be a string.")  # Raise a ValueError if not a string

    def is_sentence(self):
        '''Returns True if value ends with a period, otherwise False.'''
        return self.value.endswith('.')

    def is_question(self):
        '''Returns True if value ends with a question mark, otherwise False.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''Returns True if value ends with an exclamation mark, otherwise False.'''
        return self.value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the value.'''
        # Split the value by sentence-ending punctuation marks (., !, ?)
        import re
        sentences = re.split(r'[.!?]+', self.value)
        
        # Remove any empty strings that might have been created from the split
        sentences = [s for s in sentences if s.strip()]
        
        return len(sentences)
