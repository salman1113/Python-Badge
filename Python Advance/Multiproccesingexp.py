import multiprocessing

def heavy_calculation():
    print("calculating...")
    print(10*100)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=heavy_calculation)
    p2 = multiprocessing.Process(target=heavy_calculation)

    p1.start()
    p2.start()
    p1.join() 
    p2.join() 
    print('all procces completed')
