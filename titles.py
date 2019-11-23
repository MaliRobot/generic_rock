
f = open('out/all_titles_processed.txt', 'r')
print(f)
titles = f.read()

for t in titles.split("'b"):
    print(str(t.strip()))
