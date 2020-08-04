def is_palindrome(word):
    # 코드를 입력하세요.
    mid = int(len(word)/2)
    isSame = False
    for i in range(mid,0,-1):
        front = word[(mid-i)]
        end = word[(mid+i)]
        if(front==end):
            isSame = True
        else:
            isSame = False
    return isSame

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))