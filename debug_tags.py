import re

def find_unclosed_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Join split tags first to make counting easier
    content = re.sub(r'\{%[\s\S]*?%\}', lambda m: re.sub(r'\s+', ' ', m.group(0)), content)
    content = re.sub(r'\{\{[\s\S]*?\}\}', lambda m: re.sub(r'\s+', ' ', m.group(0)), content)

    tags = re.findall(r'\{%\s*(\w+)', content)
    
    stack = []
    for tag in tags:
        if tag in ['if', 'for', 'block', 'with']:
            stack.append(tag)
        elif tag == 'endif':
            if not stack or stack[-1] != 'if':
                print(f"Error: endif without if (stack: {stack})")
            else:
                stack.pop()
        elif tag == 'endfor':
            if not stack or stack[-1] != 'for':
                print(f"Error: endfor without for (stack: {stack})")
            else:
                stack.pop()
        elif tag == 'endblock':
            if not stack or stack[-1] != 'block':
                print(f"Error: endblock without block (stack: {stack})")
            else:
                stack.pop()
        elif tag == 'endwith':
            if not stack or stack[-1] != 'with':
                print(f"Error: endwith without with (stack: {stack})")
            else:
                stack.pop()

    if stack:
        print(f"Unclosed tags: {stack}")
    else:
        print("All tags closed.")

if __name__ == "__main__":
    find_unclosed_tags('templates/od/od_requests.html')
