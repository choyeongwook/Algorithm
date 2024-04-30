# 어떤 동물원에 가로로 두칸 세로로 N칸인 아래와 같은 우리가 있다.



# 이 동물원에는 사자들이 살고 있는데 사자들을 우리에 가둘 때, 가로로도 세로로도 붙어 있게 배치할 수는 없다. 이 동물원 조련사는 사자들의 배치 문제 때문에 골머리를 앓고 있다.

# 동물원 조련사의 머리가 아프지 않도록 우리가 2*N 배열에 사자를 배치하는 경우의 수가 몇 가지인지를 알아내는 프로그램을 작성해 주도록 하자. 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다고 가정한다.

n = int(input())

dp_nothing_in_bottom = [0] * (n+1) # 맨아래칸에 아무것도 없는 경우 수
dp_one_in_bottom = [0] * (n+1) # 맨아래칸에 하나 있는 경우 수

dp_nothing_in_bottom[1] = 1
dp_one_in_bottom[1] = 2

for i in range(2, n+1):
    dp_nothing_in_bottom[i] = (dp_nothing_in_bottom[i-1] + dp_one_in_bottom[i-1]) % 9901 # 이전 dp 개수 그대로
# 이전 dp에서 마지막 칸에 사자가 없던 경우의 수*2  +  이전 dp에서 마지막 칸에 사자가 한 마리 있던 경우의 수*1
    dp_one_in_bottom[i] = (dp_nothing_in_bottom[i-1] * 2 + dp_one_in_bottom[i-1]) % 9901 

print((dp_nothing_in_bottom[n] + dp_one_in_bottom[n]) % 9901)