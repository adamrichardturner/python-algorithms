def data_reverse(data):
    """
    A stream of data is received and needs to be reversed.

    Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

    11111111  00000000  00001111  10101010
    (byte1)   (byte2)   (byte3)   (byte4)
    should become:

    10101010  00001111  00000000  11111111
    (byte4)   (byte3)   (byte2)   (byte1)
    """
    # Using list comprehension we break the original list into chunks of bytes
    stream = [data[i:i + 8] for i in range(0, len(data), 8)]
    # Then we flatten the list in reverse
    flat_stream = [i for sub in stream[::-1] for i in sub]
    return flat_stream

x = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

print(data_reverse(x)) # [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]