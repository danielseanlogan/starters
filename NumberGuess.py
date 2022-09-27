

fire = [1,2,3,4,5,6,7]
police = [2,4,6]
sanitization = [1,2,3,4,5,6,7]

for i in range(len(fire)):
    for j in range(len(police)):
        for k in range(len(sanitization)):
            if (fire[i] + police[j] + sanitization[k]) == 12 and fire[i] != police[j] and fire[i] != sanitization[k] and police[j] != sanitization[k]:
                print(f"{fire[i]} is Fire, {police[j]} is Police, and {sanitization[k]} is Sanitization")
