#include <iostream>
#include <vector>

class Birds {
private:
	std::string b_Name;
public:
	Birds(std::string Name) {
		b_Name = Name;
	}

	std::string GetName() {
		return b_Name;
	}
};


int main() {
	//Первый пункт
	std::vector <std::string> animals = {"cat", "dog", "lion", "NastyaCh"};
	
	animals.push_back("duck");
	animals.insert(animals.begin(), "bird");

	for (int i = 0; i < animals.size(); i++)
		std::cout << animals[i] << " ";
	std::cout << std::endl;

	animals.erase(animals.begin()+4);

	for (int i = 0; i < animals.size(); i++)
		std::cout << animals[i] << " ";
	std::cout << std::endl;

	animals.erase(animals.begin() + 3, animals.end());

	for (int i = 0; i < animals.size(); i++)
		std::cout << animals[i] << " ";
	std::cout << std::endl;

	//Второй пункт
	Birds Stiven("Stiven");
	std::vector <Birds> parrots;
	parrots.emplace_back("Stiven");
	parrots.push_back(Stiven);
	//parrots.push_back("Stiven");

	std::cout << parrots[0].GetName() << " " << parrots[1].GetName() << std::endl;

	//Трейти пункт
	animals.resize(6); //Меняем размер

	std::cout << animals.size() << ": ";
	for (int i = 0; i < animals.size(); i++)
		std::cout << animals[i] << " ";
	std::cout << "end" << std::endl;

	animals.resize(8, "rat");

	std::cout << animals.size() << ": ";
	for (int i = 0; i < animals.size(); i++)
		std::cout << animals[i] << " ";
	std::cout << std::endl;

	std::vector <int> Numbers(1);  // задаем размер
	Numbers[0] = 0;
	std::cout << Numbers.capacity() << " " << Numbers.size() << std::endl;
	Numbers.reserve(3);
	std::cout << Numbers.capacity() << " " << Numbers.size() << std::endl;;

	Numbers.push_back(0);
	std::cout << Numbers.capacity() << " " << Numbers.size() << std::endl;;

	Numbers.shrink_to_fit();
	std::cout << Numbers.capacity() << " " << Numbers.size() << std::endl;;

	std::cout << std::endl;

	return 0;
}
