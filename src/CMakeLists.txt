cmake_minimum_required(VERSION 3.8)
project(iPICmini LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS  "-O3 -DNO_HDF5 -DUSE_CATALYST")
#set(ParaView_DIR "/home/steven/Programs/ParaView-v5.6.0/build")

find_package(MPI)
include_directories(SYSTEM ${MPI_INCLUDE_PATH})
include_directories(include)
add_definitions(-DOMPI_SKIP_MPICXX)

add_subdirectory(catalyst)
include_directories(catalyst)


file(
        GLOB
        src_files
        ConfigFile/*.cpp
        PSKOutput3D/*.cpp
        bc/*.cpp
        communication/*.cpp
        fields/*.cpp
        grids/*.cpp
        inputoutput/*.cpp
        mathlib/*.cpp
        mpidata/*.cpp
        particles/*.cpp
        performances/*.cpp
        processtopology/*.cpp
        solvers/*.cpp
        utility/*.cpp
        main/*.cpp
)

# Particle solver
add_executable(
        iPICmini
	iPICmini.cpp
)

add_library(
    iPIC3Dlib      #name of the library
	SHARED	   #type of the library
    ${src_files}
)

target_link_libraries(
        iPICmini
        iPIC3Dlib
	${MPI_C_LIBRARIES}
	catalystAdaptor
)

## debug releases have a _d appended to the executable
set_target_properties(iPICmini PROPERTIES DEBUG_POSTFIX "_d")

message("Which system am I compiling for:")
message("MYHOSTNAME is ${myhostname}")
message("CMAKE_SYSTEM_PROCESSOR is ${CMAKE_SYSTEM_PROCESSOR}")
message("MPI_LIBRARIES is ${MPI_LIBRARIES}")
