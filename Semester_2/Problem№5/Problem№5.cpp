// Задача№5.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
#include <iostream>


class Massiv {
private: 
    int m_size = 0; 
    int* m_mas = new int[m_size];
public: 
    Massiv(int num) {
        m_size = num;
    }
    ~Massiv() {
        delete[] m_mas;
        std::cout << "Destructor work" << std::endl;
    }

    void SetElement(int Number) {
        int* newMas = new int[m_size + 1];

        for (int i = 0; i < m_size; i++)
            newMas[i] = m_mas[i];

        newMas[m_size + 1 - 1] = Number;

        delete[] m_mas;
        m_mas = newMas;
        m_size++;

        //delete[] newMas;
    }

    int GetSize() {
        return m_size;
    }

    int GetElement(int index) {
        return m_mas[index];
    }

    void SetElementOnIndex(int Number, int index) {
        if (index >= m_size) {
            while (m_size <= index) {
                SetElement(0);
            }
            SetElement(Number);
        } 
        else {
            m_mas[index] = Number;
        }
    }

    void DeleteElement(int index) {
        int* newMas = new int[m_size - 1];

        for (int i = 0; i < index; i++) {
            newMas[i] = m_mas[i];
        }

        int k = index;
        for (int i = index + 1; i < m_size; i++) {
            newMas[k] = m_mas[i];
            k++;
        }

        delete[] m_mas;
        m_mas = newMas;
        m_size--;

        //delete[] newMas;
    }

    void AddElement(int Number, int index) {
        int* newMas = new int[m_size + 1];

        for (int i = 0; i < index; i++) {
            newMas[i] = m_mas[i];
        }

        newMas[index] = Number;
        int k = index+1;

        for (int i = index; i < m_size; i++) {
            newMas[k] = m_mas[i];
            k++;
        }

        delete[] m_mas;
        m_mas = newMas;
        m_size++;

        //delete[] newMas;
    }
};



int main()
{
    Massiv Cat(0);
   
    Cat.SetElement(3);
    Cat.SetElement(4);
    Cat.SetElement(5);

    
    std::cout << Cat.GetSize() << std::endl;
    std::cout << Cat.GetElement(0) << std::endl;
    std::cout << Cat.GetElement(2) << std::endl;

    Cat.SetElementOnIndex(7, 1);
    std::cout << Cat.GetElement(1) << std::endl;

    Cat.DeleteElement(0);
    std::cout << Cat.GetElement(0) << std::endl;

    Cat.AddElement(3, 0);
    std::cout << Cat.GetElement(0) << std::endl;
    
}
