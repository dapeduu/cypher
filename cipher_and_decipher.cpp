#include <iostream>
#include <string>
using namespace std;

string vigenere_encrypt(const string& plain_text, const string& key) {
    string encrypted_text = "";
    int key_length = key.length();

    for (size_t i = 0; i < plain_text.length(); ++i) {
        char plain_char = plain_text[i];
        if (isalpha(plain_char)) {
            char key_char = key[i % key_length];
            int shift = toupper(key_char) - 'A';
            if (isupper(plain_char)) {
                char encrypted_char = ((plain_char - 'A' + shift) % 26) + 'A';
                encrypted_text += encrypted_char;
            } else {
                char encrypted_char = ((plain_char - 'a' + shift) % 26) + 'a';
                encrypted_text += encrypted_char;
            }
        } else {
            encrypted_text += plain_char;
        }
    }

    return encrypted_text;
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
    string plaintext = "HELLO";
    string key = "KEY";

    string encrypted_text = vigenere_encrypt(plaintext, key);
    cout << "Encrypted: " << encrypted_text << endl;

    string decrypted_text = vigenere_decrypt(encrypted_text, key);
    cout << "Decrypted: " << decrypted_text << endl;

    return 0;
}
