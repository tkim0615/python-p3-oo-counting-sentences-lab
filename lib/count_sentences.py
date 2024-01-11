#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value
  def get_value(self):
     return self._value

  def set_value(self,value):
    if not isinstance(value,str):
      print("The value must be a string.")
    self._value = value
    
  value=(property(get_value, set_value))
  
  def is_sentence(self):
    return self.value.endswith('.')
  def is_question(self):
    return self.value.endswith('?')
  def is_exclamation(self):
    return self.value.endswith('!')
  def count_sentences(self):
    value = self.value
    for punc in ['?', '!']:
      value = value.replace(punc, '.')    
    sentences = [s for s in value.split('.') if s]
    return len(sentences)
    
    


    
string = MyString()
string.value = 'hello'


    


# MyString
# Create the MyString class and give it a value property. 
# The class should verify that the value is a string before assigning it.
#  The default value of value should be the empty string, ''.