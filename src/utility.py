import re

# extract first element content (by class)
def class_content(parent, className):
    first_element = parent.find_elements_by_class_name(className)[0]
    return first_element.get_attribute('innerHTML')
def a_textcontent(parent):
    first_element = parent.find_elements_by_tag_name('a')[0]
    return first_element.get_attribute('innerHTML')

# classList is [firstClassToFind, secondClassToFind, etc.]
def class_content_search(parent, classList, attribute=None):
    head = parent
    while classList:
        head = head.find_elements_by_class_name(classList[0])[0]
        classList.pop(0)
    if (attribute):
        return head.get_attribute(attribute)
    return head

def remove_spaces(inp):
    return "".join(inp.split())

def remove_nonnumerical(inp):
    return re.sub("[^0-9]", "", inp)
    
def find_between(string, char_start, char_end):
    return string[string.find(char_start)+1 : string.find(char_end)]