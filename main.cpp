#include <iostream>
#include <set>
#include <algorithm>

int main() {
    std::set<int> set1 = { 1, 2, 3, 4, 5 };
    std::set<int> set2 = { 3, 4, 5, 6, 7 };
    std::set<int> result;

    // Используем алгоритм std::set_intersection для вычисления пересечения множеств
    std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), std::inserter(result, result.begin()));
    setlocale(LC_ALL, "Russian");
    std::cout << "Результат объединения множеств с использованием пересечения: ";
    for (int element : result) {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    return 0;
}
