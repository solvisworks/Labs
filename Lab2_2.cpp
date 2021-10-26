#include <iostream>
#include <mpi.h>
using namespace std;

int main(int argc, char *argv[]){
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0){
        double a = 10;
        cout << "Proces " << rank << " odebral liczbe: " << a << endl;
        MPI_Send(&a, 1, MPI_DOUBLE, 1, 102, MPI_COMM_WORLD);
        MPI_Recv(&a, 1, MPI_DOUBLE, size-1, 102, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    }
    if (rank > 0 && rank < size-1){
        double b;
        MPI_Recv(&b, 1, MPI_DOUBLE, rank-1, 102, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        cout << "Proces "<< rank << " odebral liczbe : " << b << endl;
        b+=1;
        cout << "Proces "<< rank << " wysyla liczbe : " << b << " do procesu: " << rank+1 << endl; 
        MPI_Send(&b, 1, MPI_DOUBLE, rank+1, 102, MPI_COMM_WORLD);
        
    }
    if (rank == size-1){
        double c;
        MPI_Recv(&c, 1, MPI_DOUBLE, rank-1, 102, MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        cout << "Proces "<< rank << " odebral liczbe : " << c << endl; 
        c+=1;
        MPI_Send(&c, 1, MPI_DOUBLE, 0, 102, MPI_COMM_WORLD);
        cout << "Proces "<< rank << " wysyla liczbe : " << c << " do procesu: " << 0 << endl; 
    }

    MPI_Finalize();
    return 0;
}