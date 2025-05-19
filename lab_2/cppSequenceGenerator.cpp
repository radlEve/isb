#include <iostream>
#include <string>
#include <random>

std::string generateMyBinaryString(size_t length) {
    std::random_device seeder;
    std::mt19937 randomNumberEngine(seeder());
    std::uniform_int_distribution<int> bitDistribution(0, 1);

    std::string sequenceStr = "";
    sequenceStr.reserve(length);

    for (size_t i = 0; i < length; ++i) {
        sequenceStr += std::to_string(bitDistribution(randomNumberEngine));
    }
    return sequenceStr;
}

int main() {
    const size_t sequenceLength = 128;
    std::string my_binary_sequence = generateMyBinaryString(sequenceLength);

    std::cout << "My generated C++ sequence (" << sequenceLength << " bits):" << std::endl;
    std::cout << my_binary_sequence << std::endl;

    return 0;
}