def generate_hashtag(s):
    result = ''.join(word[:1].upper() + word[1:].lower() for word in f'{s}'.split())
    result = f'#{result}'
    if result == '#' or len(result) > 140:
        return False
    return result
