def rectangle_rotation(b, a):
    x = 1
    count = 0
    step, point = (2**0.5)/2, 2**0.5
    while (step)*x <= a/2:
        if x%2 != 0:
            count = count + (int((b/2-step)/point) + 1)*4
        else:
            count = count + (int(b/2 / (point))) * 4
        x+=1
    count = count + (int(b/2 / point)) * 2 + (int(a/2 / point)) * 2 + 1
    return count
