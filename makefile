#
# Makefile for iPic3D mini-app
# V. Olshevsky 2018
#
CPP = mpicxx
include = ./src/include/
OPTFLAGS = -lstdc++ -O3 -DNO_HDF5 -I${include} -I/usr/lib/openmpi/include/
#OPTFLAGS = -O3 -DNO_HDF5 -fopt-info-vec -pg -I${include}

#INC_HDF5 = $(HDF5_INC)

#HDF5LIBS = -lhdf5_hl -lhdf5
#LIB_HDF5 = ${HDF5_CPP_LIB} ${HDF5_LIB} ${SZIP_LIB} -lz

objects = iPIC3Dlib.o Parameters.o iPICmini.o Collective.o VCtopology3D.o Com3DNonblk.o Grid3DCU.o EMfields3D.o Particles3Dcomm.o Particles3D.o ConfigFile.o TimeTasks.o IDgenerator.o MPIdata.o Timing.o ParallelIO.o debug.o asserts.o errors.o BcFields3D.o Basic.o Moments.o EllipticF.o GMRES.o

ipic-mini: ${objects}
	${CPP} ${OPTFLAGS} -o iPICmini ${INC_MPI} ${objects} ${LIB_MPI}

iPICmini.o: ./src/iPICmini.cpp
	${CPP} ${OPTFLAGS} ${INC_MPI} -c ./src/iPICmini.cpp 

Collective.o: ./src/main/Collective.cpp
	${CPP} ${OPTFLAGS} -c ./src/main/Collective.cpp

iPIC3Dlib.o: ./src/main/iPIC3Dlib.cpp
	${CPP} ${OPTFLAGS} -c ./src/main/iPIC3Dlib.cpp

Parameters.o: ./src/main/Parameters.cpp
	${CPP} ${OPTFLAGS} -c ./src/main/Parameters.cpp

VCtopology3D.o: ./src/communication/VCtopology3D.cpp
	${CPP} ${OPTFLAGS} -c ./src/communication/VCtopology3D.cpp

Com3DNonblk.o: ./src/communication/Com3DNonblk.cpp
	${CPP} ${OPTFLAGS} -c ./src/communication/Com3DNonblk.cpp

Grid3DCU.o: ./src/grids/Grid3DCU.cpp Com3DNonblk.o
	${CPP} ${OPTFLAGS} -c ./src/grids/Grid3DCU.cpp

EMfields3D.o: ./src/fields/EMfields3D.cpp
	${CPP} ${OPTFLAGS} -c ./src/fields/EMfields3D.cpp

Moments.o: ./src/fields/Moments.cpp
	${CPP} ${OPTFLAGS} -c ./src/fields/Moments.cpp

MPIdata.o: ./src/utility/MPIdata.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/MPIdata.cpp

TimeTasks.o: ./src/utility/TimeTasks.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/TimeTasks.cpp

IDgenerator.o: ./src/utility/IDgenerator.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/IDgenerator.cpp

Basic.o: ./src/utility/Basic.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/Basic.cpp

debug.o: ./src/utility/debug.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/debug.cpp

errors.o: ./src/utility/errors.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/errors.cpp

asserts.o: ./src/utility/asserts.cpp
	${CPP} ${OPTFLAGS} -c ./src/utility/asserts.cpp

ConfigFile.o: ./src/ConfigFile/ConfigFile.cpp
	${CPP} ${OPTFLAGS} -c ./src/ConfigFile/ConfigFile.cpp

Timing.o: ./src/performances/Timing.cpp
	${CPP} ${OPTFLAGS} -c ./src/performances/Timing.cpp

Particles3Dcomm.o: ./src/particles/Particles3Dcomm.cpp
	${CPP} ${OPTFLAGS} -c ./src/particles/Particles3Dcomm.cpp

Particles3D.o: ./src/particles/Particles3D.cpp 
	${CPP} ${OPTFLAGS} -c ./src/particles/Particles3D.cpp

ParallelIO.o: ./src/inputoutput/ParallelIO.cpp
	${CPP} ${OPTFLAGS} -c ./src/inputoutput/ParallelIO.cpp

BcFields3D.o: ./src/bc/BcFields3D.cpp
	${CPP} ${OPTFLAGS} -c ./src/bc/BcFields3D.cpp

EllipticF.o: ./src/mathlib/EllipticF.cpp
	${CPP} ${OPTFLAGS} -c ./src/mathlib/EllipticF.cpp

GMRES.o: ./src/solvers/GMRES.cpp
	${CPP} ${OPTFLAGS} -c ./src/solvers/GMRES.cpp

.PHONY : clean
clean:
	rm -rf *.o iPICmini
