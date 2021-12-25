from multiprocessing import Process
import os

class Matrix:

    def __init__(self, A, B):
        self.A = self.read_file_matrix(A)
        self.B = self.read_file_matrix(B)
        self.C = [[0 for _ in range(len(self.A))] for _ in range(len(self.A))]
        self.processing_m()

    @staticmethod
    def read_file_matrix(filename):
        """
        Здесь мы из файла обрабатываем значения элементов матрицы
        и возвращаем их уже в список списков

        :filename parametr: имя файла для анализа
        :return: список списков значений матрицы
        """

        with open(filename, mode="r", encoding="utf-8") as f:
            return [[int(i) for i in line.split(" ")] for line in f]

    def processing_m(self):
        """
        Основная работа с процессами

        :return: None
        """

        proc_ss = []
        cell_ss = []

        for i in range(len(self.A)):
            for j in range(len(self.A)):
                cell_ss.append((i, j))

        try:
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), "C_matrix.txt"))
        except FileNotFoundError:
            pass

        for i, j in cell_ss:
            proc = Process(target=self.elem_matrix, args=[i, j])
            proc_ss.append(proc)

        for proc in proc_ss:
            print(proc.name)

            proc.start()
            proc.join()

    def elem_matrix(self, i, j):
        """
        Происходит умножение матрицы и запись значения в файл
        :param i: строка
        :param j: столбец
        :return: матрица с одним значением, которое и вычислял процесс
        """

        self.C[i][j] = sum(self.A[i][m] * self.B[m][j] for m in range(len(self.A[0]) or len(self.B)))

        with open("C_matrix.txt", mode="a", encoding="utf-8") as f:
            if i == j == 0:
                f.write(str(self.C[i][j]) + " ")
            elif j == 0:
                f.write("\n" + str(self.C[i][j]) + " ")
            else:
                f.write(str(self.C[i][j]) + " ")

        return self.C


if __name__ == "__main__":
    result = Matrix("A_matrix.txt", "B_matrix.txt")