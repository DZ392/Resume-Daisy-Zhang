import re
import os

def flatten_latex(main_file, output_file):
    with open(main_file, 'r') as f:
        content = f.read()

    def replace_input(match):
        filepath = match.group(1)
        if not filepath.endswith('.tex'):
            filepath += '.tex'
        
        if not os.path.exists(filepath):
            return match.group(0) # Keep original if not a local file

        with open(filepath, 'r') as f:
            return f.read()

    pattern = r'\\input\{([^}]+)\}'
    flattened_content = re.sub(pattern, replace_input, content)

    with open(output_file, 'w') as f:
        f.write(flattened_content)
    
    print(f"Successfully flattened {main_file} into {output_file}")

if __name__ == "__main__":
    flatten_latex("Daisy_Zhang_Resume.tex", "Daisy_Zhang_Resume_Combined.tex")
