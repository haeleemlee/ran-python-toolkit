# List vs Tuple vs Set

# list - 순서 있고, 바꿀 수 있음
bler_list = [0.02, 0.05, 0.02, 0.12]
bler_list.append(0.08) # 추가 가능
print(bler_list[0]) # 0.02
print(len(bler_list)) # 5 - 중복 유지

# tuple - 바꿀 수 없음
cell_config = ("Cell-1", 30, 100) # 이름, scs, bw
print(cell_config[1]) # 30
#cell_config[1] = 15 # Type error. 값을 변경할 수 없음

# set - 중복 자동 제거, 순서 없음
cells = {"Cell-1", "Cell-2" , "Cell-1"}
print(cells) # {'Cell-1', 'Cell-2'} - 하나로 합쳐짐
#print(cells[0]) # Type error : not subscriptable, 인덱싱이 안됨
 