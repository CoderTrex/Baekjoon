#include <iostream>
#include <vector>

int main() {
    int Number_People, Party_Cnt, truth_know;
    std::cin >> Number_People >> Party_Cnt;
    std::cin >> truth_know;
    std::vector<int> truth_know_people(Number_People);
    std::vector<std::vector<int>> party_list(Party_Cnt);
    for (int i = 0; i < truth_know; i++) {
        int truth_people;
        std::cin >> truth_people;
        truth_know_people[truth_people - 1] = 1;
    }

    // 1. 진실을 말해야하는 사람들의 집합을 찾는다.
    for (int i = 0; i < Party_Cnt; i++) {
        int party_people_cnt;
        bool know_truth = false;
        std::cin >> party_people_cnt;
        std::vector<int> party_people;
        for (int j = 0; j < party_people_cnt; j++) {
            int people;
            std::cin >> people;
            party_people.push_back(people);
            if (truth_know_people[people - 1] != 0) {
                know_truth = true;
            }
        }
        party_list[i] = party_people;
        if (know_truth) {
            for (int j = 0; j < party_people.size(); j++) {
                truth_know_people[party_people[j] - 1] = 1;
            }
        }
    }

    // 2. 진실을 말하지 않아도 되는 파티를 찾는다.
    int can_lie = 0;
    for (int i = 0; i < Party_Cnt; i++) {
        bool can_lie_party = true;
        for (int j = 0; j < party_list[i].size(); j++) {
            if (truth_know_people[party_list[i][j] - 1] != 0) {
                can_lie_party = false;
                break;
            }
        }
        if (can_lie_party) {
            can_lie++;
        }
    }

    std::cout << can_lie;
}