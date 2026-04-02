add_part_list = input().split('-')

# 첫번째 항
result = sum(map(int, add_part_list[0].split('+')))

for add_part in add_part_list[1:]:
    part_result = sum(map(int, add_part.split('+')))
    result -= part_result

print(result)