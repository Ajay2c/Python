if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_avg = list(arr)
    list_avg.sort()

    # avg = 0
    # for i in arr:
    #     if avg < i:
    #         avg = i
    # print(avg)