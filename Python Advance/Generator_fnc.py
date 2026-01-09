def get_gn_func():
    for i in range(1,5):
        yield i

gen = get_gn_func()

print(next(gen))
print(next(gen))

#Here the yeild keyword is pauses the function. it redume when we call the next.