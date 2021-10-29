#include <iostream>
#include <mpi.h>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]){
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);



    if (rank == 0){
        double suma;
        int wartosc;
        ifstream plik_txt("plik.txt");
        plik_txt >> wartosc;
        cout << "Wprowadzona wartosc z pliku : " << wartosc << endl; 

        double *liczby_tab = new double[wartosc];
        cout << "Wprowadzone liczby : ";
        for (int i = 0; i < wartosc; i++){
            plik_txt >> liczby_tab[i];
            cout << liczby_tab[i] << " ";
        }
        cout << endl;
        MPI_Send(&wartosc, 1, MPI_INT, 1, 102, MPI_COMM_WORLD);
        MPI_Send(liczby_tab, wartosc, MPI_DOUBLE, 1, 102, MPI_COMM_WORLD);
        cout << "Proces nr." << rank << " Wartosc: " << wartosc << " oraz tablica wyslane do procesu: " << rank +1 << endl;
        delete[] liczby_tab;
        plik_txt.close();
        MPI_Recv(&suma, 1, MPI_DOUBLE, 1, 102, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        cout << "Proces nr." << rank << " Suma liczb z tablicy: " << suma << endl;
    }
    if (rank == 1){
        int wartosc;
        MPI_Recv(&wartosc, 1, MPI_INT, 0, 102, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        double *liczby_tab = new double[wartosc];
        MPI_Recv(liczby_tab, wartosc, MPI_DOUBLE, 0, 102, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        double suma = 0;
        for (int i = 0; i < wartosc; i++){
            suma += liczby_tab[i];
        }

        cout << "Proces nr." << rank << " Suma liczb z tablicy: " << suma << endl;
        MPI_Send(&suma, 1, MPI_DOUBLE, 0, 102, MPI_COMM_WORLD);
    }
    
    MPI_Finalize();
    return 0;
}