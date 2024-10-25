#include <iostream>
#include <fstream> // ðàáîòà ñ ôàéëàìè
#include <string>
#include <cstring>


// Â òåêñòîâîì ôàéëå input.txt çàïèñàí ðóññêèé òåêñò.
// Ìàññèâ ñ áóêâàìè èç ñëîâ òåêñòà ñ ìàêñèìàëüíîé äëèíîé
// Íàéòè â òåêñòå ñëîâà, ñîäåðæàùèå áóêâó, íå âõîäÿùóþ â ìàññèâ, 
// çàïèñàòü èõ çàãëàâíûìè áóêâàìè è óêàçàòü ïîñëå êàæäîãî òàêîãî ñëîâà â ñêîáêàõ íàéäåííûå áóêâû. 
// Ïîëó÷åííûé òåêñò çàïèñàòü â ôàéë output.txt. Âåñü òåêñò, êðîìå íàéäåííûõ ñëîâ, äîëæåí îñòàòüñÿ íåèçìåííûì, 
// âêëþ÷àÿ è çíàêè ïðåïèíàíèÿ.


namespace lab {
	int Max() {
		setlocale(LC_ALL, "rus"); // êîððåêòíîå îòîáðàæåíèå Êèðèëëèöû
		std::ifstream file("Òåêñò.txt"); // îòêðûëè ôàéë äëÿ ÷òåíèÿ

		int max = 0;
		std::string variable;
		while (file >> variable) {
			if (ispunct(variable[0]) != 0)
				variable.erase(variable.cbegin());//Ïðîâåðêà íà ïóíêòóàöèþ
			if (ispunct(variable[size(variable) - 1]) != 0)
				variable.erase(variable.cend() - 1);//Ïðîâåðêà íà ïóíêòóàöèþ

			if (size(variable) > max)
				max = size(variable); //íàõîäèì ìàêñèìàëüíóþ äëèíó ñëîâ
		}
		file.close(); // çàêðûâàåì ôàéë
		return max;
	}

	std::string LetterFromMax(int max) { // ñîçäàåì ìàññèâ áóêâ èç ñëîâ ñ ìàêñèìàëüíîé äëèíîé
		setlocale(LC_ALL, "rus"); // êîððåêòíîå îòîáðàæåíèå Êèðèëëèöû
		std::ifstream file("Òåêñò.txt"); // îòêðûëè ôàéë äëÿ ÷òåíèÿ

		std::string Letters;
		//char Letters[33] = {' '};
		//int k = 0;

		std::string variable;
		while (file >> variable) {

			if (ispunct(variable[0]) != 0)
				variable.erase(variable.cbegin());//Ïðîâåðêà íà ïóíêòóàöèþ
			if (ispunct(variable[size(variable) - 1]) != 0)
				variable.erase(variable.cend() - 1);//Ïðîâåðêà íà ïóíêòóàöèþ

			if (size(variable) == max) {
				for (int i = 0; i < size(variable); i++) {
					bool flag = true;

					if ((int)variable[i] < -32) { // óáèðàåì çàãëàâíûå áóêâû èç ñëîâà
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
		
		file.close(); // çàêðûâàåì ôàéë
		return Letters;
	}

	int max = Max();
	std::string Letters = LetterFromMax(max); //ìàññèâ áóêâ èç ñëîâ ñ ìàêñèìàëüíîé äëèííîé


	//char* LettersNotMax(std::string word) { //ñîçäàäèì ìàññèâ áóêâ ñëîâà
	std::string LettersNotMax(std::string word) {
		//char LettersWord[33];
		//int k = 0;

		std::string LettersWord;

		if (ispunct(word[0]) != 0)
			word.erase(word.cbegin());//Ïðîâåðêà íà ïóíêòóàöèþ
		if (ispunct(word[size(word) - 1]) != 0)
			word.erase(word.cend() - 1);
		
		for (int i = 0; i < word.length(); i++) {
			bool Flag = true;
			if ((int)word[i] < -32) { // óáèðàåì çàãëàâíûå áóêâû èç ñëîâà
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
		setlocale(LC_ALL, "rus"); // êîððåêòíîå îòîáðàæåíèå Êèðèëëèöû
		std::ifstream file("Òåêñò.txt"); // îòêðûëè ôàéë äëÿ ÷òåíèÿ
		std::ofstream fout("File.txt"); // îòêðûâàåì ôàéë äëÿ äîáàâëåíèÿ èíôîðìàöèè ê êîíöó ôàéëà

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
