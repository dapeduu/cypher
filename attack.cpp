#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <regex>
using namespace std;

double calculate_ic(const string& text) {
    // Calculate the Index of Coincidence (IC)
    string cleaned_text = regex_replace(text, regex("[^a-zA-Z]"), "");
    int n = cleaned_text.length();
    if (n <= 1) {
        return 0.0;
    }
    map<char, int> freq_count;
    for (char c : cleaned_text) {
        freq_count[c]++;
    }
    double ic = 0.0;
    for (const auto& entry : freq_count) {
        int freq = entry.second;
        ic += static_cast<double>(freq * (freq - 1)) / (n * (n - 1));
    }
    return ic;
}

int find_key_length(const string& encrypted_text) {
    // Try different key lengths and calculate IC for each
    int max_length = min(20, static_cast<int>(encrypted_text.length()));
    vector<pair<int, double>> ic_values;

    for (int key_length = 1; key_length <= max_length; ++key_length) {
        vector<string> segments(key_length);
        for (int i = 0; i < key_length; ++i) {
            for (int j = i; j < static_cast<int>(encrypted_text.length()); j += key_length) {
                segments[i] += encrypted_text[j];
            }
        }
        double avg_ic = 0.0;
        for (const string& segment : segments) {
            avg_ic += calculate_ic(segment);
        }
        avg_ic /= key_length;
        ic_values.emplace_back(key_length, avg_ic);
    }

    // Find the key length with the highest IC
    auto max_ic_it = max_element(ic_values.begin(), ic_values.end(),
        [](const pair<int, double>& a, const pair<int, double>& b) {
            return a.second < b.second;
        });

    return max_ic_it->first;
}

string vigenere_decrypt(const string& encrypted_text, const string& key) {
    string decrypted_text = "";
    int key_length = key.length();

    for (size_t i = 0; i < encrypted_text.length(); ++i) {
        char encrypted_char = encrypted_text[i];
        if (isalpha(encrypted_char)) {
            char key_char = key[i % key_length];
            int shift = toupper(key_char) - 'A';
            if (isupper(encrypted_char)) {
                char decrypted_char = ((encrypted_char - 'A' - shift + 26) % 26) + 'A';
                decrypted_text += decrypted_char;
            } else {
                char decrypted_char = ((encrypted_char - 'a' - shift + 26) % 26) + 'a';
                decrypted_text += decrypted_char;
            }
        } else {
            decrypted_text += encrypted_char;
        }
    }

    return decrypted_text;
}

int main() {
    string encrypted_text = "Rkfojyhu amavq jw slwjfsvctsv!";
    int best_key_length = find_key_length(encrypted_text);
    cout << "Best Key Length: " << best_key_length << endl;

    // Now, let's try to find the key using common English words (a simple dictionary attack)
    ifstream word_file("english_words.txt");
    set<string> english_words;
    string word;
    while (getline(word_file, word)) {
        transform(word.begin(), word.end(), word.begin(), ::tolower);
        english_words.insert(word);
    }

    string key = "";
    for (int i = 0; i < best_key_length; ++i) {
        string segment;
        for (int j = i; j < static_cast<int>(encrypted_text.length()); j += best_key_length) {
            segment += encrypted_text[j];
        }
        map<string, int> word_count;
        for (const string& english_word : english_words) {
            word_count[english_word] = count(segment.begin(), segment.end(), english_word[0]);
        }
        string most_common_word;
        int max_count = 0;
        for (const auto& entry : word_count) {
            if (entry.second > max_count) {
                most_common_word = entry.first;
                max_count = entry.second;
            }
        }
        char key_char = ((most_common_word[0] - 'a' + 26) % 26) + 'a';
        key += key_char;
    }

    string decrypted_text = vigenere_decrypt(encrypted_text, key);
    cout << "Decrypted with Key: " << key << endl;
    cout << "Decrypted Text: " << decrypted_text << endl;

    return 0;
}
