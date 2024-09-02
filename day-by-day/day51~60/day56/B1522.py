ab_slide_str = str(input())
a_cnt = 0
b_cnt = 0

for i in range(len(ab_slide_str)):
    if ab_slide_str[i] == "b":
        b_cnt += 1
    else:
        a_cnt += 1

b_max_cnt = 0
b_window_len = 0
for idx in range(b_cnt):
    if (ab_slide_str[idx] == "b"):
        b_window_len += 1
b_max_cnt = b_window_len


for start_idx in range(1, len(ab_slide_str)):
    end_idx = start_idx + b_cnt - 1
    if (end_idx >= len(ab_slide_str)):
        end_idx = b_cnt + start_idx - len(ab_slide_str) - 1
    if ab_slide_str[start_idx - 1] == "b":
        b_window_len -= 1
    if ab_slide_str[end_idx] == "b":
        b_window_len += 1
    if (b_window_len > b_max_cnt):
        b_max_cnt = b_window_len
    # print("start: ", start_idx, " end: ", end_idx, " size: ", b_window_len)
print(b_cnt - b_max_cnt)
