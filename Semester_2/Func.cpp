#include <iostream>
#include <fstream> // ðàáîòà ñ ôàéëàìè
#include <string>

namespace lab {
	std::ifstream file("Òåêñò.txt"); // îòêðûëè ôàéë äëÿ ÷òåíèÿ

	int Number(int M[1000]) {
		std::string p;
		file >> p;
		int n = size(p);
		for (int i = 0; i < n; i++) {
			M[i] = int(p[n-i-1]) - 48;
		}
		return n;
	}

	int* Addition(int A[1000], int n, int B[1000], int m) {
		if (m > n)
			n = m;
		int sum = 0;
		int Sub[1000];
		for (int i = 0; i < n; i++) {
			sum += A[i] + B[i];
			if (sum > 9) {
				Sub[i] = sum % 10;
				sum = sum / 10;
			}
			else {
				Sub[i] = sum;
				sum = 0;
			}
		}
		return Sub;
	}

	int FinalNumber(int Sub[1000], int n, int m) {
		if (m > n)
			n = m;

		int FN = 0;
		for (int i = 0; i < n; i++) {
			FN = FN * 10 + Sub[n-i-1];
		}
		std::cout << FN;
		return FN;
	}

	int* MultiplicationOfNumber(int B[1000], int n, int A) {
		int M[1000] = { 0 };
		int remainder = 0;
		for (int i = 0; i < n+1; i++) {
			M[i] = A * B[i] % 10 + remainder;
			remainder = A * B[i] / 10; 
		}
		return M;
	}

	int* Multiplication(int A[1000], int n, int B[1000], int m) {
		if (m > n)
			n = m;

		int Milt[1000] = { 0 };

		for (int i = 0; i < n; i++) {
			int* M = MultiplicationOfNumber(B, n, A[i]);
			int Param[1000] = {0};

			for (int j = 0; j < n+1; j++) {
				Param[j+i] = M[j];
			}

			int* Parametr = Addition(Milt, n + 1 + i, Param, n);
			for (int j = 0; j < n + 1 + i; j++) {
				Milt[j] = Parametr[j];
			}
		}

		return Milt;
	}
}
