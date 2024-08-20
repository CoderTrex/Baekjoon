# width, height, Trampoline, star_len = map(int, input().split())
# shooting_star = [list(map(int, input().split())) for _ in range(star_len)]
# shooting_star.sort(key=lambda x: x[0])

# # print(shooting_star)

# # print("\n")
# min_hit_star = star_len
# for i in range(star_len):
#     cover_location_x = shooting_star[i][0]
#     cover_location_y = shooting_star[i][1]
#     # print("shooting_star[i]:", shooting_star[i])
    
#     start_x = cover_location_x - Trampoline
#     start_y = cover_location_y - Trampoline
    
#     for x in range(start_x, cover_location_x+1):
#         for y in range(start_y, cover_location_y+1):
#             hit_star = 0
#             for star in shooting_star:
#                 if x <= star[0] <= x+Trampoline and y <= star[1] <= y+Trampoline:
#                     continue
#                 if min_hit_star <= hit_star:
#                     break
#                 hit_star += 1
#             min_hit_star = min(min_hit_star, hit_star)
#             # print("hit_star:", hit_star)
#             # print("coverd:", x, x+Trampoline, y, y+Trampoline)
# print(min_hit_star)


def star_max(x, y):
    star_cnt = 0
    for i in range(star_len):
        star_x, star_y = shooting_star[i]
        if (x<=star_x) and (star_x<=x+Trampoline) and (y<=star_y) and (star_y<=y+Trampoline):
            star_cnt += 1
    return star_cnt

def solution(star_len, shooting_star):
    max_star = 0
    for i in range(star_len):
        for j in range(star_len):
            x, y = shooting_star[i][0], shooting_star[j][1]
            max_star = max(max_star, star_max(x, y))
    return star_len - max_star

width, height, Trampoline, star_len = map(int, input().split())
shooting_star = [list(map(int, input().split())) for _ in range(star_len)]

print(solution(star_len, shooting_star))