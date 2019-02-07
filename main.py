from markovchain.text import MarkovText
from gtts import gTTS

def generate_markov(input_path):
    markov = MarkovText()
    with open(input_path) as fp:
        markov.data(fp.read())

    return markov

def text_to_speech(text, output_path):
    # gTTS only outputs mp3 data
    assert output_path.endswith('.mp3')

    markov_tts = gTTS(text, lang='en')
    with open(output_path, 'wb') as fd:
        markov_tts.write_to_fp(fd)

def save_gene_rayism(output_path, input_text_path='input.txt'):
    markov = generate_markov(input_text_path)
    gene_statement = markov()

    text_to_speech(gene_statement, output_path)
    return gene_statement

if __name__ == '__main__':
    import sys
    import subprocess
    output_path = 'gene-ray.mp3'
    print(save_gene_rayism(output_path))

    if sys.platform == 'darwin':
        subprocess.call(['afplay', output_path])
    elif 'linux' in sys.platform:
        # This probably won't work but like who cares
        subprocess.call(['aplay', output_path])
