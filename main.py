print("Script has been run!")#
import time

start_time = time.time()

while True:
  time.sleep(5)
  print(time.time() - start_time)

print("Script has ended!")
print(time.time() - start_time)
