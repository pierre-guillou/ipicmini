#
# makefile for iPic3D (3D null point simulations) for SuperMUC
# V. Olshevsky
#
CPP = mpicxx
include = ./include/
OPTFLAGS = -lstdc++ -O2 -DNO_HDF5 -I${include} -I/usr/lib/openmpi/include/
#OPTFLAGS = -O3 -DNO_HDF5 -fopt-info-vec -pg -I${include}

#INC_HDF5 = $(HDF5_INC)

#HDF5LIBS = -lhdf5_hl -lhdf5
#LIB_HDF5 = ${HDF5_CPP_LIB} ${HDF5_LIB} ${SZIP_LIB} -lz

objects = iPIC3Dlib.o Parameters.o iPICmini.o Collective.o VCtopology3D.o Com3DNonblk.o Grid3DCU.o EMfields3D.o Particles3Dcomm.o Particles3D.o ConfigFile.o TimeTasks.o IDgenerator.o MPIdata.o Timing.o ParallelIO.o debug.o asserts.o errors.o BcFields3D.o Basic.o Moments.o EllipticF.o GMRES.o

ipic-mini: ${objects}
	${CPP} ${OPTFLAGS} -o iPICmini ${INC_MPI} ${objects} ${LIB_MPI}

iPICmini.o: iPICmini.cpp
	${CPP} ${OPTFLAGS} ${INC_MPI} -c iPICmini.cpp 

Collective.o: ./main/Collective.cpp
	${CPP} ${OPTFLAGS} -c ./main/Collective.cpp

iPIC3Dlib.o: ./main/iPIC3Dlib.cpp
	${CPP} ${OPTFLAGS} -c ./main/iPIC3Dlib.cpp

Parameters.o: ./main/Parameters.cpp
	${CPP} ${OPTFLAGS} -c ./main/Parameters.cpp

VCtopology3D.o: ./communication/VCtopology3D.cpp
	${CPP} ${OPTFLAGS} -c ./communication/VCtopology3D.cpp

Com3DNonblk.o: ./communication/Com3DNonblk.cpp
	${CPP} ${OPTFLAGS} -c ./communication/Com3DNonblk.cpp

Grid3DCU.o: ./grids/Grid3DCU.cpp Com3DNonblk.o
	${CPP} ${OPTFLAGS} -c ./grids/Grid3DCU.cpp

EMfields3D.o: ./fields/EMfields3D.cpp
	${CPP} ${OPTFLAGS} -c ./fields/EMfields3D.cpp

Moments.o: ./fields/Moments.cpp
	${CPP} ${OPTFLAGS} -c ./fields/Moments.cpp

MPIdata.o: ./utility/MPIdata.cpp
	${CPP} ${OPTFLAGS} -c ./utility/MPIdata.cpp

TimeTasks.o: ./utility/TimeTasks.cpp
	${CPP} ${OPTFLAGS} -c ./utility/TimeTasks.cpp

IDgenerator.o: ./utility/IDgenerator.cpp
	${CPP} ${OPTFLAGS} -c ./utility/IDgenerator.cpp

Basic.o: ./utility/Basic.cpp
	${CPP} ${OPTFLAGS} -c ./utility/Basic.cpp

debug.o: ./utility/debug.cpp
	${CPP} ${OPTFLAGS} -c ./utility/debug.cpp

errors.o: ./utility/errors.cpp
	${CPP} ${OPTFLAGS} -c ./utility/errors.cpp

asserts.o: ./utility/asserts.cpp
	${CPP} ${OPTFLAGS} -c ./utility/asserts.cpp

ConfigFile.o: ./ConfigFile/src/ConfigFile.cpp
	${CPP} ${OPTFLAGS} -c ./ConfigFile/src/ConfigFile.cpp

Timing.o: ./performances/Timing.cpp
	${CPP} ${OPTFLAGS} -c ./performances/Timing.cpp

Particles3Dcomm.o: ./particles/Particles3Dcomm.cpp
	${CPP} ${OPTFLAGS} -c ./particles/Particles3Dcomm.cpp

Particles3D.o: ./particles/Particles3D.cpp 
	${CPP} ${OPTFLAGS} -c ./particles/Particles3D.cpp

ParallelIO.o: ./inputoutput/ParallelIO.cpp
	${CPP} ${OPTFLAGS} -c ./inputoutput/ParallelIO.cpp

BcFields3D.o: ./bc/BcFields3D.cpp
	${CPP} ${OPTFLAGS} -c ./bc/BcFields3D.cpp

EllipticF.o: ./mathlib/EllipticF.cpp
	${CPP} ${OPTFLAGS} -c ./mathlib/EllipticF.cpp

GMRES.o: ./solvers/GMRES.cpp
	${CPP} ${OPTFLAGS} -c ./solvers/GMRES.cpp

.PHONY : clean
clean:
	rm -rf *.o iPICmini
