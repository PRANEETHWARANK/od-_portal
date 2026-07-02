import re

def parse_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    stack = []
    for i, line in enumerate(lines):
        line_num = i + 1
        # Extract all tags on this line
        tags = re.findall(r'\{%\s*(\w+)', line)
        for tag in tags:
            if tag in ['if', 'for', 'block', 'with']:
                stack.append((tag, line_num))
                # print(f"Open {tag} at {line_num}")
            elif tag == 'endif':
                if not stack or stack[-1][0] != 'if':
                    print(f"Error: endif at {line_num} without if. Stack: {stack}")
                else:
                    stack.pop()
            elif tag == 'endfor':
                if not stack or stack[-1][0] != 'for':
                    print(f"Error: endfor at {line_num} without for. Stack: {stack}")
                else:
                    stack.pop()
            elif tag == 'empty':
                # Check if we are inside a 'for' and not inside an 'if'
                is_in_if = any(t[0] == 'if' for t in stack)
                is_in_for = any(t[0] == 'for' for t in stack)
                if is_in_if:
                    # Find the latest 'if'
                    for t, ln in reversed(stack):
                        if t == 'if':
                            print(f"Error: empty at {line_num} is inside if from {ln}")
                            break
                if not is_in_for:
                    print(f"Error: empty at {line_num} is not inside for")
            elif tag == 'endblock':
                if not stack or stack[-1][0] != 'block':
                    print(f"Error: endblock at {line_num} without block. Stack: {stack}")
                else:
                    stack.pop()

    if stack:
        print(f"Unclosed tags at end: {stack}")

if __name__ == "__main__":
    parse_template('templates/od/od_requests.html')
