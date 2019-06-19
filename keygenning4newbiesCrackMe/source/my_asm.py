def MOVSX(destination, source):
    destination[:] = [0, 0, 0, 0]
    if source < 128:
        destination[3] = source
    else:
        destination[:3] = [255, 255, 255]
        destination[3] = source


def XOR(arg1, arg2):
    for i in range(len(arg1)):
        arg1[i] = arg1[i] ^ arg2[i]


def ADD(arg1, arg2):
    for i in range(3, -1, -1):
        arg1[i] += arg2[i]
        if arg1[i] >= 256:
            quotient, remainder = divmod(arg1[i], 256)
            if i == 0:
                arg1[i] = remainder
            else:
                arg1[i] = remainder
                arg1[i - 1] += quotient


def IMUL(arg1, cnt):
    tmp = arg1[:]
    for i in range(cnt-1):
        ADD(arg1, tmp)


def SHL(arg1, cnt):
    for i in range(cnt):
        for j in range(3, -1, -1):
            arg1[j] *= 2
        for j in range(3, -1, -1):
            if arg1[j] >= 256:
                quotient, remainder = divmod(arg1[j], 256)
                if j == 0:
                    arg1[j] = remainder
                else:
                    arg1[j] = remainder
                    arg1[j - 1] += quotient
