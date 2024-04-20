import json
f = open('output.txt')

ins = "instruction"
inp = "Input"
outp = "Output"
bslash = '''\\"'''
outls = []
j = 0

for data in f:
    while True:
        j+=1
        outdic = {}
        #print(len(data))
        i = data[data.find(ins) + len(ins) + 2:].find(bslash)+ data.find(ins) + len(ins) + 4
        if i > len(data):break
        data = data[i:]
        snippet = data[:data.find(bslash)]
        if(data[len(snippet):].find(inp) != -1):
            while(data[len(snippet):].find(inp) > 15): snippet = data[:data[len(snippet)+2:].find(bslash)+len(snippet)+2]
        #snippet = data[:data.find(bslash)
        else: snippet = data[:data.rfind(bslash)]
        while len(snippet)>0 and snippet[0]=='#' : snippet = snippet[1:]
        while len(snippet)>0 and snippet[-1]=='@' : snippet = snippet[:-1]
        outdic["Instruction"] = snippet
        data = data[len(snippet)+2:]
        
        i = data[data.find(inp) + len(inp) + 2:].find(bslash)+ data.find(inp) + len(inp) + 4
        data = data[i:]
        snippet = data[:data.find(bslash)]
        if(data[len(snippet):].find(outp) != -1):
            while(data[len(snippet):].find(outp) > 15): snippet = data[:data[len(snippet)+2:].find(bslash)+len(snippet)+2]
        #snippet = data[:data.find(bslash)
        else: snippet = data[:data.rfind(bslash)]
        while len(snippet)>0 and snippet[0]=='#' : snippet = snippet[1:]
        while len(snippet)>0 and snippet[-1]=='@' : snippet = snippet[:-1]
        outdic["Input"] = snippet
        data = data[len(snippet)+2:]
        
        i = data[data.find(outp) + len(outp) + 2:].find(bslash)+ data.find(outp) + len(outp) + 4
        data = data[i:]
        snippet = data[:data.find(bslash)]
        if(data[len(snippet):].find(ins) != -1 and len(data[len(snippet):]) > 15):
            while(data[len(snippet):].find(ins) > 15): snippet = data[:data[len(snippet)+2:].find(bslash)+len(snippet)+2]
        #snippet = data[:data.find(bslash)
        else : snippet = data[:data.rfind(bslash)]
        while len(snippet)>0 and snippet[0]=='#' : snippet = snippet[1:]
        while len(snippet)>0 and snippet[-1]=='@' : snippet = snippet[:-1]
        outdic["Output"] = snippet
        data = data[len(snippet)+2:]

        outls.append(outdic)
        print(j)

with open('outputclean.json', 'a') as file:
    json.dump(outls, file, indent=4)