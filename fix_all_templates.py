import os
import re

def fix_split_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for {{ ... }} tags that span multiple lines
    def join_variable_tag(match):
        res = re.sub(r'\s+', ' ', match.group(0))
        if res != match.group(0):
            print(f"  Joined variable tag in {file_path}")
        return res

    # Regex for {% ... %} tags that span multiple lines
    def join_block_tag(match):
        res = re.sub(r'\s+', ' ', match.group(0))
        if res != match.group(0):
            print(f"  Joined block tag in {file_path}")
        return res

    # Find and replace split variable tags
    new_content = re.sub(r'\{\{[\s\S]*?\}\}', join_variable_tag, content)
    
    # Find and replace split block tags
    new_content = re.sub(r'\{%[\s\S]*?%\}', join_block_tag, new_content)

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    template_dir = 'templates'
    found_any = False
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html'):
                if fix_split_tags(os.path.join(root, file)):
                    print(f"Fixed: {os.path.join(root, file)}")
                    found_any = True
    if not found_any:
        print("No split tags found in any template.")

if __name__ == '__main__':
    main()
