#include <iostream>
#include <fstream> // ������ � �������
#include <string>
#include <cstring>


// � ��������� ����� input.txt ������� ������� �����.
// ������ � ������� �� ���� ������ � ������������ ������
// ����� � ������ �����, ���������� �����, �� �������� � ������, 
// �������� �� ���������� ������� � ������� ����� ������� ������ ����� � ������� ��������� �����. 
// ���������� ����� �������� � ���� output.txt. ���� �����, ����� ��������� ����, ������ �������� ����������, 
// ������� � ����� ����������.


namespace lab {
	int Max() {
		setlocale(LC_ALL, "rus"); // ���������� ����������� ���������
		std::ifstream file("�����.txt"); // ������� ���� ��� ������

		int max = 0;
		std::string variable;
		while (file >> variable) {
			if (ispunct(variable[0]) != 0)
				variable.erase(variable.cbegin());//�������� �� ����������
			if (ispunct(variable[size(variable) - 1]) != 0)
				variable.erase(variable.cend() - 1);//�������� �� ����������

			if (size(variable) > max)
				max = size(variable); //������� ������������ ����� ����
		}
		file.close(); // ��������� ����
		return max;
	}

	std::string LetterFromMax(int max) { // ������� ������ ���� �� ���� � ������������ ������
		setlocale(LC_ALL, "rus"); // ���������� ����������� ���������
		std::ifstream file("�����.txt"); // ������� ���� ��� ������

		std::string Letters;
		//char Letters[33] = {' '};
		//int k = 0;

		std::string variable;
		while (file >> variable) {

			if (ispunct(variable[0]) != 0)
				variable.erase(variable.cbegin());//�������� �� ����������
			if (ispunct(variable[size(variable) - 1]) != 0)
				variable.erase(variable.cend() - 1);//�������� �� ����������

			if (size(variable) == max) {
				for (int i = 0; i < size(variable); i++) {
					bool flag = true;

					if ((int)variable[i] < -32) { // ������� ��������� ����� �� �����
						variable[i] = (char)((int)variable[i] + 32);
					}

					for (int j = 0; j < size(Letters); j++) {
						if (Letters[j] == variable[i]) {
							flag = false;
							break;
						}
					}

					if (flag == true)
						Letters += variable[i];	
				}
			}
		}
		
		file.close(); // ��������� ����
		return Letters;
	}

	int max = Max();
	std::string Letters = LetterFromMax(max); //������ ���� �� ���� � ������������ �������


	//char* LettersNotMax(std::string word) { //�������� ������ ���� �����
	std::string LettersNotMax(std::string word) {
		//char LettersWord[33];
		//int k = 0;

		std::string LettersWord;

		if (ispunct(word[0]) != 0)
			word.erase(word.cbegin());//�������� �� ����������
		if (ispunct(word[size(word) - 1]) != 0)
			word.erase(word.cend() - 1);
		
		for (int i = 0; i < word.length(); i++) {
			bool Flag = true;
			if ((int)word[i] < -32) { // ������� ��������� ����� �� �����
				word[i] = (char)((int)word[i] + 32);
			}
			for (int j = 0; j < Letters.length(); j++)
				if (word[i] == Letters[j]) {
					Flag = false;
				}
			if (Flag == true) 
				LettersWord += word[i];
		}
		return LettersWord;
	}

	bool Proverka(std::string LettersVariable, char k) {
		bool flag = false;
		for (int i = 0; i < LettersVariable.length(); i++)
		{
			if (k == LettersVariable[i]) {
				flag = true;
			}
		}
		return flag;
	}


	void Change() {
		setlocale(LC_ALL, "rus"); // ���������� ����������� ���������
		std::ifstream file("�����.txt"); // ������� ���� ��� ������
		std::ofstream fout("File.txt"); // ��������� ���� ��� ���������� ���������� � ����� �����

		std::string variable;

		while (file >> variable) {
			//char* LettersVariable = LettersNotMax(variable);

			std::string LettersVariable = LettersNotMax(variable);
			
			//std::cout << char(-64) << " ";
			//for (int i = 0; i < size(LettersVariable); i++) {
			//	std::cout << LettersVariable[i];
			//}
			//std::cout << " ";

			if (size(LettersVariable) != 0) {
				for (int i = 0; i < size(variable); i++)
					if ((int)variable[i] > -32 && Proverka(LettersVariable, variable[i]) == true)
					{
						int capital = (int)variable[i] - 32;
						fout << char(capital);
					}
					else {
						fout << variable[i];
					}
				fout << "(";

				for (int i = 0; i < size(LettersVariable); i++)
					fout << LettersVariable[i];

				fout << ") ";
			}
			else {
				fout << variable << " ";
			}
			
		}

		
	}
}