import subprocess

p1 = subprocess.Popen(['python','my_code.py'], stdout = subprocess.PIPE)

p2 = subprocess.Popen(['python', 'find_word.py'], stdin =  p1.stdout , stdout = subprocess.PIPE)

p1.stdout.close()

print (p2.communicate()[0])
