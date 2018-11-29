cmake_minimum_required(VERSION 3.8) 

set(CMAKE_CXX_STANDARD 14)

set(CMAKE_CXX_FLAGS  "-O3 -DNO_HDF5")

find_package(MPI)
include_directories(SYSTEM ${MPI_INCLUDE_PATH})
include_directories(include)

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
        iPIC3D
	iPICmini.cpp
)

add_library(
    iPIC3Dlib      #name of the library
	SHARED	   #type of the library
    ${src_files}
)

target_link_libraries(
        iPIC3D
        iPIC3Dlib
	${MPI_C_LIBRARIES}
	catalystAdaptor
)
#target_link_libraries(${CMAKE_PROJECT_NAME} PUBLIC catalystAdaptor)


## to save the executable in the folder where the CMakeLists.txt file is, i.e. CMAKE_CURRENT_SOURCE_DIR
set_target_properties(iPIC3D PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

## debug releases have a _d appended to the executable
set_target_properties(iPIC3D PROPERTIES DEBUG_POSTFIX "_d")

message("Which system am I compiling for:")
message("MYHOSTNAME is ${myhostname}")
message("CMAKE_SYSTEM_PROCESSOR is ${CMAKE_SYSTEM_PROCESSOR}")
message("MPI_LIBRARIES is ${MPI_LIBRARIES}")
