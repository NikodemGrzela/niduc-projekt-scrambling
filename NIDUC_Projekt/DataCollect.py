import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Sender import Sender
from Receiver import Receiver
from Channel import Channel
from XORKeyScrambler import XORKeyScrambler
from BLEScrambler import BLEScrambler
from DBEScrambler import DBEScrambler
from V34Scrambler import V34Scrambler

# Ja wybralem takie ale mogą być też inne
signal_lengths = [1000, 25000, 50000, 100000, 250000]
percentages_of_ones = [0, 25, 50, 75, 100]
# Zwiekszyć dla wiekszej dokładności w ostatecznym sprawku (do 500 wystarczy myśle)
num_iterations = 5

scramblers = {
    'XORKeyScrambler': XORKeyScrambler(),
    'BLEScrambler': BLEScrambler(),
    'DBEScrambler': DBEScrambler(),
    'V34Scrambler': V34Scrambler()
}

# DataFrame
results = pd.DataFrame(columns=['Scrambler', 'Signal Length', 'Percentage of Ones', 'Execution Time', 'Accuracy'])
std_devs = pd.DataFrame(columns=['Scrambler', 'Signal Length', 'Percentage of Ones', 'Execution Time Std', 'Accuracy Std'])


# Główna pętla do zbierania danych
for length in signal_lengths:
    for percentage in percentages_of_ones:
        for scrambler_name, scrambler in scramblers.items():
            sender = Sender(scrambler)
            receiver = Receiver(scrambler)
            channel = Channel()

            total_time = 0
            total_accuracy = 0
            execution_times = []
            accuracies = []

            for _ in range(num_iterations):
                # Generowanie sygnału
                signal = generate_signal(length, percentage)
                sender.data = signal

                # Pomiar czasu scramblowania
                start_time = time.time()
                scrambled_signal = sender.send_data()
                scrambling_time = time.time() - start_time

                # Wysyłanie sygnału scramblowanego przez kanał
                channel.receive_data(scrambled_signal)
                noisy_signal = channel.send_data()

                # Pomiar czasu descramblowania i dokładności
                receiver.receive_data(noisy_signal)
                start_time = time.time()
                descrambled_signal = receiver.descrambler.descramble(noisy_signal)
                descrambling_time = time.time() - start_time

                iteration_time = scrambling_time + descrambling_time
                iteration_accuracy = sum(1 for a, b in zip(signal, descrambled_signal) if a == b) / len(signal) * 100

                total_time += iteration_time
                total_accuracy += iteration_accuracy
                execution_times.append(iteration_time)
                accuracies.append(iteration_accuracy)

            avg_time = total_time / num_iterations
            avg_accuracy = total_accuracy / num_iterations
            std_exec_time = np.std(execution_times)
            std_accuracy = np.std(accuracies)

            new_row = pd.DataFrame({
                'Scrambler': [scrambler_name],
                'Signal Length': [length],
                'Percentage of Ones': [percentage],
                'Execution Time': [avg_time],
                'Accuracy': [avg_accuracy]
            })

            new_std_row = pd.DataFrame({
                'Scrambler': [scrambler_name],
                'Signal Length': [length],
                'Percentage of Ones': [percentage],
                'Execution Time Std': [std_exec_time],
                'Accuracy Std': [std_accuracy]
            })

            if not new_row.isna().all().all():
                results = pd.concat([results, new_row], ignore_index=True)

            if not new_std_row.isna().all().all():
                std_devs = pd.concat([std_devs, new_std_row], ignore_index=True)

            # Wypisanie wyników na konsolę żeby sprawdzić czy bangla
            print(f"Scrambler: {scrambler_name}, Length: {length}, Ones: {percentage}%, Avg Time: {avg_time:.4f}s, Avg Accuracy: {avg_accuracy:.2f}%")

results = results.merge(std_devs, on=['Scrambler', 'Signal Length', 'Percentage of Ones'])

# Zapisanie wyników do pliku CSV
results.to_csv('scrambling_results.csv', index=False)

