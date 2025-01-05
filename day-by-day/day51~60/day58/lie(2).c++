#include <iostream>
#include <deque>


std::deque<bool> dfs(std::deque<std::deque<int>> party_list, 
        std::deque<int> truth_know_people, 
        std::deque<bool> party_visited) {

    for (int i = 0; i < party_list.size(); i++) {
        bool know_truth = false;
        // 이미 방문한 파티라면 넘어간다.
        if (party_visited[i]) {
            continue;
        }

        // 파티에 참가한 사람들 중 진실을 알고 있는 사람이 있는 지 확인한다.
        for (int j = 0; j < party_list[i].size(); j++) {
            if (truth_know_people[party_list[i][j] - 1] != 0) {
                know_truth = true;
                break;
            }
        }

        // 진실을 알고 있는 사람이 있다면, 그 파티에 참가한 사람들은 모두 진실을 알고 있는 사람으로 표시한다.
        if (know_truth) {
            for (int j = 0; j < party_list[i].size(); j++) {
                truth_know_people[party_list[i][j] - 1] = 1;
            }
            party_visited[i] = true;
            dfs(party_list, truth_know_people, party_visited);
        }

        // 다시 dfs를 호출한다.

        std::cout << "party_visited: " << party_visited[i] << std::endl;
        for (int i = 0; i < party_visited.size(); i++) {
            std::cout << party_visited[i] << " ";
        }
        std::cout << std::endl;
    }
    return party_visited;
}
    


int main () {
    int people_cnt, party_cnt, truth_know_cnt;
    std::deque<int> truth_know_people;
    std::cin >> people_cnt >> party_cnt;
    std::cin >> truth_know_cnt;
    for (int i = 0; i < truth_know_cnt; i++) {
        std::cin >> truth_know_people[i];
    }

    std::deque<std::deque<int>> party_list;
    for (int i = 0; i < party_cnt; i++) {
        int party_people_cnt;
        std::cin >> party_people_cnt;
        std::deque<int> party_people;
        for (int j = 0; j < party_people_cnt; j++) {
            int people;
            std::cin >> people;
            party_people.push_back(people);
        }
        party_list.push_back(party_people);
    }

    std::deque<bool> visited(party_cnt, false);
    std::deque<bool> result = dfs(party_list, truth_know_people, visited);
    int can_lie = 0;
    for (int i = 0; i < result.size(); i++) {
        if (!result[i]) {
            can_lie++;
        }
    }
    std::cout << can_lie;
}