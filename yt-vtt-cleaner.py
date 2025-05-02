import re
import sys

def clean_vtt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove timestamp lines
    content = re.sub(r'(\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*?)\n', '', content)

    # Remove alignment and position tags
    content = re.sub(r'align:start position:\d+%', '', content)

    # Remove tags like <c> and timestamps within the text
    content = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}><c>', '', content)
    content = re.sub(r'</c>', '', content)

    # Remove extra blank lines
    content = re.sub(r'\n+', '\n', content)

    # Remove duplicate lines
    lines = content.strip().split('\n')
    unique_lines = []
    previous_line = ""
    for line in lines:
        if line.strip() and line != previous_line:
            unique_lines.append(line)
            previous_line = line

    # Join lines and save cleaned text
    cleaned_text = '\n'.join(unique_lines)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"Cleaned text saved to {output_file}")

try:
    clean_vtt(sys.argv[1], 'cleaned_subtitles.txt')
except IndexError:
    print("ERROR: name the text file!")
except FileNotFoundError:
    print("File not found: {}\nIs that the correct file name?".format(sys.argv[1])) 