# Wykresy czas wykonania vs długość sygnału dla każdego procentu jedynek i dokładność vs długość sygnału dla każdego procentu jedynek
for metric, std_metric in [('Execution Time', 'Execution Time Std'), ('Accuracy', 'Accuracy Std')]:
    for scrambler_name in scramblers.keys():
        plt.figure(figsize=(12, 6))
        for percentage in percentages_of_ones:
            subset = results[(results['Scrambler'] == scrambler_name) & (results['Percentage of Ones'] == percentage)]
            plt.errorbar(subset['Signal Length'], subset[metric], yerr=subset[std_metric], marker='o',
                         label=f'{percentage}% ones')

        plt.title(f'{metric} for {scrambler_name}')
        plt.xlabel('Signal Length (bits)')
        plt.ylabel(f'{metric} (s)' if metric == 'Execution Time' else f'{metric} (%)')
        plt.grid(True)
        plt.legend(title='Percentage of Ones')
        plt.xticks(signal_lengths)
        plt.show()

# Dodatkowe wykresy

# Czas wykonania vs procent jedynek dla każdej długości sygnału
for length in signal_lengths:
    plt.figure(figsize=(12, 6))
    for scrambler_name in scramblers.keys():
        subset = results[(results['Signal Length'] == length) & (results['Scrambler'] == scrambler_name)]
        plt.errorbar(subset['Percentage of Ones'], subset['Execution Time'], yerr=subset['Execution Time Std'],
                     marker='o', label=scrambler_name)

    plt.title(f'Execution Time for Signal Length {length}')
    plt.xlabel('Percentage of Ones (%)')
    plt.ylabel('Execution Time (s)')
    plt.grid(True)
    plt.legend(title='Scrambler')
    plt.xticks(percentages_of_ones)
    plt.show()

# Dokładność vs procent jedynek dla każdej długości sygnału
for length in signal_lengths:
    plt.figure(figsize=(12, 6))
    for scrambler_name in scramblers.keys():
        subset = results[(results['Signal Length'] == length) & (results['Scrambler'] == scrambler_name)]
        plt.errorbar(subset['Percentage of Ones'], subset['Accuracy'], yerr=subset['Accuracy Std'], marker='o',
                     label=scrambler_name)

    plt.title(f'Accuracy for Signal Length {length}')
    plt.xlabel('Percentage of Ones (%)')
    plt.ylabel('Accuracy (%)')
    plt.grid(True)
    plt.legend(title='Scrambler')
    plt.xticks(percentages_of_ones)
    plt.show()

# Czas wykonania vs długość sygnału dla każdego procentu jedynek
for percentage in percentages_of_ones:
    plt.figure(figsize=(12, 6))
    for scrambler_name in scramblers.keys():
        subset = results[(results['Percentage of Ones'] == percentage) & (results['Scrambler'] == scrambler_name)]
        plt.errorbar(subset['Signal Length'], subset['Execution Time'], yerr=subset['Execution Time Std'], marker='o',
                     label=scrambler_name)

    plt.title(f'Execution Time for {percentage}% Ones')
    plt.xlabel('Signal Length (bits)')
    plt.ylabel('Execution Time (s)')
    plt.grid(True)
    plt.legend(title='Scrambler')
    plt.xticks(signal_lengths)
    plt.show()

# Dokładność vs długość sygnału dla każdego procentu jedynek
for percentage in percentages_of_ones:
    plt.figure(figsize=(12, 6))
    for scrambler_name in scramblers.keys():
        subset = results[(results['Percentage of Ones'] == percentage) & (results['Scrambler'] == scrambler_name)]
        plt.errorbar(subset['Signal Length'], subset['Accuracy'], yerr=subset['Accuracy Std'], marker='o',
                     label=scrambler_name)

    plt.title(f'Accuracy for {percentage}% Ones')
    plt.xlabel('Signal Length (bits)')
    plt.ylabel('Accuracy (%)')
    plt.grid(True)
    plt.legend(title='Scrambler')
    plt.xticks(signal_lengths)
    plt.show()
