        for (int i = 1; i < N + 1; i++) {
            int min = Integer.MAX_VALUE - 1;
            int min_loc = i, new_path;

            for (int j = i + 1; j < N + 1; j++) {
                if (min > graph[i][j]) {
                    v_min_loc.clear();
                    min = graph[i][j];
                    v_min_loc.add(j);
                }
                else if (min == graph[i][j]) {
                    v_min_loc.add(j);
                }
            }
            for (int j = 0; j < v_min_loc.size(); j++) {
                min_loc = v_min_loc.get(j); // i에서 가장 가까운 정점
                for (int k = 1; k < N + 1; k++) {
                    // print debug
                    new_path = graph[i][k];
                    if (k == i || k == min_loc) continue;
                    if (graph[i][min_loc] == Integer.MAX_VALUE || graph[min_loc][k] == Integer.MAX_VALUE)
                    new_path = Integer.MAX_VALUE;
                    else
                        if (min_loc > k) 
                            new_path = graph[i][min_loc] + graph[k][min_loc];
                        else
                            new_path = graph[i][min_loc] + graph[min_loc][k];
                    if (graph[i][k] > new_path) 
                        graph[i][k] = new_path;
                }
            }
        }