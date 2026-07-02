import re

def join_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Join split block tags {% ... %}
    def block_repl(match):
        return re.sub(r'\s+', ' ', match.group(0))
    
    content = re.sub(r'\{%[\s\S]*?%\}', block_repl, content)

    # Join split variable tags {{ ... }}
    def var_repl(match):
        return re.sub(r'\s+', ' ', match.group(0))
    
    content = re.sub(r'\{\{[\s\S]*?\}\}', var_repl, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    join_tags('templates/od/od_requests.html')
