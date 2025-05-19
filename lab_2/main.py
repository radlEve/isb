from math import erfc
from scipy.special import gammaincc

from constants import *


def frequency_bitwise_test(data: str) -> float:
    """
    Частотный побитовый анализ
    :param data: последовательность в виде строки
    :return: вер-ть произведения генератором случайных чисел
    """
    s = 0
    for i in data:
        if i == '0':
            s -= 1
        if i == '1':
            s += 1
    s = s / (len(data) ** 0.5)

    return erfc(abs(s / (2 ** 0.5)))


def consecutive_running_bits_test(data: str) -> float:
    """
    Тест на одинаковые подряд идущие биты
    :param data: последовательность в виде строки
    :return: вер-ть произведения генератором случайных чисел
    """
    n_len = len(data)
    s_ones = 0
    for i in data:
        if i == '1':
            s_ones += 1
    zeta = s_ones / n_len

    if not (abs(zeta - 0.5) < (2 / n_len ** 0.5)):
        return 0.0

    v = 0
    for i in range(n_len - 1):
        if data[i] != data[i + 1]:
            v += 1

    return erfc(abs(v - 2 * n_len * zeta * (1 - zeta)) / (2 * (2 * n_len) ** 0.5 * zeta * (1 - zeta)))


def longest_sequence_test(data: str) -> float:
    """
        Тест на самую длинную последовательность единиц в блоке
        :param data: последовательность в виде строки
        :return: вер-ть произведения генератором случайных чисел
        """
    v_counts = [0, 0, 0, 0]
    m_block_size = 8
    n_blocks = len(data) / m_block_size  # 128 / 8 = 16
    blocks = [data[i:i + m_block_size] for i in range(0, len(data), m_block_size)]
    for block in blocks:
        max_run = 0
        current_run = 0
        for bit in block:
            if bit == '1':
                current_run += 1
            else:
                max_run = max(current_run, max_run)
                current_run = 0
        max_run = max(current_run, max_run)
        if max_run <= 1:
            v_counts[0] += 1
        if max_run == 2:
            v_counts[1] += 1
        if max_run == 3:
            v_counts[2] += 1
        if max_run >= 4:
            v_counts[3] += 1

    chi_squared_obs = 0
    for i in range(len(v_counts)):
        chi_squared_obs += (v_counts[i] - n_blocks * PI[i]) ** 2 / (n_blocks * PI[i])

    return gammaincc(3.0 / 2.0, chi_squared_obs / 2.0)


def main():
    output_filename = "lab_results.txt"

    results_to_write = []

    p_freq_cpp = frequency_bitwise_test(cppSequence)
    p_runs_cpp = consecutive_running_bits_test(cppSequence)
    p_longest_cpp = longest_sequence_test(cppSequence)

    results_to_write.append(f"C++ generator\nSequence: {cppSequence}")
    results_to_write.append(
        f"Frequency bitwise test: {p_freq_cpp:.16f}")
    results_to_write.append(f"Identical consecutive bits test: {p_runs_cpp:.16f}")
    results_to_write.append(f"Max ones sequence test: {p_longest_cpp:.16f}")
    results_to_write.append("\n")

    p_freq_java = frequency_bitwise_test(javaSequence)
    p_runs_java = consecutive_running_bits_test(javaSequence)
    p_longest_java = longest_sequence_test(javaSequence)

    results_to_write.append(f"Java generator\nSequence: {javaSequence}")
    results_to_write.append(f"Frequency bitwise test: {p_freq_java:.16f}")
    results_to_write.append(f"Identical consecutive bitsTest: {p_runs_java:.16f}")
    results_to_write.append(f"Max ones sequence test: {p_longest_java:.16f}")
    results_to_write.append("\n")

    try:
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            for line in results_to_write:
                f_out.write(line + "\n")
        print(f"Анализ завершен. Результаты сохранены в файл '{output_filename}'")

        print("\n--- Результаты анализа ---")
        for line in results_to_write:
            print(line)

    except IOError:
        print(f"Ошибка: Не удалось записать в файл {output_filename}")


if __name__ == "__main__":
    main()
