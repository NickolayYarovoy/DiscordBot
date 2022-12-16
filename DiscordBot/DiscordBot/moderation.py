from email import message
import re

def moderation(message: str) -> bool:
    r_message = message.lower()
    first = r'\b(?:вы?|до|за|на|не|от?|при|по|рас)?ху[йаиеёоуыэюя]'
    if re.search(first, r_message) != None:
        return True
    second = r'\b\w*бля[дт]|бля'
    if re.search(second, r_message) != None:
        return True
    if re.search(r'пизд|ебат', r_message) != None:
        return True
    return False





