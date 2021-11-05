#include <iostream>
#include <mpi.h>
#include <unistd.h>
#include <stdlib.h>
using namespace std;
// int fun_Max_Szukaj(int tab[], int n_){
    //     int n_ = tab[0];
    //     for (int i=1;i < n;i++){
    //         if (tab[i] > n_){
    //             n_ = tab[i];
    //         }
    //     }
    //     return n_;
    // }
    //test
int main(int argc, char *argv[]){
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int n;
    
    

    if (rank == 0){
        cout << "Podaj wielkosc tablicy: " << endl;
        cin >> n;
    }
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    sleep(rank);
    srand(time(NULL));
    
    int *tab = new int[n];
    int tab_Max = 0, proc_Max;
    cout << "Wygenerowane wartosci: ";
    for(int i = 0; i < n; i++){
        
        tab[i] = rand() % 10+1;
        cout << tab[i] << " ";
        if (tab_Max < tab[i]){
            tab_Max = tab[i];
        }
    }
    cout << "\nWartosc maksymalna tablicy procesu " << rank << " : " << tab_Max << endl;
    MPI_Reduce(&tab_Max, &proc_Max, 1, MPI_INT, MPI_MAX, 1, MPI_COMM_WORLD);

    
    
    if (rank == 1){
        cout << "Wartosc maksymalna wszystkich procesow: " << proc_Max << endl;
    }
    delete[] tab;
    MPI_Finalize();
    return 0;
}