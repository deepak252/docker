from tasks import add

result = add.delay(5, 7)
print("Task submitted! ID:", result.id)