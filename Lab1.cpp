#include <iostream>
#include <mpi.h>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]){
    MPI_Init(&argc, &argv);
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    cout << "(Numer procesu) Rank: " << rank 
    << "\t Z :" << size << endl;
    MPI_Finalize();
    return 0;
}