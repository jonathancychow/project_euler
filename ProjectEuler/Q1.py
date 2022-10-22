import datetime 
start_time = datetime.datetime.now()

print(sum([num for num in range(1000)if num%3==0 or num%5==0]))
time_taken = datetime.datetime.now() - start_time  

print(f"Time taken: {time_taken}")
    