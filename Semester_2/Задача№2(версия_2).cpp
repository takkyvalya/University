#include <iostream>
#include "Func.hpp"

int main()
{

	int A[1000] = {};
	int B[1000] = {};
	int n;
	int m;

	n = lab::Number(A); //чтение из файла числа и преобразование в массив цифр
	m = lab::Number(B);

	//int* Sub = lab::Addition(A, n, B, m);
	//int FN = lab::FinalNumber(Sub, n, m);
	int* M = lab::Multiplication(A, n, B, m);
	int FN = lab::FinalNumber(M, n + m, m + n);
}
