import argparse,sys

parser = argparse.ArgumentParser()

parser.add_argument("--match",  help="data", required=True)

params = parser.parse_args()

input = params.match

data_input = sys.stdin.read()

data_input_l = data_input.split('\n')
data_l = list(filter(lambda e: input in e,data_input_l))
data =  '\n'.join(data_l)

sys.stdout.write('Received: %s'%data)

