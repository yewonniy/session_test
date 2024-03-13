high = int(input("숫자 게임 최대값을 입력해주세요: "))
low = 1

print("1부터", high,"까지의 숫자를 하나 생각하세요.")
input("준비가 되었으면 Enter를 누르세요.")

correct = False
count = 0

while not correct:
    count += 1
    guess = (low + high) // 2
    print("당신이 생각한 숫자는", guess, "입니까?")
    feedback = input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크다면 '큼', 작다면 '작음'을 입력해주세요: ")

    if feedback == '맞음':
        print(count,"번만에 맞췄다")
        correct = True
    elif feedback == '큼':
        low = guess + 1
    elif feedback == '작음':
        high = guess - 1