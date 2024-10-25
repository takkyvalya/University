#include <iostream>
#include <fstream> // работа с файлами
#include <string>
#include <cstring>


// В текстовом файле input.txt записан русский текст.
// Массив с буквами из слов текста с максимальной длиной
// Найти в тексте слова, содержащие букву, не входящую в массив, 
// записать их заглавными буквами и указать после каждого такого слова в скобках найденные буквы. 
// Полученный текст записать в файл output.txt. Весь текст, кроме найденных слов, должен остаться неизменным, 
// включая и знаки препинания.


namespace lab {
	int Max() {
		setlocale(LC_ALL, "rus"); // корректное отображение Кириллицы
		std::ifstream file("Текст.txt"); // открыли файл для чтения

		int max = 0;
		std::string variable;
		while (file >> variable) {
			if (ispunct(variable[0]) != 0)
				variable.erase(variable.cbegin());//Проверка на пунктуацию
			if (ispunct(variable[size(variable) - 1]) != 0)
				variable.erase(variable.cend() - 1);//Проверка на пунктуацию

			if (size(variable) > max)
				max = size(variable); //находим максимальную длину слов
		}
		file.close(); // закрываем файл
		return max;
	}

	std::string LetterFromMax(int max) { // создаем массив букв из слов с максимальной длиной
		setlocale(LC_ALL, "rus"); // корректное отображение Кириллицы
		std::ifstream file("Текст.txt"); // открыли файл для чтения

		std::string Letters;
		//char Letters[33] = {' '};
		//int k = 0;

		std::string variable;
		while (file >> variable) {

			if (ispunct(variable[0]) != 0)
				variable.erase(variable.cbegin());//Проверка на пунктуацию
			if (ispunct(variable[size(variable) - 1]) != 0)
				variable.erase(variable.cend() - 1);//Проверка на пунктуацию

			if (size(variable) == max) {
				for (int i = 0; i < size(variable); i++) {
					bool flag = true;

					if ((int)variable[i] < -32) { // убираем заглавные буквы из слова
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
		
		file.close(); // закрываем файл
		return Letters;
	}

	int max = Max();
	std::string Letters = LetterFromMax(max); //массив букв из слов с максимальной длинной


	//char* LettersNotMax(std::string word) { //создадим массив букв слова
	std::string LettersNotMax(std::string word) {
		//char LettersWord[33];
		//int k = 0;

		std::string LettersWord;

		if (ispunct(word[0]) != 0)
			word.erase(word.cbegin());//Проверка на пунктуацию
		if (ispunct(word[size(word) - 1]) != 0)
			word.erase(word.cend() - 1);
		
		for (int i = 0; i < word.length(); i++) {
			bool Flag = true;
			if ((int)word[i] < -32) { // убираем заглавные буквы из слова
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
		setlocale(LC_ALL, "rus"); // корректное отображение Кириллицы
		std::ifstream file("Текст.txt"); // открыли файл для чтения
		std::ofstream fout("File.txt"); // открываем файл для добавления информации к концу файла

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